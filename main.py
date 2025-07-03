from utils.affichage import Affichage
from utils.reception_osc import Reception_osc
import time
import threading
import pygame as pg

ip = "192.168.0.125" 
port_client = 12001
recept_port = 3335


def afficher():
    visualiser = Affichage(13.08, 7.77)
    running=True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                visualiser.quit()
                print("Arrêt du programme d'affichage")
                return
        positions = osc.get_positions()
        visualiser.clear()
        visualiser.draw_points(positions)
        visualiser.update()



osc = Reception_osc(recept_port)



thread1 = threading.Thread(target=osc.run_server)
thread2 = threading.Thread(target=afficher)
thread1.start()
thread2.start()
try:
    while True:
        time.sleep(0.5)
except KeyboardInterrupt:
    osc.stop_server()
    thread1.join()  
    thread2.join()
# Wait for threads to finish


print("Fin du programme")
