import pygame
import numpy as np
import time
import NDIlib as ndi

# --- Initialisation NDI ---
#if not ndi.util.initialize():
 #   raise Exception("NDI library not initialized")

sender = ndi.send.Sender("Pygame NDI Stream")

# --- Initialisation Pygame ---
width, height = 640, 480
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

running = True
color_val = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Dessin : rectangle avec couleur changeante
    screen.fill((0, 0, 0))
    color_val = (color_val + 1) % 255
    pygame.draw.rect(screen, (color_val, 100, 255 - color_val), (100, 100, 200, 150))

    # Convertir la surface en image NumPy (RGB)
    surface = pygame.display.get_surface()
    array = pygame.surfarray.array3d(surface)
    array = np.rot90(array)  # pour corriger orientation
    array = np.fliplr(array)  # corriger mirroring
    array = np.ascontiguousarray(array)

    # Envoyer via NDI
    sender.send_video(array)

    pygame.display.flip()
    clock.tick(30)  # Limite à 30 FPS

# --- Nettoyage ---
pygame.quit()
sender.close()
ndi.util.destroy()
