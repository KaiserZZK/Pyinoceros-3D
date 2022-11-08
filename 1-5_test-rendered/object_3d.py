"""Zekai Zhang (zz2919@columbia.edu), 6 Nov 2022"""'''
# documentations here  
'''

import pygame as pg
from math import *
from matrix_util import *

import OpenGL
from OpenGL.GL import *
from OpenGL.GLU import *

class Object3D:
    def __init__(self, render, v, s):
        self.render = render
        self.vertices = np.array(v)
        self.surfaces = np.array(s)
        self.rotation_speed = 0.002
        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_surfaces = [(pg.Color('orange'), surface) for surface in self.surfaces]
        self.movement_flag, self.draw_vertices = True, True
        self.label = ''

    def draw(self):
        self.screen_projection()
        self.movement()

    def movement(self):
        key = pg.key.get_pressed()
        if key[pg.K_m]:
            if self.movement_flag:
                self.rotate_y(-(pg.time.get_ticks() % 0.005))
            # change in y direction and its value seems to be reversed

    def light(self):
        normals = get_normals(self.vertices, self.surfaces)
        # colors = 0
        edges = self.get_edges(self.surfaces)
        # print(normals)
        # print(edges)

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glEnable(GL_LIGHTING)
        glEnable(GL_LIGHT0)
        glEnable(GL_COLOR_MATERIAL)
        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)

        glRotatef(1, 3, 1, 1)
        self.render_object(self.surfaces, normals, edges)

        glDisable(GL_LIGHT0)
        glDisable(GL_LIGHTING)
        glDisable(GL_COLOR_MATERIAL)

    def render_object(self, surfaces, normals, edges):
        glBegin(GL_QUADS)
        for i_surface, surface in enumerate(surfaces):
            x = 0
            glNormal3fv(normals[i_surface])
            for vertex in surface:
                x += 1
                # glColor3fv(colors[x])
                glColor3fv((0,0,1))
                glVertex3fv(verticies[vertex])
        glEnd()

        # glColor3fv(colors[0])
        glColor3fv((0,0,1))
        glBegin(GL_LINES)
        for edge in edges:
            for vertex in edge:
                glVertex3fv(verticies[vertex])
        glEnd()

    def get_edges(self, surfaces):
        output = set()
        for surface in surfaces:
            for i in range(len(surface)):
                output.add(tuple(sorted((surface[i], surface[(i + 1) % (len(surface))]))))
        return list(output)

    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:, :2]

        # for index, color_face in enumerate(self.color_faces):
        # for surface in self.surfaces:
        for index, color_surface in enumerate(self.color_surfaces):
            color, surface = color_surface
            polygon = vertices[surface]
            if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                pg.draw.polygon(self.render.screen, color, polygon, 3)
                # might need to come back and change color later
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color('white'))
                    self.render.screen.blit(text, polygon[-1])

        if self.draw_vertices:
            for vertex in vertices:
                if not np.any((vertex == self.render.H_WIDTH) | (vertex == self.render.H_HEIGHT)):
                    pg.draw.circle(self.render.screen, pg.Color('blue'), vertex, 6)

    def translate(self, pos):
        self.vertices = self.vertices @ translate(pos)

    def scale(self, scale_to):
        self.vertices = self.vertices @ scale(scale_to)

    def rotate_x(self, angle):
        self.vertices = self.vertices @ rotate_x(angle)

    def rotate_y(self, angle):
        self.vertices = self.vertices @ rotate_y(angle)

    def rotate_z(self, angle):
        self.vertices = self.vertices @ rotate_z(angle)


class Axes(Object3D):
    def __init__(self, render, v, s):
        super().__init__(render, v, s)
        self.vertices = v
        self.surfaces = s
        self.colors = [pg.Color('red'), pg.Color('green'), pg.Color('blue')]
        self.color_surfaces = [(color, surface) for color, surface in zip(self.colors, self.surfaces)]
        self.draw_vertices = False
        self.label = 'XYZ'