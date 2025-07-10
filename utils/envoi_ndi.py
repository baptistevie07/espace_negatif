import pygame as pg
import numpy as np
import NDIlib as ndi
import time
if not ndi.initialize():
    raise RuntimeError("NDI initialization failed")

class NDI_Sender:
    def __init__(self, name="Pygame NDI Stream", width=1000, height=594):
        self.height, self.width = height, width  # NDI attend (hauteur, largeur)
        print(f"Creating NDI sender with name: {name}, size: ({self.width}, {self.height})")

        # Création du sender NDI
        send_settings = ndi.SendCreate()
        send_settings.ndi_name = name.encode('utf-8')  # important : bytes
        self.sender = ndi.send_create(send_settings)

        if self.sender is None:
            raise RuntimeError("Failed to create NDI sender")

        self.video_frame = ndi.VideoFrameV2()        
        self.video_frame.FourCC = ndi.FOURCC_VIDEO_TYPE_BGRX

    def send(self, screen: pg.Surface):
        if screen.get_size() != (self.width, self.height):
            print(f"Resizing screen from {screen.get_size()} to {(self.width, self.height)}")
        # Resize la surface pour matcher la taille attendue
            screen = pg.transform.smoothscale(screen,( self.height, self.width))
        # Récupérer les pixels en RGB
        arr = pg.surfarray.pixels3d(screen)
        arr = np.transpose(arr, (1, 0, 2))  # passer de (x, y, rgb) à (y, x, rgb)
        bgrx = np.zeros((self.width, self.height, 4), dtype=np.uint8)
        bgrx[:, :, :3] = arr[:, :, ::-1]  # inverse les canaux RGB → BGR

        self.video_frame.data = bgrx
        ndi.send_send_video_v2(self.sender, self.video_frame)
        # Convertir en BGRX (ordre inversé + canal X plein)
        

        # Affecter au frame
        #self.video_frame.data = bgrx_array.tobytes()

        # Envoi
        #ndi.send_send_video_v2(self.sender, self.video_frame)

    def __del__(self):
        if hasattr(self, 'sender'):
            ndi.send_destroy(self.sender)
        ndi.destroy()