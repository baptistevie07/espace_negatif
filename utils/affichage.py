import pygame as py
import numpy as np

class Affichage:
    def __init__(self, width, height,nb_max_pixels=1000):
        if width>height:
            self.width=int(nb_max_pixels)
            self.height=int(height*nb_max_pixels/width)
        else:
            self.width=int(width*nb_max_pixels/height)
            self.height=int(nb_max_pixels)
        self.screen = py.display.set_mode((self.width, self.height))
        self.clock = py.time.Clock()
        self.running = True
        self.nb_max_pixels = nb_max_pixels

    def clear(self):
        self.screen.fill((0, 0, 0))

    def update(self):
        py.display.flip()
        self.clock.tick(60)

    def quit(self):
        py.quit()

    def draw_points(self, points):
        '''points is a list of lists [x,y]'''
        for point in points:
            if len(point) == 2:
                x, y = point
                py.draw.circle(self.screen, (255, 255, 255), (int(x), int(y)), 5)