from utils.affichage import Affichage
import time

visualiser = Affichage(800, 600)
visualiser.clear()
visualiser.draw_points([[100, 100], [200, 200], [300, 300]])
visualiser.update()
time.sleep(2)  # Pause for 2 seconds to see the drawn points