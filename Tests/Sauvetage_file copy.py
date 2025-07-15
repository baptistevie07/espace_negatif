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
osc_address = "/worlds/world/children/scene/nodes"  # Adresse OSC 
url = f"http://{ip}:{send_port}{osc_address}"  # URL pour accéder au fichier JSON /worlds/world/children/scene/nodes/cloudRecorder1/progression

 

def boucle():
    state =1
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/play", 1)
    
    
    while not stop_event.is_set() and state<4:
        #lire le contenu du json en 127.0.0.1:20000 a l'adresse osc_address
        if state ==1:
            progression = 0.0
            try:
                response = requests.get(url+"/cloudRecorder1")
                if response.status_code == 200:
                    data = response.json()
                    progression = data.get("CONTENTS", {}).get("progression", {}).get("VALUE", [None])[0]
                    
                    #print(f"Progression: {progression}, nb personnes: {len(recepteur.get_positions())}")
                    
                else:
                    print(f"Erreur lors de la récupération du JSON: {response.status_code}")
            except Exception as e:
                print(f"Exception lors de la récupération du JSON: {e}")
            if progression >0.02:
                state = 2
                
                client.send_message("/worlds/world/children/scene/nodes/cloudRecorder/play", 1)
                client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/record", 1)
        if state ==2:
            progression = 0.0
            try:
                response = requests.get(url+"/cloudRecorder")
                if response.status_code == 200:
                    data = response.json()
                    progression = data.get("CONTENTS", {}).get("progression", {}).get("VALUE", [None])[0]
                    
                    #print(f"Progression: {progression}, nb personnes: {len(recepteur.get_positions())}")
                    
                else:
                    print(f"Erreur lors de la récupération du JSON: {response.status_code}")
            except Exception as e:
                print(f"Exception lors de la récupération du JSON: {e}")
            if progression >0.37:
                state = 3
                
                client.send_message("/worlds/world/children/scene/nodes/cloudRecorder/stop", 1)
        if state ==3:
            progression = 0.0
            try:
                response = requests.get(url+"/cloudRecorder1")
                if response.status_code == 200:
                    data = response.json()
                    progression = data.get("CONTENTS", {}).get("progression", {}).get("VALUE", [None])[0]
                    
                    #print(f"Progression: {progression}, nb personnes: {len(recepteur.get_positions())}")
                    
                else:
                    print(f"Erreur lors de la récupération du JSON: {response.status_code}")
            except Exception as e:
                print(f"Exception lors de la récupération du JSON: {e}")
            if progression >0.99:
                state = 4
                
                client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/stop", 1)
                client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/stop", 1)


        
        time.sleep(0.1)
        
        
        
    print("fin de recherche du rerecording")
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
