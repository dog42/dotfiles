import math
import FreeCAD
from FreeCAD import Vector
import Part
import Sketcher

doc = FreeCAD.newDocument("RevoMagBodyLeft_CAD")


def make_poly_face(pts_2d, z=0.0):
  vecs = [Vector(p[0], p[1], z) for p in pts_2d]
  if (vecs[0] - vecs[-1]).Length > 1e-5:
    vecs.append(vecs[0])
  wire = Part.makePolygon(vecs)
  return Part.Face(wire)


def extrude_poly(pts_2d, z0, z1):
  f = make_poly_face(pts_2d, z0)
  return f.extrude(Vector(0, 0, z1 - z0))


def make_plane_halfspace(point_on_plane, normal_outward, size=300.0, depth=60.0):
  """Create an analytical planar half-space box using only Part.Plane faces (no BSpline Lofts)."""
  n = Vector(normal_outward.x, normal_outward.y, normal_outward.z)
  n.normalize()
  # Find two orthogonal vectors u, v perpendicular to n
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


# ---------------------------------------------------------
# 1. BASE OUTER ENVELOPE (Z = 0 .. 17.75)
# ---------------------------------------------------------
outer_edges = []


def add_chain(pts_list):
  for k in range(len(pts_list) - 1):
    p1 = Vector(pts_list[k][0], pts_list[k][1], 0.0)
    p2 = Vector(pts_list[k + 1][0], pts_list[k + 1][1], 0.0)
    if (p2 - p1).Length > 1e-5:
      outer_edges.append(Part.LineSegment(p1, p2).toShape())


p_arc_end = Vector(20.93, 212.02, 0.0)
p_arc_mid = Vector(34.16, 209.08, 0.0)
p_arc_start = Vector(51.68, 214.42, 0.0)

chain_main = [
    (51.68, 214.42),
    (52.42, 213.77),
    (51.89, 176.41),
    (52.69, 174.98),
    (52.69, 171.09),
    (51.78, 169.66),
    (51.64, 169.20),
    (50.98, 120.66),
    (49.99, 57.36),
    (48.30, 22.36),
    (47.12, 20.36),
    (40.99, 20.36),
    (39.34, 18.68),
    (39.29, 8.80),
    (38.78, 8.00),
    (24.39, 2.75),
    (23.35, 3.30),
    (23.19, 18.98),
    (21.61, 20.36),
    (0.00, 20.36),
    (0.00, 60.36),
    (1.45, 64.33),
    (4.25, 64.30),
    (4.25, 61.12),
    (9.40, 61.12),
    (9.40, 78.06),
    (6.20, 78.06),
    (6.20, 94.06),
    (9.40, 94.06),
    (9.40, 163.47),
    (4.25, 163.47),
    (4.25, 160.10),
    (0.00, 160.10),
    (0.00, 184.56),
    (2.25, 189.56),
    (14.99, 189.56),
    (15.08, 196.83),
    (18.31, 196.97),
    (18.37, 209.61),
    (20.93, 212.02),
]
add_chain(chain_main)
outer_edges.append(Part.Arc(p_arc_end, p_arc_mid, p_arc_start).toShape())

outer_wire = Part.Wire(outer_edges)
base_solid = Part.Face(outer_wire).extrude(Vector(0, 0, 17.75))

# Fuse lower flared rear base (Z = 0 .. 4.30)
rear_flare_pts = [
    (22.78, 0.44),
    (43.89, 8.35),
    (47.12, 20.36),
    (6.00, 20.36),
    (8.72, 17.96),
    (15.55, 12.68),
    (15.74, 5.46),
]
rear_flare = extrude_poly(rear_flare_pts, 0.0, 4.30)
base_solid = base_solid.fuse(rear_flare)

# Rear nose bottom chamfers using pure analytical planes (0 BSplines!)
box_rear_clip = Part.makeBox(60, 34, 25, Vector(-2, -2, -2))
cut_rt = make_plane_halfspace(
    Vector(30.0, 7.50, 0.0), Vector(0.172, -0.470, -0.866)
)
cut_rr = make_plane_halfspace(
    Vector(43.50, 20.0, 0.0), Vector(0.511, -0.133, -0.849)
)
cut_rl = make_plane_halfspace(
    Vector(19.0, 7.50, 0.0), Vector(-0.325, -0.386, -0.864)
)
base_solid = base_solid.cut(cut_rt.common(box_rear_clip))
base_solid = base_solid.cut(cut_rr.common(box_rear_clip))
base_solid = base_solid.cut(cut_rl.common(box_rear_clip))

# ---------------------------------------------------------
# 2. RIGHT-SIDE 15-DEGREE CHAMFER (Z = 0 .. 10.5) - PURE PLANE
# ---------------------------------------------------------
n_rc = Vector(0.965062, -0.015106, -0.261584)
n_rc.normalize()
cut_rc = make_plane_halfspace(n_rc * 44.7726, n_rc, size=400.0, depth=40.0)
base_solid = base_solid.cut(cut_rc)

# ---------------------------------------------------------
# 3. REAR POCKET (Y = 22.36 .. 57.36, Z = 5.50 .. 20.0)
# ---------------------------------------------------------
rear_pocket = Part.makeBox(
    55.0, 57.36 - 22.36, 15.0, Vector(1.02, 22.36, 5.50)
)
base_solid = base_solid.cut(rear_pocket)

left_rear_step = Part.makeBox(2.10, 44.0, 15.0, Vector(-0.5, 20.36, 5.50))
base_solid = base_solid.cut(left_rear_step)

# ---------------------------------------------------------
# 4. MIDDLE SECTION TOP STEP, RIBS, AND SIDE CUTS (Y = 57.36 .. 120.66)
# ---------------------------------------------------------
mid_top_cut = Part.makeBox(
    47.02, 120.66 - 60.36, 10.0, Vector(-0.5, 60.36, 13.75)
)
base_solid = base_solid.cut(mid_top_cut)

mid_front_bar_cut = Part.makeBox(
    47.02, 60.36 - 57.36, 10.0, Vector(-0.5, 57.36, 14.55)
)
base_solid = base_solid.cut(mid_front_bar_cut)

# Fuse 5 analytical half-round ribs along X (R = 1.806 mm, Z_center = 12.744, Z_top = 14.55)
for yc, x_min, x_max in [
    (69.01, 9.40, 15.75),
    (69.01, 21.50, 46.52),
    (81.16, 6.20, 15.75),
    (81.16, 37.50, 46.52),
    (96.66, 9.40, 29.00),
    (108.66, 9.40, 46.52),
    (119.16, 9.40, 46.52),
]:
  rib_box = Part.makeBox(
      x_max - x_min, 3.20, 0.80, Vector(x_min, yc - 1.60, 13.75)
  )
  cyl_rib = Part.makeCylinder(
      1.806, x_max - x_min, Vector(x_min, yc, 12.744), Vector(1, 0, 0)
  )
  base_solid = base_solid.fuse(cyl_rib.common(rib_box))

# Cut the 3 rectangular top slots in the ribs (Z = 13.75 .. 15.0)
base_solid = base_solid.cut(
    Part.makeBox(15.75 - 9.40, 69.83 - 68.20, 2.0, Vector(9.40, 68.20, 13.75))
)
base_solid = base_solid.cut(
    Part.makeBox(15.75 - 6.20, 81.98 - 80.34, 2.0, Vector(6.20, 80.34, 13.75))
)
base_solid = base_solid.cut(
    Part.makeBox(29.00 - 9.40, 97.41 - 95.84, 2.0, Vector(9.40, 95.84, 13.75))
)

# Left tab undercuts at X = 6.20 .. 9.40:
base_solid = base_solid.cut(
    Part.makeBox(3.20, 5.00, 5.75, Vector(6.20, 78.06, 0.0))
)
base_solid = base_solid.cut(
    Part.makeBox(3.20, 11.00, 12.45, Vector(6.20, 83.06, 0.0))
)

# ---------------------------------------------------------
# 5. PARALLELOGRAM CUTOUT WITH TRUE R=1.5mm FILLET ARCS
# ---------------------------------------------------------
para_corners = [
    (16.24, 65.05),
    (42.39, 84.76),
    (42.39, 108.32),
    (16.24, 88.62),
]
para_wire = make_rounded_poly_wire(para_corners, [1.5, 1.5, 1.5, 1.5], z=-1.0)
para_cut = Part.Face(para_wire).extrude(Vector(0, 0, 22.0))
base_solid = base_solid.cut(para_cut)

para_step_corners = [
    (15.75, 64.68),
    (42.75, 85.03),
    (42.75, 108.59),
    (15.75, 88.25),
]
para_step_wire = make_rounded_poly_wire(
    para_step_corners, [1.5, 1.5, 1.5, 1.5], z=13.00
)
para_step_cut = Part.Face(para_step_wire).extrude(Vector(0, 0, 5.0))
base_solid = base_solid.cut(para_step_cut)

# ---------------------------------------------------------
# 6. TWO HORIZONTAL ANALYTICAL PINS (D = 3.00 mm, X = 9.40 .. 16.40)
# ---------------------------------------------------------
pin1 = Part.makeCylinder(
    1.50, 7.00, Vector(9.40, 107.565, 2.350), Vector(1, 0, 0)
)
pin2 = Part.makeCylinder(
    1.50, 7.00, Vector(9.40, 129.565, 3.250), Vector(1, 0, 0)
)
base_solid = base_solid.fuse(pin1).fuse(pin2)

# ---------------------------------------------------------
# 7. MIDDLE RAMP (Y = 120.66 .. 141.89) & FLOOR (Y = 141.89 .. 169.66, Z = 6.00)
# ---------------------------------------------------------
ramp_yz = [
    (120.66, 18.0),
    (120.66, 11.75),
    (141.89, 6.00),
    (169.66, 6.00),
    (169.66, 18.0),
]
ramp_vecs = [Vector(-1.0, p[0], p[1]) for p in ramp_yz]
ramp_vecs.append(ramp_vecs[0])
ramp_face = Part.Face(Part.makePolygon(ramp_vecs))
ramp_cut = ramp_face.extrude(Vector(49.0, 0, 0))
base_solid = base_solid.cut(ramp_cut)

rail_mid_cut = Part.makeBox(
    6.0, 169.66 - 120.66, 10.0, Vector(48.00, 120.66, 10.48)
)
base_solid = base_solid.cut(rail_mid_cut)

# ---------------------------------------------------------
# 8. BOTTOM TRIANGULAR POCKET (Z = 0 .. 2.45, PURE ANALYTICAL PLANES + CYLINDERS)
# ---------------------------------------------------------
tri_bot_mid = [
    (18.80, 152.10),
    (39.10, 167.05),
    (39.10, 180.00),
    (18.80, 180.00),
]
w_bot = make_rounded_poly_wire(tri_bot_mid, [1.5, 1.5, 1.5, 1.5], z=-0.01)
bot_pocket_ext = Part.Face(w_bot).extrude(Vector(0, 0, 2.46))
base_solid = base_solid.cut(bot_pocket_ext)

# ---------------------------------------------------------
# 9. FRONT SECTION (Y = 169.66 .. 214.42)
# ---------------------------------------------------------
# 9a. Front bottom 21-degree ramp (extruded along X = 12.69 .. 55.0)
fr_yz = [
    (184.63, -0.5),
    (216.0, -0.5),
    (216.0, 12.03),
    (184.63, 0.0),
]
fr_vecs = [Vector(12.69, p[0], p[1]) for p in fr_yz]
fr_vecs.append(fr_vecs[0])
cut_fr = Part.Face(Part.makePolygon(fr_vecs)).extrude(Vector(42.0, 0, 0))
base_solid = base_solid.cut(cut_fr)
base_solid = base_solid.cut(
    Part.makeBox(
        40.0, 189.56 - 185.33, 1.30, Vector(12.69, 185.33, 0.0)
    )
)

# Front-left lower bevel using pure analytical plane
n_fl = Vector(-0.890, 0.100, -0.445)
n_fl.normalize()
cut_fl = make_plane_halfspace(
    Vector(19.66, 190.29, 2.17), n_fl, size=100.0, depth=30.0
)
box_fl_clip = Part.makeBox(12.0, 26.0, 18.0, Vector(14.0, 189.56, 0.0))
base_solid = base_solid.cut(cut_fl.common(box_fl_clip))

# 9b. Front top steps (Y = 169.66 .. 189.96, X = 0 .. 48.00):
base_solid = base_solid.cut(
    Part.makeBox(
        48.5, 174.86 - 169.66, 5.0, Vector(-0.5, 169.66, 14.55)
    )
)
base_solid = base_solid.cut(
    Part.makeBox(
        48.5, 177.36 - 174.86, 6.0, Vector(-0.5, 174.86, 13.55)
    )
)
base_solid = base_solid.cut(
    Part.makeBox(
        48.5, 186.96 - 177.36, 5.0, Vector(-0.5, 177.36, 14.95)
    )
)
base_solid = base_solid.cut(
    Part.makeBox(
        48.5, 189.96 - 186.96, 5.0, Vector(-0.5, 186.96, 13.95)
    )
)

# Fuse Shell_1_TopInsert (X = 2.64 .. 33.12, Y = 177.36 .. 186.96, Z = 14.95 .. 15.45)
top_insert = Part.makeBox(
    33.12 - 2.0, 186.96 - 177.36, 0.50, Vector(2.0, 177.36, 14.95)
)
base_solid = base_solid.fuse(top_insert)

# Left circular arc step at X = 0 .. 5.50, Y = 174.56 .. 189.56 cut down to Z = 10.25
cyl_fl_arc = Part.makeCylinder(
    15.11, 10.0, Vector(-9.60, 186.23, 10.25), Vector(0, 0, 1)
)
box_fl_step = Part.makeBox(
    6.0, 189.96 - 174.56, 8.0, Vector(-0.5, 174.56, 10.25)
)
base_solid = base_solid.cut(cyl_fl_arc.common(box_fl_step))

# Right slot at X = 48.00 .. 49.28, Y = 169.66 .. 189.96 (Z = 12.75) and X = 49.28 .. 49.75 (Z = 14.55)
base_solid = base_solid.cut(
    Part.makeBox(
        49.28 - 48.00, 189.96 - 169.66, 6.0, Vector(48.00, 169.66, 12.75)
    )
)
base_solid = base_solid.cut(
    Part.makeBox(
        49.75 - 49.28, 189.96 - 169.66, 5.0, Vector(49.28, 169.66, 14.55)
    )
)

# 9c. Front-top pockets at Y = 189.96 .. 209.50:
base_solid = base_solid.cut(
    Part.makeBox(
        49.42 - 36.51, 197.41 - 189.96, 5.0, Vector(36.51, 189.96, 14.85)
    )
)

# - Arc pocket X = 28.55 .. 49.28, Y = 197.41 .. 209.50 cut down to Z = 14.35
#   (outside concentric cylinder center=(33.963, 239.699), R = 33.90 mm,
#    and outside R = 4.60 mm clearance around Boss_Front1 at (33.70, 195.06)!)
cyl_front_inner = Part.makeCylinder(
    33.90, 10.0, Vector(33.963, 239.699, 14.35), Vector(0, 0, 1)
)
cyl_boss3_clear = Part.makeCylinder(
    4.60, 10.0, Vector(33.70, 195.06, 14.35), Vector(0, 0, 1)
)
box_front_pocket = Part.makeBox(
    49.28 - 28.55, 211.0 - 197.41, 6.0, Vector(28.55, 197.41, 14.35)
)
pocket_front_1435 = box_front_pocket.cut(cyl_front_inner).cut(cyl_boss3_clear)
base_solid = base_solid.cut(pocket_front_1435)

# Front raised L-block (X = 25.55 .. 28.55, Y = 196.65 .. 206.21 and X = 25.55 .. 33.70, Y = 196.65 .. 199.65) up to Z = 21.15
l_block1 = Part.makeBox(
    28.55 - 25.55, 206.21 - 196.65, 21.15 - 17.75, Vector(25.55, 196.65, 17.75)
)
l_block2 = Part.makeBox(
    33.70 - 25.55, 199.65 - 196.65, 21.15 - 17.75, Vector(25.55, 196.65, 17.75)
)
base_solid = base_solid.fuse(l_block1).fuse(l_block2)

# Small cylindrical nub on right rail (Y = 173.05, Z = 17.75, R = 0.85 along X = 49.75 .. 52.42)
nub_cyl = Part.makeCylinder(
    0.85, 52.42 - 49.75, Vector(49.75, 173.05, 17.75), Vector(1, 0, 0)
)
base_solid = base_solid.fuse(nub_cyl)

# ---------------------------------------------------------
# 10. THREE ANALYTICAL SCREW BOSSES (D=5.70) & FOUR HOLES (3x D=2.60, 1x D=3.10)
# ---------------------------------------------------------
boss1 = Part.makeCylinder(2.85, 20.05 - 17.0, Vector(31.750, 14.862, 17.0))
boss2 = Part.makeCylinder(2.85, 20.05 - 13.0, Vector(45.400, 64.360, 13.0))
boss3 = Part.makeCylinder(2.85, 21.15 - 14.0, Vector(33.700, 195.060, 14.0))

base_solid = base_solid.fuse(boss1).fuse(boss2).fuse(boss3)

hole1 = Part.makeCylinder(1.30, 15.0, Vector(31.750, 14.862, 7.75))
hole2 = Part.makeCylinder(1.30, 15.0, Vector(45.400, 64.360, 7.75))
hole3 = Part.makeCylinder(1.30, 15.0, Vector(33.700, 195.060, 7.75))
hole4 = Part.makeCylinder(1.55, 8.0, Vector(45.900, 193.862, 8.75))

base_solid = base_solid.cut(hole1).cut(hole2).cut(hole3).cut(hole4)

final_solid = base_solid.removeSplitter().Solids[0]

print("Final analytical solid:")
print("  ShapeType:", final_solid.ShapeType)
print("  Faces count:", len(final_solid.Faces))
print("  Edges count:", len(final_solid.Edges))
print("  Vertices count:", len(final_solid.Vertexes))
print("  isValid:", final_solid.isValid())
print("  isClosed:", final_solid.isClosed())
print("  Volume:", round(final_solid.Volume, 2))

surf_types = {}
for f in final_solid.Faces:
  st = type(f.Surface).__name__
  surf_types[st] = surf_types.get(st, 0) + 1
print("  Surface types:", surf_types)
