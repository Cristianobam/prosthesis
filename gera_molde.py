from vedo import *
import pygmsh

with pygmsh.occ.Geometry() as geom:
    geom.characteristic_length_min = 0.1
    geom.characteristic_length_max = 5
    rectangle = geom.add_rectangle([-80, -40, -100], 150.0, 50.0)
    geom.extrude(rectangle, [0, 0, 130])
    msh = geom.generate_mesh()

molde_positivo = Mesh('mama_restante_mirror.ply')
lines, triangles, tetras, vertices = msh.cells
molde_negativo_wire = TetMesh([msh.points, tetras[1]]).tomesh().color("b").wireframe(True)
molde_negativo_normal = TetMesh([msh.points, tetras[1]]).tomesh().color("b").wireframe(False)
molde_negativo_wire.cutWithMesh(molde_positivo, invert=True)
molde_negativo_normal.cutWithMesh(molde_positivo, invert=True)
molde_negativo_normal.pos(0,0,200)
show(molde_negativo_wire, molde_positivo, molde_negativo_normal, axes=dict(xtitle='x [\mum]')).close()

