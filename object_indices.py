import numpy as np

'''defines the indices of some common objects'''


# Cube
class cube:
    def __init__(self):
        # Define the 8 vertices of the cube
        self.vertices = np.array([\
        [-1, -1, -1],
        [+1, -1, -1],
        [+1, +1, -1],
        [-1, +1, -1],
        [-1, -1, +1],
        [+1, -1, +1],
        [+1, +1, +1],
        [-1, +1, +1]])

    # Define the 12 triangles composing the cube
        self.faces = np.array([\
            [0,3,1],
            [1,3,2],
            [0,4,7],
            [0,7,3],
            [4,5,6],
            [4,6,7],
            [5,1,2],
            [5,2,6],
            [2,3,6],
            [3,7,6],
            [0,1,5],
            [0,5,4]])

    def vertices(self):
        return self.vertices
    def faces(self):
        return self.faces

# Cylinder


# Triangle