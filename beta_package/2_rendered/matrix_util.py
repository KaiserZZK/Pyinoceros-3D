"""Zekai Zhang (zz2919@columbia.edu), 6 Nov 2022"""'''
# Defines core matrix operations for transforation.
'''

import math
from math import pow, sqrt
import numpy as np

def translate(pos):
    tx, ty, tz = pos
    return np.array([
        [1, 0, 0, 0],
        [0, 1, 0, 0],
        [0, 0, 1, 0],
        [tx, ty, tz, 1]
    ])

def rotate_x(a):
    return np.array([
        [1, 0, 0, 0],
        [0, math.cos(a), math.sin(a), 0],
        [0, -math.sin(a), math.cos(a), 0],
        [0, 0, 0, 1]
    ])

def rotate_y(a):
    return np.array([
        [math.cos(a), 0, -math.sin(a), 0],
        [0, 1, 0, 0],
        [math.sin(a), 0, math.cos(a), 0],
        [0, 0, 0, 1]
    ])

def rotate_z(a):
    return np.array([
        [math.cos(a), math.sin(a), 0, 0],
        [-math.sin(a), math.cos(a), 0, 0],
        [0, 0, 1, 0],
        [0, 0, 0, 1]
    ])

def scale(n):
    return np.array([
        [n, 0, 0, 0],
        [0, n, 0, 0],
        [0, 0, n, 0],
        [0, 0, 0, 1]
    ])


class Vector3:
    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z
        self.w = 1

    def __add__(a, b):
        if type(b) == Vector3:
            return Vector3(a.x + b.x, a.y + b.y, a.z + b.z)
        return Vector3(a.x + b, a.y + b, a.z + b)

    def __sub__(a, b):
        if type(b) == Vector3:
            return Vector3(a.x - b.x, a.y - b.y, a.z - b.z)
        return Vector3(a.x - b, a.y - b, a.z - b)

    def __mul__(a, b):
        if type(b) == Vector3:
            return Vector3(a.x * b.x, a.y * b.y, a.z * b.z)
        return Vector3(a.x * b, a.y * b, a.z * b)

    def __truediv__(a, b):
        if type(b) == Vector3:
            return Vector3(a.x / b.x, a.y / b.y, a.z / b.z)
        return Vector3(a.x / b, a.y / b, a.z / b)

    def norm(self):
        mg = sqrt(pow(self.x, 2) + pow(self.y, 2) + pow(self.z, 2))
        if mg == 0:
            self.x, self.y, self.z = 0, 0, 0
        else:
            self.x, self.y, self.z = self.x / mg, self.y / mg, self.z / mg

    def dot(self, b):
        return self.x * b.x + self.y * b.y + self.z * b.z

    def toMatrix(self):
        return [[self.x, self.y, self.z, self.w]]

    def GetTuple(self):
        return (int(self.x), int(self.y))

    def __repr__(self):
        # debug
        return f" vec3-> ({self.x}, {self.y}, {self.z})"

def crossProduct(a, b):
    x = a[1] * b[2] - a[2] * b[1]
    y = a[2] * b[0] - a[0] * b[2]
    z = a[0] * b[1] - a[1] * b[0]
    return Vector3(x, y, z)

def GetMagnitude(a):
    if type(a) == Vector3:
        return sqrt( pow(a.x,2) + pow(a.y,2) + pow(a.z,2) )
    else:
        return sqrt(pow(a.x,2) + pow(a.y,2))

def Normalize(a):
    mg = GetMagnitude(a)
    if mg == 0:
        return Vector3()
    return (a.x/mg, a.y/mg, a.z/mg)

def get_normals(v, s):
    normals = []
    vertices, surfaces = v, s
    for surface in surfaces:
        line1 = np.array(vertices[surface[1]][:3]) - np.array(vertices[surface[0]][:3])
        line2 = np.array(vertices[surface[1]][:3]) - np.array(vertices[surface[2]][:3])
        normal = Normalize(crossProduct(line1, line2))
        normals.append(normal)
    return normals