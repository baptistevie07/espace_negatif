from pythonosc.udp_client import SimpleUDPClient

class Emission_osc:
    def __init__(self, ip="127.0.0.1", port=3336):
        self.client = SimpleUDPClient(ip, port)
        self.envoi("/area_on",0) # Initialisation à 0 pour éviter les erreurs de TouchDesigner
        
    def envoi(self,adresse, valeurs):
        
        self.client.send_message(adresse, valeurs)

