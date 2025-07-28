from pythonosc.udp_client import SimpleUDPClient
from pythonosc.dispatcher import Dispatcher
from pythonosc.osc_server import BlockingOSCUDPServer

class Emission_osc:
    def __init__(self, ip="127.0.0.1", port=3336):
        self.client = SimpleUDPClient(ip, port)

        
    def envoi(self,adresse, valeurs):
        
        self.client.send_message(adresse, valeurs)

