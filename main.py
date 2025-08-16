from utils.affichage import Affichage
from utils.reception_osc import Reception_osc
from utils.computation import *
from utils.area_life import Life
from utils.emission_osc import Emission_osc
import time
import threading
import pygame as pg

# Configuration des adresses IP et ports
augmenta_ip = "127.0.0.1"
augmenta_port = 3335
touchdesigner_ip = "192.168.10.239"
touchdesigner_port = 3336

# Variables de recherche (cf documentation dans le README)
n_triangles = 8
distance_min = 1.2
angle_max = 100
min_count = 2
min_dist = 3
ratio_threshold = 1.4
nb_min_region = 6
min_density = 1.5
max_dist_between_2_persons = 4.5
ratio_area = 2
min_ratio = 0.3
life_threshold = 3

def afficher():
    visualiser = Affichage(13.08, 7.77,sender=True)
    computation= Computation(filename="test1.csv")
    life = Life(min_ratio=min_ratio, life_threshold=life_threshold)
    
    visualiser.add_button("points", "Points",True)
    visualiser.add_button("triangles", "Triangles Delaunay",True)
    visualiser.add_button("zones", "Candidats détectées")
    visualiser.add_button("expansion_candidate", "Expansion candidats")
    visualiser.add_button("triangles_v", "Triangles Vides")
    visualiser.add_button("expansion_empty", "Expansion vide")
    visualiser.add_button("areas", "Aires de Voronoi")
    visualiser.add_button("triangles_counts", "Nb voisins")
    visualiser.add_button("ids", "IDs")
    visualiser.add_button("final", "Finalisation",True)
    running=True
    while running and not stop_event.is_set():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                visualiser.quit()
                computation.arret_enregistrement()
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
        computation.personnes_centrales(n_triangles=n_triangles,distance_min=distance_min,angle_max=angle_max,id_to_track=[])
        computation.empty_zones(area_threshold=3, radius=3)
        computation.expansion_candidates(ratio_threshold=ratio_threshold, min_density=min_density,ratio_area=ratio_area, nb_min_region=nb_min_region, max_dist_between_2_persons=max_dist_between_2_persons)
        computation.expansion_empty(ratio_threshold=ratio_threshold,min_density=min_density,ratio_area=ratio_area, nb_min_region=nb_min_region, max_dist_between_2_persons=max_dist_between_2_persons)
        life.update(computation)
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
        visualiser.draw_area_life(life)
        osc_sender.envoi("/area_on", life.area_on)
        visualiser.update()
    osc_sender.envoi("/area_on", 0)  # Stop sending area_on when quitting
    visualiser.quit()
    computation.arret_enregistrement()
    



osc = Reception_osc(ip=augmenta_ip, port_in=augmenta_port)
osc_sender = Emission_osc(ip=touchdesigner_ip, port=touchdesigner_port)
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
    osc_sender.envoi("/area_on", 0)  # Stop sending area_on when quitting
    stop_event.set()
osc_sender.envoi("/area_on", 0)  # Stop sending area_on when quitting
thread1.join()  
thread2.join()
# Wait for threads to finish


print("Fin du programme")
