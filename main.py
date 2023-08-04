# Derived from GitHub page
# https://github.com/WoLpH/numpy-stl

import numpy as np
import stl.stl
from stl import mesh
import object_indices as ob
import object_utils as u
import math

# 1- ask for an object type to create mesh for
input_name = 'cube'

# 2- load the vertices and faces
if input_name == 'cube':
    my_cube = ob.cube()
    vertices = my_cube.vertices
    faces = my_cube.faces
    print(faces.shape)

print(faces.shape) # numpy array

vertices += 1
# Create the mesh
cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
for i, f in enumerate(faces):
    for j in range(3):
        cube.vectors[i][j] = vertices[f[j],:]


# 3- ask for alongations and rotations
# 3.1- get min max values for bounding box
minx, maxx, miny, maxy, minz, maxz = u.find_mins_maxs(cube)
w1 = maxx - minx
l1 = maxy - miny
h1 = maxz - minz

# 3.2- copy the main obj with min max values
copies = u.copy_obj(cube, (w1, l1, h1), 1, 1, 1)

# 3.3- repeat first and second step for the other object
cube2 = mesh.Mesh(cube.data.copy())

minx, maxx, miny, maxy, minz, maxz = u.find_mins_maxs(cube2)
w2 = maxx - minx
l2 = maxy - miny
h2 = maxz - minz

# translate to avoid collsions
cube2.y -= 2

# 3.4- combine those two objects
combined = mesh.Mesh(np.concatenate([cube.data, cube2.data] ))

#u.show_3d(cube, title='cube')
#u.show_3d(cube2, title='cube2')
u.show_3d(combined, title='combined')

# 4- save the final type to a folder
combined.save('stl_objects/combined.stl', mode=stl.stl.ASCII)  # save as ASCII

