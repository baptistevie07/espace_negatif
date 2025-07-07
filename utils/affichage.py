import pygame as pg
import numpy as np
import math as ma
from utils.pg_utils.buttons import Parametres

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
        self.screen = pg.display.set_mode((self.width+150, self.height))
        pg.display.set_caption("Visualisation des positions")
        self.clock = pg.time.Clock()
        self.running = True
        self.nb_max_pixels = nb_max_pixels
        self.real_width = width
        self.real_height = height
        self.parametres = Parametres()

    def clear(self):
        self.screen.fill((0, 0, 0))
    
    def handle_event(self, event):
        self.parametres.handle_event(event)

    def update(self):
        self.parametres.draw_params(self.screen, self.width, self.height)
        pg.display.flip()
        self.clock.tick(60)
        print(f"\rFPS: {self.clock.get_fps():.2f}                                             ", end="")

    def quit(self):
        self.screen.fill((0, 0, 0))  # fond noir
        pg.display.flip()
        pg.quit()

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
            self.screen = pg.display.set_mode((self.width+150, self.height))

    def draw_points(self, positions,label):
        '''positions is a dictionary with keys as object IDs and values as lists of [x, y] coordinates'''
        if self.parametres.buttons[label].active:
            for key in positions.keys():
                pos = positions[key]
                if pos is not None:
                    x, y = pos
                    # Normalize coordinates to fit within the screen dimensions
                    x = int(x*self.ratio)
                    y = self.height-int(y*self.ratio)
                    # Draw the point
                    pg.draw.circle(self.screen, (255, 255, 255), (x, y), 5)
    def draw_areas(self, points,areas,label):
        '''dessine un cercle autour de chaque point avec une taille proportionnelle à la surface'''
        if self.parametres.buttons[label].active:
            for i, point in enumerate(points):
                x, y = point
                if areas[i] == np.inf:
                    continue
                radius = int(ma.sqrt(areas[i])* self.ratio/10)
                x = int(x * self.ratio)
                y = self.height - int(y * self.ratio)
                # Draw the circle
                pg.draw.circle(self.screen, (0, 0, 255), (x, y), radius, 1)


    def draw_triangle(self, points, tri,label):
        if tri==None or points is None:
            return
        """Draws the triangles formed by the Delaunay triangulation."""
        if self.parametres.buttons[label].active:
            for simplex in tri.simplices:
                pts = points[simplex]
                pts = [(int(pt[0]*self.ratio), self.height-int(pt[1]*self.ratio)) for pt in pts]
                pts.append(pts[0])
                pg.draw.lines(self.screen, (0, 255, 0), False, pts, 1)

    def add_button(self, name, text, active=False):
        """Adds a button to the display."""
        self.parametres.add_button(name, text, self.width,active)