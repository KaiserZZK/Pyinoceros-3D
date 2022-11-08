import sys
import pygame
from pygame.locals import *

import numpy as np

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

from matrix_util import *

def get_object_from_file(input):
    vertices_in, surfaces_in = [], []
    if len(input) < 2:
        print('provide an object file');
        quit()
    elif len(input) > 2:
        print('provide ONE file only');
        quit()

    lines = open(input[1], 'r').readlines()
    counts = lines[0].split(",");
    vertices_count = int(counts[0])
    for vertex_raw in lines[1:vertices_count + 1]:
        vertex = [float(v) for v in vertex_raw.strip().split(",")[1:]]
        # vertex.append(1)
        vertices_in.append(tuple(vertex))
    for surface_raw in lines[vertices_count + 1:]:
        surface = [int(s) - 1 for s in surface_raw.strip().split(",")]
        surfaces_in.append(tuple(surface))

    return vertices_in, surfaces_in


def build():
    glBegin(GL_QUADS)
    for i_surface, surface in enumerate(surfaces):
        x = 0
        glNormal3fv(normals[i_surface])
        for vertex in surface:
            x+=1
            # glColor3fv(colors[x])
            glColor3fv((0,0,1))
            glVertex3fv(vertices[vertex])
    glEnd()

    # glColor3fv(colors[0])
    glColor3fv((0,0,1))
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

def control():
    mouse_pressed = pygame.mouse.get_pressed(num_buttons=3)[0]
    change_pos = pygame.mouse.get_rel()
    if mouse_pressed:
        if change_pos[0] > 0:
            glRotatef(1, 0, 1, 0)
        if change_pos[0] < 0:
            glRotatef(1, 0, -1, 0)
        if change_pos[1] > 0:
            glRotatef(1, 1, 0, 0)
        if change_pos[1] < 0:
            glRotatef(1, -1, 0, 0)
        if change_pos[1] < 0 and change_pos[0] > 0:
            glRotatef(1, 0, 0, -1)
        if change_pos[1] > 0 and change_pos[0] < 0:
            glRotatef(1, 0, 0, 1)

def get_edges(surfaces):
    output = set()
    for surface in surfaces:
        for i in range(len(surface)):
            output.add(tuple(sorted((surface[i], surface[(i + 1) % (len(surface))]))))
    return list(output)

vertices, surfaces = get_object_from_file(sys.argv)
edges = get_edges(surfaces)
normals = get_normals(vertices, surfaces)

def main():
    global surfaces

    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    clock = pygame.time.Clock()

    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0]/display[1]), 0.1, 50.0)

    glMatrixMode(GL_MODELVIEW)
    glTranslatef(0, 0, -5)

    #glLight(GL_LIGHT0, GL_POSITION,  (0, 0, 1, 0)) # directional light from the front
    glLight(GL_LIGHT0, GL_POSITION,  (5, 5, 5, 1)) # point light from the left, top, front
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0, 0, 0, 1))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1, 1, 1, 1))

    glEnable(GL_DEPTH_TEST)

    while True:

        pygame.display.set_caption("Rendered View")
        # pygame.display.set_mode((600, 600)).fill(pygame.Color('white'))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE )


        control()
        build()

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)

        pygame.display.flip()
        clock.tick(60)

main()