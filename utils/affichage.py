import pygame as py
import numpy as np
import math as ma

class Affichage:
    def __init__(self, width, height,nb_max_pixels=1000):
        if width>height:
            self.width=int(nb_max_pixels)
            self.height=int(height*nb_max_pixels/width)
            self.ratio = nb_max_pixels / width
        else:
            self.width=int(width*nb_max_pixels/height)
            self.height=int(nb_max_pixels)
            self.ratio = nb_max_pixels / height
        self.screen = py.display.set_mode((self.width, self.height))
        py.display.set_caption("Visualisation des positions")
        self.clock = py.time.Clock()
        self.running = True
        self.nb_max_pixels = nb_max_pixels
        self.real_width = width
        self.real_height = height

    def clear(self):
        self.screen.fill((0, 0, 0))

    def update(self):
        py.display.flip()
        self.clock.tick(60)

    def quit(self):
        self.screen.fill((0, 0, 0))  # fond noir
        py.display.flip()
        py.quit()

    def update_size(self, width, height):
        if self.real_width != width or self.real_height != height:
            self.real_width = width
            self.real_height = height
            #print("Mise à jour de la taille de l'affichage :", abs(self.width/self.ratio-width), abs(self.height/self.ratio-height))
            if width>height:
                self.width=int(self.nb_max_pixels)
                self.height=int(height*self.nb_max_pixels/width)
                self.ratio = self.nb_max_pixels / width
            else:
                self.width=int(width*self.nb_max_pixels/height)
                self.height=int(self.nb_max_pixels)
                self.ratio = self.nb_max_pixels / height
            self.screen = py.display.set_mode((self.width, self.height))

    def draw_points(self, positions):
        '''positions is a dictionary with keys as object IDs and values as lists of [x, y] coordinates'''
        for key in positions.keys():
            pos = positions[key]
            if pos is not None:
                x, y = pos
                # Normalize coordinates to fit within the screen dimensions
                x = int(x*self.ratio)
                y = self.height-int(y*self.ratio)
                # Draw the point
                py.draw.circle(self.screen, (255, 255, 255), (x, y), 5)
        py.draw.rect(self.screen, (255, 0, 0), (0, 0, self.width, self.height), 1)  # Draw a red rectangle around the screen