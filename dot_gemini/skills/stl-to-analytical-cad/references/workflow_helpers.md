# Wiederverwendbare Python-Hilfsfunktionen für `freecadcmd` & `numpy`

## 1. Ebenen-Halbraum ohne BSpline-Flächen (`make_plane_halfspace`)
Vermeidet `Part.makeLoft` (welches `BSplineSurface` erzeugt) und schneidet Fasen/Schrägen als echte mathematische `Part.Plane`:

```python
from FreeCAD import Vector
import Part


def make_plane_halfspace(point_on_plane, normal_outward, size=300.0, depth=60.0):
    """Erzeugt einen analytischen Halbraum-Quader nur aus Part.Plane-Flächen."""
    n = Vector(normal_outward.x, normal_outward.y, normal_outward.z)
    n.normalize()
    ref = Vector(1, 0, 0) if abs(n.x) < 0.9 else Vector(0, 1, 0)
    u = n.cross(ref)
    u.normalize()
    v = n.cross(u)
    v.normalize()
    p0 = point_on_plane - u * (size * 0.5) - v * (size * 0.5)
    p1 = p0 + u * size
    p2 = p1 + v * size
    p3 = p0 + v * size
    f = Part.Face(Part.makePolygon([p0, p1, p2, p3, p0]))
    return f.extrude(n * depth)
```

## 2. 2D-Polygon mit echten Kreisbogen-Verrundungen (`make_rounded_poly_wire`)
Erzeugt aus Eckpunkten und Eckenradien einen geschlossenen `Part.Wire` aus echten `Part.LineSegment`- und `Part.Arc`-Elementen (sodass bei der Extrusion echte `Part.Cylinder`-Flächen entstehen):

```python
import math
from FreeCAD import Vector
import Part


def make_rounded_poly_wire(corners_2d, radii, z=0.0):
    n = len(corners_2d)
    pts = [Vector(c[0], c[1], z) for c in corners_2d]
    tangent_pts = []
    for i in range(n):
        p_prev = pts[(i - 1) % n]
        p_curr = pts[i]
        p_next = pts[(i + 1) % n]
        r = radii[i]
        if r <= 1e-4:
            tangent_pts.append((p_curr, None, p_curr))
            continue
        v1 = p_prev - p_curr
        v2 = p_next - p_curr
        v1.normalize()
        v2.normalize()
        cos_a = max(-1.0, min(1.0, v1.dot(v2)))
        half_a = 0.5 * math.acos(cos_a)
        dist = r / math.tan(half_a)
        t1 = p_curr + v1 * dist
        t2 = p_curr + v2 * dist
        bis = v1 + v2
        bis.normalize()
        center_dist = r / math.sin(half_a)
        c = p_curr + bis * center_dist
        p_mid = c - bis * r
        tangent_pts.append((t1, p_mid, t2))

    edges = []
    for i in range(n):
        t1, p_mid, t2 = tangent_pts[i]
        if p_mid is not None:
            edges.append(Part.Arc(t1, p_mid, t2).toShape())
        t1_next, _, _ = tangent_pts[(i + 1) % n]
        if (t2 - t1_next).Length > 1e-5:
            edges.append(Part.LineSegment(t2, t1_next).toShape())
    return Part.Wire(edges)
```

## 3. Algebraic Circle Fit (in `python3` / `numpy`) zur Radien-Extraktion
Findet Mittelpunkt $(c_x, c_y)$ und Radius $R$ aus geslicten 2D-Punkten:

```python
import numpy as np


def fit_circle_2d(pts_2d):
    x, y = pts_2d[:, 0], pts_2d[:, 1]
    A = np.column_stack([x, y, np.ones_like(x)])
    b = -(x**2 + y**2)
    sol, _, _, _ = np.linalg.lstsq(A, b, rcond=None)
    cx, cy = -sol[0] / 2.0, -sol[1] / 2.0
    r = np.sqrt(cx**2 + cy**2 - sol[2])
    max_err = np.abs(np.hypot(x - cx, y - cy) - r).max()
    return cx, cy, r, max_err
```
