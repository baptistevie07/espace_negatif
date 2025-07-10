import sys
import time
import numpy as np
import pygame
import NDIlib as ndi

def main():
    if not ndi.initialize():
        return 0

    # Création de l'émetteur NDI
    send_settings = ndi.SendCreate()
    send_settings.ndi_name = 'pygame-ndi'
    ndi_send = ndi.send_create(send_settings)
    if ndi_send is None:
        return 0

    # Initialiser Pygame
    width, height = 640, 480
    pygame.init()
    screen = pygame.Surface((width, height))
    clock = pygame.time.Clock()
    color = 0

    # Créer un objet vidéo_frame réutilisable
    video_frame = ndi.VideoFrameV2()
    video_frame.FourCC = ndi.FOURCC_VIDEO_TYPE_BGRX

    start = time.time()
    while time.time() - start < 60:  # pendant 60 secondes
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                ndi.send_destroy(ndi_send)
                ndi.destroy()
                pygame.quit()
                return 0

        # Dessin simple
        color = (color + 1) % 255
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, (0,0,color), (100, 100, 300, 200))
        #pygame.display.flip()

        # Convertir en image NumPy BGRX (NDI attend des strides alignés)
        #surf = pygame.display.get_surface()
        arr = pygame.surfarray.pixels3d(screen)
        arr = np.transpose(arr, (1, 0, 2))  # passer de (x, y, rgb) à (y, x, rgb)
        bgrx = np.zeros((height, width, 4), dtype=np.uint8)
        bgrx[:, :, :3] = arr[:, :, ::-1]  # inverse les canaux RGB → BGR

        video_frame.data = bgrx

        # Envoyer image
        ndi.send_send_video_v2(ndi_send, video_frame)

        clock.tick(30)

    ndi.send_destroy(ndi_send)
    ndi.destroy()
    pygame.quit()
    return 0

if __name__ == "__main__":
    sys.exit(main())
