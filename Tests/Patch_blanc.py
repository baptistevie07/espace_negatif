#!/usr/bin/env python3
# ...existing code...

from pythonosc.udp_client import SimpleUDPClient
import time
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
  # URL pour accéder au fichier JSON /worlds/world/children/scene/nodes/cloudRecorder1/progression

def reinitialisation():
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/updateFileList", 1)
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/updateFileList", 1)
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder/stop", 1)
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/stop", 1)
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/stop", 1)
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder/loopRange", [0,1])
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/loopRange", [0,1])
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/loopRange", [0,1])
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder/progression", 0)
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/progression", 0)
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/progression", 0)

def rerecord(zone_a_effacer,nom_fichier,num_fichier):
    osc_address = "/worlds/world/children/scene/nodes"  # Adresse OSC 
    url = f"http://{ip}:{send_port}{osc_address}" 
    state =1
    print("Initialisation patch bug...")
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/updateFileList", 1)
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/updateFileList", 1)
    time.sleep(1)
    reinitialisation()
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/recordingFiles", f"{nom_fichier}_{num_fichier}.json")
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/recordFileName", f"{nom_fichier}_{num_fichier+1}")
    time.sleep(1)
    print(f"Début programme de rerecording avec patchs blancs, fichier: {nom_fichier}_{num_fichier}.json, zone à effacer: {zone_a_effacer}")
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/play", 1)
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/record", 1)
    print("Envoi de la commande de lecture pour cloudRecorder1 et record", time.strftime("%H:%M", time.localtime()))
    
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
            if progression >zone_a_effacer:
                state = 2
                
                client.send_message("/worlds/world/children/scene/nodes/cloudRecorder/play", 1)
                
                print("Envoi de la commande de lecture pour cloudRecorder", time.strftime("%H:%M", time.localtime()))
        if state ==2:
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
            if progression >zone_a_effacer+0.001:
                state = 3
                
                client.send_message("/worlds/world/children/scene/nodes/cloudRecorder/stop", 1)
                print("Envoi de la commande de stop pour cloudRecorder", time.strftime("%H:%M", time.localtime()))
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
            if progression >0.9999 or progression<0.1:
                state = 4
                
                client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/stop", 1)
                time.sleep(1)
                client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/stop", 1)
                print("Envoi de la commande de stop pour cloudRecorder1 et cloudRecorder2", time.strftime("%H:%M", time.localtime()))


        
        time.sleep(0.1)
        
        
        
    print("fin de recherche du rerecording")
    print("")
    
def recherche_bug(nom_fichier,num_fichier):
    
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/updateFileList", 1)
    time.sleep(1)
    reinitialisation()
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/recordingFiles", f"{nom_fichier}_{num_fichier}")
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/stop", 1)
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/play", 1)
    target_value = 0.0
    last_working_value = 0.0
    step = 0.1 
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/play", 1)
    print("Recherche du point de bug...")
    time.sleep(3)
    while not stop_event.is_set() and step > 0.0001:
        #lire le contenu du json en 127.0.0.1:20000 a l'adresse osc_address
        target_value += step  # Réinitialiser la valeur d'offset à chaque itération
        #print(f"    Envoi de la progression: {target_value}")
        if target_value >= 1.0:
            return None
        client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/progression", round(target_value, 4))
        time.sleep(1)
        #print(len(recepteur.get_positions())," personnes détectées")
        if len(recepteur.get_positions()) <= 2 and target_value > 0.2:
            print(f"    progression non atteinte {target_value}")
            last_working_value = target_value-step
            target_value = last_working_value
            step /= 10
        
    print("fin de recherche du point de bug :", last_working_value)
    print("")
    return last_working_value    
  
def boucle(num_fichier=2,fichier="rerecording"):
    
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder1/directory", os.path.abspath('./records_augmenta'))
    client.send_message("/worlds/world/children/scene/nodes/cloudRecorder2/directory", os.path.abspath('./records_augmenta'))
    reinitialisation()
    bugs=[]
    while not stop_event.is_set():
        zone_a_effacer = recherche_bug(nom_fichier=fichier,num_fichier=num_fichier)
        if zone_a_effacer is None:
            print("Aucun bug trouvé, arrêt du programme")
            stop_event.set()
            return
        bugs.append(zone_a_effacer)
        rerecord(zone_a_effacer,fichier,num_fichier)
        num_fichier += 1
    print("Rerecording terminé, bugs trouvés :", bugs)
    stop_event.set()

        
# Création du client OSC
client = SimpleUDPClient(ip, send_port)
recepteur = reception_osc.Reception_osc(3335)

print("Rerecording avec patchs blancs")
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
