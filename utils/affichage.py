from matplotlib import text
import pygame as pg
import numpy as np
import math as ma
from utils.pg_utils.buttons import Parametres
from utils.envoi_ndi import NDI_Sender

class Affichage:
    def __init__(self, width, height,sender=True,nb_max_pixels=1000):
        if width>height:
            self.width=int(nb_max_pixels)
            self.height=int(height*nb_max_pixels/width)
            self.ratio = nb_max_pixels / width
        else:
            self.width=int(width*nb_max_pixels/height)
            self.height=int(nb_max_pixels)
            self.ratio = nb_max_pixels / height

        self.screen = pg.display.set_mode((self.width+250, self.height))
        if sender:
            self.screen_ndi = pg.Surface((self.width, self.height))
            #self.screen_ndi = pg.display.set_mode((self.width, self.height))
            self.sender = NDI_Sender("Espace_Negatif", self.width, self.height)
        else:
            self.screen_ndi = None
            self.sender = None
        pg.display.set_caption("Visualisation des positions")
        self.clock = pg.time.Clock()
        self.running = True
        self.nb_max_pixels = nb_max_pixels
        self.real_width = width
        self.real_height = height
        self.parametres = Parametres()

    def clear(self):
        self.screen.fill((0, 0, 0))
        if self.screen_ndi:
            self.screen_ndi.fill((0, 0, 0))
    
    def handle_event(self, event):
        self.parametres.handle_event(event)

    def update(self):
        self.parametres.draw_params(self.screen, self.width, self.height)
        pg.display.flip()
        if self.screen_ndi:
            self.sender.send(self.screen_ndi)
        self.clock.tick(60)
        print(f"\rFPS: {self.clock.get_fps():.2f}                                                                  ", end="")

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
            if self.screen_ndi:
                self.screen_ndi = pg.Surface((self.width, self.height))

                print(f"New size: {self.width}x{self.height}, ratio: {self.ratio}")

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
    
    def draw_triangle(self, computation, label):
        """Draws the triangles formed by the Delaunay triangulation."""
        if computation.tri is None or computation.points is None:
            return
        if self.parametres.buttons[label].active:
            for simplex in computation.tri.simplices:
                pts = computation.points[simplex]
                pts = [(int(pt[0]*self.ratio), self.height-int(pt[1]*self.ratio)) for pt in pts]
                pts.append(pts[0])
                pg.draw.lines(self.screen, (0, 255, 0), False, pts, 1)

    def draw_counts(self, computation, number, label):
        """Draws the number of triangles around each point, only the top 'number' points."""
        if computation.triangle_counts is None or computation.points is None:
            return
        if self.parametres.buttons[label].active:
            # Sort points by the number of triangles
            sorted_points = sorted(computation.triangle_counts.items(), key=lambda x: x[1], reverse=True)
            top_points = [(idx, count) for idx, count in sorted_points if count >= number]
            for idx, (point_idx, count) in enumerate(top_points):
                point = computation.points[point_idx]
                x, y = point
                x = int(x * self.ratio)
                y = self.height - int(y * self.ratio)

                pg.draw.circle(self.screen, (255, 255, 255), (x, y), 10)
                # Draw the count as text
                font = pg.font.Font(None, 24)
                text_surface = font.render(str(count), True, (255, 0, 0))
                text_rect = text_surface.get_rect(center=(x, y))
                self.screen.blit(text_surface, text_rect)

    def draw_point_areas(self, computation, label):
        '''dessine un cercle autour de chaque point avec une taille proportionnelle à la surface'''
        if self.parametres.buttons[label].active:
            if computation.points is None or computation.areas is None:
                return
            for i, point in enumerate(computation.points):
                x, y = point
                area = computation.areas.get(i, None)
                if area is None or area == np.inf:
                    continue
                radius = int(ma.sqrt(area) * self.ratio / 5)
                x = int(x * self.ratio)
                y = self.height - int(y * self.ratio)
                # Draw the circle
                pg.draw.circle(self.screen, (0, 0, 255), (x, y), radius, 3)

    def draw_candidates(self, computation, label):
        """Dessine les zones autour des triangles connectés aux points spécifiés dans 'candidates'."""
        if not self.parametres.buttons[label].active or computation.candidates is None:
            return
        self.draw_areas(computation, "candidates")
        # Tracer un disque sur chaque candidat
        for idx in computation.candidates:
            if 0 <= idx < len(computation.points):
                x, y = computation.points[idx]
                x = int(x * self.ratio)
                y = self.height - int(y * self.ratio)
                pg.draw.circle(self.screen, (255, 255, 0), (x, y), 18, 0)  # disque jaune plein

    def draw_ids(self, computation, label):
        """Draws the IDs of the objects at their positions."""
        if self.parametres.buttons[label].active:
            if computation.points is None:
                return
            for idx, pos in enumerate(computation.points):
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

    def draw_areas(self, computation, type):
        """Draws the empty triangles."""
        """empty_triangles is a dictionary with keys as triangle indices and values as lists of [point1, point2, point3]"""
        if computation.points is None:
            return
        if type == "central":
            if computation.empty_triangles is None:
                return
            triangles = []
            for ensemble in computation.empty_triangles:
                triangles.extend(list(ensemble.values()))
            color = (0, 0, 255) 
        elif type == "candidates":
            if computation.candidates_triangles is None:
                return
            #On cherche les ids des points des triangles dans self.region
            # Flatten all dict_values to get a list of triangle triplets
            triangles = []
            for ensemble in computation.candidates_triangles:
                triangles.extend(list(ensemble.values()))
            #print(f"candidats triangles : {triangles}")
            #triangles = computation.candidates_triangles.values()
            #triangles = list(set(triangles))  # Remove duplicates
            color= (255, 0, 0)
            
        elif type == "expansion_empty":
            if computation.region_empty is None:
                return
            #On cherche les ids des points des triangles dans self.region
            triangles = [computation.tri.simplices[simplex] for simplex in computation.region_empty if simplex < len(computation.tri.simplices)]
            color= (100, 100, 255)
        elif type == "expansion_candidates":
            if computation.region_candidates is None:
                return
            #On cherche les ids des points des triangles dans self.region
            triangles = [computation.tri.simplices[simplex] for simplex in computation.region_candidates]
            color= (180, 100, 100)
        elif type == "final" or type == "ndi":
            #print(f"Drawing final zone with type: {type}, taille region candidates : {len(computation.region_candidates) if computation.region_candidates else 'None'}, taille region empty : {len(computation.region_empty) if computation.region_empty else 'None'}")
            triangles =[]
            if computation.region_empty:
                triangles+=[computation.tri.simplices[simplex] for simplex in computation.region_empty if simplex < len(computation.tri.simplices)]
            if computation.region_candidates:
                triangles+=[computation.tri.simplices[simplex] for simplex in computation.region_candidates if simplex < len(computation.tri.simplices)]
            if not triangles:
                return
            color = (128, 128, 128)
        else:
            print(f"Type '{type}' non reconnu pour draw_areas.")
            return
        for (p1,p2,p3) in triangles:
            if p1 is None or p2 is None or p3 is None:
                continue
            # Normalize coordinates to fit within the screen dimensions
            x1, y1 = computation.points[p1]
            x2, y2 = computation.points[p2]
            x3, y3 = computation.points[p3]
            x1 = int(x1 * self.ratio)
            y1 = self.height - int(y1 * self.ratio)
            x2 = int(x2 * self.ratio)
            y2 = self.height - int(y2 * self.ratio)
            x3 = int(x3 * self.ratio)
            y3 = self.height - int(y3 * self.ratio)
            
            if type == "ndi":
                # Draw the triangle on the NDI surface
                pg.draw.polygon(self.screen_ndi, (255,255,255), [(x1, y1), (x2, y2), (x3, y3)])
            else:
                # Draw the triangle
                pg.draw.polygon(self.screen, color, [(x1, y1), (x2, y2), (x3, y3)])
        #triangles : {idx: [area, point1, point2, point3]}

    def draw_empty(self, computation, label):
        if not self.parametres.buttons[label].active:
            return
        self.draw_areas(computation, "central")

    def draw_expansion_empty(self, computation, label):
        if not self.parametres.buttons[label].active:
            return
        self.draw_areas(computation, "expansion_empty")

    def draw_expansion_candidates(self, computation, label):
        if not self.parametres.buttons[label].active:
            return
        self.draw_areas(computation, "expansion_candidates")

    def add_button(self, name, text, active=False):
        """Adds a button to the display."""
        self.parametres.add_button(name, text, self.width,active)

    def draw_final_zone(self, computation,label):
        if self.screen_ndi:
            self.draw_areas(computation, "ndi")
        if not self.parametres.buttons[label].active:
            return
        self.draw_areas(computation, "final")

    def list_to_dict(self,triangles,points):
        """Converts a list of triangles to a dictionary with triangle indices as keys and lists of points as values."""
        triangles_dict = {}
        for idx, triangle in enumerate(triangles):
            if len(triangle) == 3:
                triangles_dict[idx] = [points[triangle[0]], points[triangle[1]], points[triangle[2]]]
        return triangles_dict
    
    def draw_area_life(self, life, life_threshold):
        pg.draw.rect(self.screen, (128, 128, 128), (self.width +15, 25, 220, 20))
        if life>life_threshold:
            color = (0, 255, 0)
            pg.draw.rect(self.screen, color, (self.width +15, 25, 220, 20))
            font=pg.font.Font(None, 24)
            txt_surface = font.render(str(int(life))+" secondes", True, (255,255,255))
            txt_rect = txt_surface.get_rect(center=(self.width + 15 + 110, 25 + 10))
            self.screen.blit(txt_surface, txt_rect)
        else:
            color = (255, 0, 0)
            pg.draw.rect(self.screen, color, (self.width +15, 25, int(220*life/life_threshold), 20))
