from matrix_util import *
import numpy as np

# vertices = [(1.0, 0.0, 0.0, 1), (0.0, -1.0, 0.0, 1), (0.0, 0.0, 1.0, 1),
#             (-2.0, 0.0, 0.0, 1), (0.0, 2.0, 0.0, 1), (0.0, 0.0, -2.0, 1)]
vertices = [
    ( 1, -1, -1, 1), # 0
    ( 1,  1, -1, 1), # 1
    (-1,  1, -1, 1), # 2
    (-1, -1, -1, 1), # 3
    ( 1, -1,  1, 1), # 4
    ( 1,  1,  1, 1), # 5
    (-1, -1,  1, 1), # 6
    (-1,  1,  1, 1), # 7
    ]

# surfaces = [(0, 1, 2), (0, 1, 5), (0, 2, 4), (0, 4, 5),
#             (1, 2, 3), (1, 3, 5), (2, 3, 4), (3, 4, 5)]
surfaces = [
    (0,1,2,3),
    (3,2,7,6),
    (6,7,5,4),
    (4,5,1,0),
    (1,5,7,2),
    (4,0,3,6),
    ]

normals = []

for surface in surfaces:
    # line1 = transformed.vertex2 - transformed.vertex1
    # line2 = transformed.vertex3 - transformed.vertex1
    # normal = Normalize(crossProduct(line1, line2))
    line1 = np.array(vertices[surface[1]][:3])-np.array(vertices[surface[0]][:3])
    line2 = np.array(vertices[surface[1]][:3])-np.array(vertices[surface[2]][:3])
    # print(list(line1), list(line2))
    normal = Normalize(crossProduct(line1, line2))
    normals.append(normal)

print(get_normals(vertices, surfaces))
