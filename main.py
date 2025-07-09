from utils.affichage import Affichage
from utils.reception_osc import Reception_osc
from utils.computation import *
import time
import threading
import pygame as pg

ip = "192.168.0.125" 
port_client = 12001
recept_port = 3335


def afficher():
    visualiser = Affichage(13.08, 7.77)
    computation= Computation()
    visualiser.add_button("points", "Points",True)
    visualiser.add_button("triangles", "Triangles Delaunay",True)
    visualiser.add_button("zones", "Candidats détectées",True)
    visualiser.add_button("expansion_candidate", "Expansion candidats",True)
    visualiser.add_button("triangles_v", "Triangles Vides",True)
    visualiser.add_button("expansion_empty", "Expansion vide",True)
    visualiser.add_button("areas", "Aires de Voronoi")
    visualiser.add_button("triangles_counts", "Nb voisins")
    visualiser.add_button("ids", "IDs")
    visualiser.add_button("final", "Finalisation",False)
    running=True
    while running and not stop_event.is_set():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                visualiser.quit()
                print("Arrêt du programme d'affichage")
                stop_event.set()
                return
            visualiser.handle_event(event)
        width = osc.scene_width
        height = osc.scene_height
        visualiser.update_size(width, height)
        positions = osc.get_positions()
        ages = osc.get_ages()
        computation.computation(positions,ages,width, height)
        computation.personnes_centrales(n_triangles=8,distance_min=0.8,angle_max=75,id_to_track=[])
        computation.empty_zones(area_threshold=2, radius=1.5)
        computation.expansion_candidates(ratio_threshold=1.3, min_density=1.2)
        computation.expansion_empty(ratio_threshold=1.3,min_density=1.2)
        visualiser.clear()
        visualiser.draw_expansion_empty(computation,"expansion_empty")
        visualiser.draw_empty(computation,"triangles_v")
        visualiser.draw_expansion_candidates(computation,"expansion_candidate")
        visualiser.draw_candidates(computation,"zones")
        visualiser.draw_final_zone(computation,"final")
        visualiser.draw_triangle(computation,"triangles")
        visualiser.draw_points(positions,"points")
        visualiser.draw_counts(computation,5,"triangles_counts")
        visualiser.draw_point_areas(computation,"areas")
        visualiser.draw_ids(computation,"ids")
        visualiser.update()
    visualiser.quit()



osc = Reception_osc(recept_port)
stop_event = threading.Event()


thread1 = threading.Thread(target=osc.run_server)
thread2 = threading.Thread(target=afficher)
thread1.start()
thread2.start()
try:
    while not stop_event.is_set():
        time.sleep(0.5)
    osc.stop_server()
except KeyboardInterrupt:
    osc.stop_server()
    stop_event.set()
thread1.join()  
thread2.join()
# Wait for threads to finish


print("Fin du programme")
