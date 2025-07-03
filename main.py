from utils.affichage import Affichage
from utils.reception_osc import Reception_osc
from utils.triangles import triangles
import time
import threading
import pygame as pg

ip = "192.168.0.125" 
port_client = 12001
recept_port = 3335


def afficher():
    visualiser = Affichage(13.08, 7.77)
    visualiser.parametres.add_button("start", "Start", visualiser.width)
    running=True
    while running and not stop_event.is_set():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                visualiser.quit()
                print("Arrêt du programme d'affichage")
                stop_event.set()
                return
        width = osc.scene_width
        height = osc.scene_height
        visualiser.update_size(width, height)
        positions = osc.get_positions()
        ages = osc.get_ages()
        points,tri= triangles(positions,ages,width, height)
        visualiser.clear()
        visualiser.draw_triangle(points, tri)
        visualiser.draw_points(positions)
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
