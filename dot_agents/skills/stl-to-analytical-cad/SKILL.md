---
name: stl-to-analytical-cad
description: >-
  Reverse-engineers STL mesh files (including corrupted or non-manifold STLs) into
  100% native, analytical FreeCAD (.FCStd) and STEP (.step) CAD solids built exclusively
  from true mathematical planes (Part.Plane) and cylinders (Part.Cylinder) with zero mesh
  triangles. Use whenever the user asks to convert an STL file into a STEP or FreeCAD (.FCStd)
  file that can be cleanly edited in FreeCAD without crashing.
---

# STL to Analytical CAD Reverse Engineering (`stl-to-analytical-cad`)

When converting an STL file to STEP or FreeCAD (`.FCStd`) for CAD editing, **do NOT simply convert the mesh via `makeShapeFromMesh` + `removeSplitter()`**. Mesh-to-BRep conversion leaves hundreds of tessellated triangles on curved/filleted edges and slightly warped walls, which causes FreeCAD's OpenCASCADE kernel to lag or crash during Part Design operations.

Instead, perform **complete Analytical Reverse Engineering** by extracting exact 2D cross-sections, planes, and circles/arcs from the STL and rebuilding the solid from 100% native analytical CAD primitives (`Part.Plane` and `Part.Cylinder`).

## Step-by-Step Procedure

### 1. Geometry & Topology Extraction (Standalone `python3` + `numpy`)
* **Never run heavy `numpy` loops inside `freecadcmd`** (causes segfaults in FreeCAD's embedded Python). Always run mesh analysis in system `python3`.
* Split the STL into connected triangle shells to identify duplicate or internal sub-parts.
* Extract all axis-aligned planes ($X, Y, Z$) and tilted planes/chamfers/ramps ($\vec{n} \cdot \vec{x} = d$) weighted by triangle area.
* Slice the mesh along $Z$, $Y$, and $X$ at key heights, simplify collinear polygon chains (e.g., Ramer-Douglas-Peucker), and fit exact circles (`fit_circle_2d`) to all holes, bosses, pins, ribs, and rounded corners.

### 2. 100% Analytical CAD Rebuild (`freecadcmd` Script)
* Build the solid in `freecadcmd` using **only analytical surfaces** (`Part.Plane` and `Part.Cylinder`):
  * Extrude 2D wires (`Part.Wire` made of `Part.LineSegment` and `Part.ArcOfCircle`).
  * Use `Part.makeBox` and `Part.makeCylinder` for slots, pockets, bosses, pins, ribs, and holes.
  * **Avoid `Part.makeLoft`** for planar chamfers/ramps (since `makeLoft` creates `BSplineSurface` faces). Instead, cut tilted planes using an extruded planar half-space (`make_plane_halfspace`).
* Call `.removeSplitter()` at the end and verify:
  * `ShapeType == 'Solid'`, `isValid() == True`, `isClosed() == True`
  * Surface types contain only `'Plane'` and `'Cylinder'` (`0` mesh triangles, `0` BSplines).

### 3. Visual & Volumetric Verification (Mandatory)
* Verify that the volume of the analytical CAD solid matches the repaired STL volume within `< 0.5%`.
* Slice both the original STL and the new analytical CAD solid across at least 8 $Z$-levels (and $Y$-levels) and plot an overlay image (`Black = Original STL`, `Red dashed = Analytical CAD`) to verify that every step, pocket, ramp, rib, and hole matches accurately.

### 4. Export Deliverable Files
1. **`<name>.FCStd` (Native FreeCAD Project):**
   * Add the analytical solid as a `Part::Feature` (`BaseFeature`) inside an active **`PartDesign::Body`** so the user can immediately select any face/edge in FreeCAD's *Part Design* workbench and use *Sketch*, *Pocket*, *Pad*, *Chamfer*, or *Fillet*.
   * Store extracted 2D wire profiles as `Part::Feature` objects in a group (avoid `Sketcher::SketchObject` with `ArcOfCircle` in headless `freecadcmd`, as `doc.recompute()` segfaults without GUI).
   * Place any optional internal sub-parts in a separate group (`App::DocumentObjectGroup`).
2. **`<name>.step`:** Export via `final_solid.exportStep(...)`.
3. **`<name>_fixed.stl`:** Export a clean mesh from the analytical solid via `MeshPart.meshFromShape(Shape=final_solid, LinearDeflection=0.03, AngularDeflection=0.08)`.

## Reference Implementation
See [/home/dock/stl_zu_freecad_workflow.md](file:///home/dock/stl_zu_freecad_workflow.md) for reusable helper functions (`make_plane_halfspace`, `make_rounded_poly_wire`, `fit_circle_2d`).
