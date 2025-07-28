#!/usr/bin/env python3
# ...existing code...

from pythonosc.udp_client import SimpleUDPClient
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer


class Reception_osc:
    def __init__(self, port_in):
        self.port_in = port_in
        self.clients = []
        self.positions={}
        self.ages = {}
        self.scene_width = 100.0  # Largeur de la scène
        self.scene_height = 100.0  # Hauteur de la scène

        dispatcher = Dispatcher()
        dispatcher.map("/au/*", self.address_logger)
        self.server = BlockingOSCUDPServer(("127.0.0.1", self.port_in), dispatcher)
        print("")
        print("Programme de réception des positions en cours, port ",self.port_in," ...")
        print("CTRL+C pour quitter le programme")
        print("")


    # Callback générique
    def address_logger(self,address, *args):
        
        #print("Message reçu :", address, args)
        
        if address == "/au/scene/size":
            
            self.scene_width = args[0]
            self.scene_height = args[2]
            
        
            
        elif address == "/au/frame/objList":
            keys = list(self.positions.keys())
            for obj in keys:
                if obj not in args:
                    del self.positions[obj]
                    del self.ages[obj]
                    #print("Objet supprimé : ",obj,", actuellement :", len(args), " objet(s) détecté(s)")
            for obj in args:
                if obj not in self.positions.keys():
                    self.positions[obj] = None
                    self.ages[obj] = 0
                    #print("Nouveau objet détecté : ",obj,", actuellement :", len(args), " objet(s) détecté(s)")
        
            
        else:
            for n_id in self.positions.keys():
                if address == "/au/"+str(n_id)+"/pos":
                    #print("Vitesse détectée pour l'objet", n_id, ":", args[0:3])
                    self.positions[n_id] = [args[0],args[2]]
                    break
                elif address == "/au/"+str(n_id)+"/age":
                    self.ages[n_id] = args[0]
            
    def run_server(self):
        self.server.serve_forever()
    def stop_server(self):
        """Arrête le serveur OSC"""
        self.server.shutdown()
        print("Serveur OSC arrêté")

    def get_positions(self):
        """Retourne les positions des objets détectés"""
        return self.positions
    def get_ages(self):
        """Retourne les âges des objets détectés"""
        return self.ages
