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
        self.screen = pg.display.set_mode((self.width+250, self.height))
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
            self.screen = pg.display.set_mode((self.width+250, self.height))

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
                area = areas.get(i, None)
                if area is None or area == np.inf:
                    continue
                radius = int(ma.sqrt(area) * self.ratio / 5)
                x = int(x * self.ratio)
                y = self.height - int(y * self.ratio)
                # Draw the circle
                pg.draw.circle(self.screen, (0, 0, 255), (x, y), radius, 3)


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

    def draw_counts(self, points, triangle_counts,number,label):
        """Draws the number of triangles around each point, only the top 'number' points."""
        if triangle_counts is None or points is None:
            return
        if self.parametres.buttons[label].active:
            # Sort points by the number of triangles
            sorted_points = sorted(triangle_counts.items(), key=lambda x: x[1], reverse=True)
            top_points = [(idx, count) for idx, count in sorted_points if count >= number]
            for idx, (point_idx, count) in enumerate(top_points):
                point = points[point_idx]
                x, y = point
                x = int(x * self.ratio)
                y = self.height - int(y * self.ratio)

                pg.draw.circle(self.screen, (255, 255, 255), (x, y), 10)
                # Draw the count as text
                font = pg.font.Font(None, 24)
                text_surface = font.render(str(count), True, (255, 0, 0))
                text_rect = text_surface.get_rect(center=(x, y))
                self.screen.blit(text_surface, text_rect)
        
    def draw_zones(self, points, tri, candidates, label):
        """Dessine les zones autour des triangles connectés aux points spécifiés dans 'candidates'."""
        if tri is None or points is None or not candidates:
            return
        if not self.parametres.buttons[label].active:
            return
        candidate_set = set(candidates)
        for simplex in tri.simplices:
            if any(vertex in candidate_set for vertex in simplex):
                pts = points[simplex]
                pts = [(int(pt[0]*self.ratio), self.height-int(pt[1]*self.ratio)) for pt in pts]
                pg.draw.polygon(self.screen, (255, 0, 0, 100), pts)  # zone rouge semi-transparente
        # Tracer un disque sur chaque candidat
        for idx in candidate_set:
            if 0 <= idx < len(points):
                x, y = points[idx]
                x = int(x * self.ratio)
                y = self.height - int(y * self.ratio)
                pg.draw.circle(self.screen, (255, 255, 0), (x, y), 18, 0)  # disque jaune plein

    def draw_ids(self, points, label):
        """Draws the IDs of the objects at their positions."""
        if self.parametres.buttons[label].active:
            for idx, pos in enumerate(points):
                if pos is not None:
                    x, y = pos
                    # Normalize coordinates to fit within the screen dimensions
                    x = int(x * self.ratio) + 15
                    y = self.height - int(y * self.ratio) - 15
                    # Draw the ID as text
                    font = pg.font.Font(None, 24)
                    text_surface = font.render(str(idx), True, (0, 0, 0))
                    text_rect = text_surface.get_rect(center=(x, y))
                    # Draw a white rectangle as background for better readability
                    rect_bg = text_rect.inflate(6, 4)
                    pg.draw.rect(self.screen, (255, 255, 255), rect_bg)
                    self.screen.blit(text_surface, text_rect)
    def draw_empty_triangles(self, empty_triangles,points,label):
        """Draws the empty triangles."""
        """empty_triangles is a dictionary with keys as triangle indices and values as lists of [area, point1, point2, point3]"""
        if type(empty_triangles)=='NoneType' or points is None:
            return
        if not self.parametres.buttons[label].active:
            return
        for idx, (area, p1, p2, p3) in empty_triangles.items():
            if p1 is None or p2 is None or p3 is None:
                continue
            # Normalize coordinates to fit within the screen dimensions
            x1, y1 = points[p1]
            x2, y2 = points[p2]
            x3, y3 = points[p3]
            x1 = int(x1 * self.ratio)
            y1 = self.height - int(y1 * self.ratio)
            x2 = int(x2 * self.ratio)
            y2 = self.height - int(y2 * self.ratio)
            x3 = int(x3 * self.ratio)
            y3 = self.height - int(y3 * self.ratio)
            # Draw the triangle
            pg.draw.polygon(self.screen, (180, 0, 0), [(x1, y1), (x2, y2), (x3, y3)])
        #triangles : {idx: [area, point1, point2, point3]}
    def add_button(self, name, text, active=False):
        """Adds a button to the display."""
        self.parametres.add_button(name, text, self.width,active)