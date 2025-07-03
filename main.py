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
                return
        positions = osc.get_positions()
        visualiser.clear()
        visualiser.draw_points(positions)
        visualiser.update()



osc = Reception_osc(recept_port)



thread1 = threading.Thread(target=osc.run_server)
thread2 = threading.Thread(target=afficher)
thread2.start()
thread1.start()
# Wait for threads to finish
thread1.join()  
thread2.join()

print("Fin du programme")


""""
 thread1 = threading.Thread(target=run_server, args=(server,))


    thread1.start()




    thread1.join()"""