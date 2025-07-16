#!/usr/bin/env python3
# ...existing code...

from pythonosc.udp_client import SimpleUDPClient
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer
import time
import json
import requests
import os
import sys
sys.path.append(os.path.abspath('./utils'))
import reception_osc as reception_osc
import threading

# Paramètres OSC
ip = "127.0.0.1"  # Adresse IP du destinataire
send_port = 20000
recept_port = 3335
osc_address = "/worlds/world/children/scene/nodes/cloudRecorder1"  # Adresse OSC 
url = f"http://{ip}:{send_port}{osc_address}"  # URL pour accéder au fichier JSON /worlds/world/children/scene/nodes/cloudRecorder1/progression

 

def boucle():

    target_value = 0.0
    last_working_value = 0.0
    step = 0.01  # Valeur d'incrémentation pour l'offset
    client.send_message(f"{osc_address}/play", 1)
    time.sleep(3)
    while not stop_event.is_set() and step > 0.00001:
        #lire le contenu du json en 127.0.0.1:20000 a l'adresse osc_address
        target_value += step  # Réinitialiser la valeur d'offset à chaque itération
        if target_value > 1.0:
            target_value = 0.0
        client.send_message(f"{osc_address}/progression", target_value)
        time.sleep(0.1)
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                progression = data.get("CONTENTS", {}).get("progression", {}).get("VALUE", [None])[0]
                
                #print(f"Progression: {progression}, nb personnes: {len(recepteur.get_positions())}")
                
            else:
                print(f"Erreur lors de la récupération du JSON: {response.status_code}")
        except Exception as e:
            print(f"Exception lors de la récupération du JSON: {e}")
        if len(recepteur.get_positions()) == 2 and target_value > 0.2:
            print(f"progression non atteinte {target_value}")
            last_working_value = target_value-step
            target_value = last_working_value
            step /= 10
        time.sleep(1)
    print("fin de recherche du point de bug :", last_working_value)
    stop_event.set()
        

        
# Création du client OSC
client = SimpleUDPClient(ip, send_port)
recepteur = reception_osc.Reception_osc(3335)

print("Envoi automatique de l'offet")
print("CTRL+C pour quitter le programme")
print("")


stop_event = threading.Event()


thread1 = threading.Thread(target=recepteur.run_server)
thread2 = threading.Thread(target=boucle)
thread1.start()
thread2.start()
try:
    while not stop_event.is_set():
        time.sleep(0.5)
    recepteur.stop_server()
except KeyboardInterrupt:
    recepteur.stop_server()
    stop_event.set()
thread1.join()  
thread2.join()
# Wait for threads to finish


print("Fin du programme")
