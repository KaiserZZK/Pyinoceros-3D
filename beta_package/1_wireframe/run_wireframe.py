import sys
import pygame as pg
from camera_3d      import *
from projection_3d  import *
from object_3d      import *

class SoftwareRender:
    def __init__(self):
        pg.init()
        self.RES = self.WIDTH, self.HEIGHT = 600, 600
        self.H_WIDTH, self.H_HEIGHT = self.WIDTH // 2, self.HEIGHT // 2
        self.FPS = 60
        self.screen = pg.display.set_mode(self.RES)
        self.clock = pg.time.Clock()
        self.create_objects()

    def create_objects(self):
        self.camera = Camera(self, [0.5,1,5])
        self.projection = Projection(self)
        self.object = self.get_object_from_file(sys.argv)
        self.object.translate([0.2, 0.4, 0.2])
        axes_vertices = np.array([(0, 0, 0, 1), (1, 0, 0, 1), (0, 1, 0, 1), (0, 0, 1, 1)])
        axes_surfaces = np.array([(0, 1), (0, 2), (0, 3)])
        self.axes = Axes(self, axes_vertices, axes_surfaces)
        self.axes.translate([0.7,0.9,0.7])
        self.world_axes = Axes(self, axes_vertices, axes_surfaces)
        self.world_axes.movement_flag = False
        self.world_axes.scale(2.5)
        self.world_axes.translate([0.0001, 0.0001, 0.0001])


    def get_object_from_file(self, input):
        vertices_in, surfaces_in = [], []
        if len(input) < 2:
            print('provide an object file'); quit()
        elif len(input) > 2:
            print('provide ONE file only'); quit()

        lines = open(input[1], 'r').readlines()
        counts = lines[0].split(","); vertices_count = int(counts[0])
        for vertex_raw in lines[1:vertices_count + 1]:
            vertex = [float(v) for v in vertex_raw.strip().split(",")[1:]]
            vertex.append(1)
            vertices_in.append(tuple(vertex))
        for surface_raw in lines[vertices_count + 1:]:
            surface = [int(s) - 1 for s in surface_raw.strip().split(",")]
            surfaces_in.append(tuple(surface))

        return Object3D(self, vertices_in, surfaces_in)

    def draw(self):
        self.screen.fill(pg.Color('white'))
        key = pg.key.get_pressed()
        if key[pg.K_x]:
            self.world_axes.draw()
        self.object.draw()

    def run(self):
        while True:
            self.draw()
            self.camera.control()
            [exit() for i in pg .event.get() if i.type == pg.QUIT]
            pg.display.set_caption("Wireframe View  |  %.5f FPS" %(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)


if __name__ == '__main__':
    app = SoftwareRender()
    app.run()

