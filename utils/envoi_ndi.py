import pygame as pg
import numpy as np
import NDIlib as ndi
import time
if not ndi.initialize():
    raise RuntimeError("NDI initialization failed")

class NDI_Sender:
    def __init__(self, name="Pygame NDI Stream", size=(1280, 720)):
        self.size = (1250, 746)

        # Création du sender NDI
        send_settings = ndi.SendCreate()
        send_settings.ndi_name = name.encode('utf-8')  # important : bytes
        self.sender = ndi.send_create(send_settings)

        if self.sender is None:
            raise RuntimeError("Failed to create NDI sender")

        self.img = np.ones((746,1250,  4), dtype=np.uint8)

        self.video_frame = ndi.VideoFrameV2()

        self.video_frame.data = self.img
        self.video_frame.FourCC = ndi.FOURCC_VIDEO_TYPE_BGRX

    def send(self, screen: pg.Surface):
        if screen.get_size() != self.size:
            print(f"Resizing screen from {screen.get_size()} to {self.size}")
        # Resize la surface pour matcher la taille attendue
            screen = pg.transform.smoothscale(screen, self.size)
        # Récupérer les pixels en RGB
        rgb_bytes = pg.image.tostring(screen, "RGB")
        rgb_array = np.frombuffer(rgb_bytes, dtype=np.uint8).reshape((self.size[1], self.size[0], 3))

        bgr_array = rgb_array[:, :, ::-1]
        bgrx_array = np.concatenate([bgr_array, np.full((self.size[1], self.size[0], 1), 255, dtype=np.uint8)], axis=2)

        idx = int(time.time()) % 2  # Pour alterner les couleurs
        #self.img.fill(255 if idx % 2 else 0)
        self.img[:] = bgrx_array
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
