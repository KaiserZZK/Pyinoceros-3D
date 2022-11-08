"""Zekai Zhang (zz2919@columbia.edu), 6 Nov 2022"""'''
# Handling the rotation and transformation of objects   
'''

import pygame as pg
from math import *
from matrix_util import *

class Object3D:
    def __init__(self, render, v, s):
        self.render = render
        self.vertices = np.array(v)
        self.surfaces = np.array(s)
        self.rotation_speed = 0.002
        self.font = pg.font.SysFont('Arial', 30, bold=True)
        self.color_surfaces = [(pg.Color('darkblue'), surface) for surface in self.surfaces]
        self.movement_flag, self.draw_vertices = True, True
        self.label = ''

    def draw(self):
        self.screen_projection()
        self.movement()

    def movement(self):
        mouse_pressed = pg.mouse.get_pressed(num_buttons=3)[0]
        change_pos = pg.mouse.get_rel()
        if mouse_pressed and self.movement_flag:
            if change_pos[0] > 0:
                self.rotate_y(-(pg.time.get_ticks() % 0.005))
            if change_pos[0] < 0:
                self.rotate_y((pg.time.get_ticks() % 0.005))
            if change_pos[1] > 0:
                self.rotate_x((pg.time.get_ticks() % 0.005))
            if change_pos[1] < 0:
                self.rotate_x(-(pg.time.get_ticks() % 0.005))
            if change_pos[1] < 0 and change_pos[0] > 0:
                self.rotate_z(-(pg.time.get_ticks() % 0.005))
            if change_pos[1] > 0 and change_pos[0] < 0:
                self.rotate_z((pg.time.get_ticks() % 0.005))

    def screen_projection(self):
        vertices = self.vertices @ self.render.camera.camera_matrix()
        vertices = vertices @ self.render.projection.projection_matrix
        vertices /= vertices[:, -1].reshape(-1, 1)
        vertices[(vertices > 2) | (vertices < -2)] = 0
        vertices = vertices @ self.render.projection.to_screen_matrix
        vertices = vertices[:, :2]

        for index, color_surface in enumerate(self.color_surfaces):
            color, surface = color_surface
            polygon = vertices[surface]
            if not np.any((polygon == self.render.H_WIDTH) | (polygon == self.render.H_HEIGHT)):
                pg.draw.polygon(self.render.screen, color, polygon, 3)
                if self.label:
                    text = self.font.render(self.label[index], True, pg.Color('white'))
                    self.render.screen.blit(text, polygon[-1])

        if self.draw_vertices:
            for vertex in vertices:
                if not np.any((vertex == self.render.H_WIDTH) | (vertex == self.render.H_HEIGHT)):
                    pg.draw.circle(self.render.screen, pg.Color('darkblue'), vertex, 6)

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