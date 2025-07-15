import time

import cv2
from picamera2 import Picamera2

picam2 = Picamera2()
# Configurer pour la prévisualisation, ce qui est plus adapté pour un flux vidéo
camera_config = picam2.create_preview_configuration()
picam2.configure(camera_config)
picam2.start()

# Laisser le temps à la caméra de s'ajuster
time.sleep(2)

try:
    print("Affichage du flux vidéo. Appuyez sur 'q' dans la fenêtre pour quitter.")

    while True:
        # Capturer l'image sous forme de tableau NumPy (au format RGB)
        image_rgb = picam2.capture_array()

        # Convertir l'image de RGB (utilisé par picamera2) à BGR (utilisé par OpenCV)
        image_bgr = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        # Afficher l'image dans une fenêtre OpenCV
        cv2.imshow("Flux de la caméra", image_bgr)

        # Attendre une touche (pendant 1ms) et vérifier si c'est 'q' pour quitter
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("\nArrêt demandé par l'utilisateur.")

finally:
    # Arrêter la caméra et fermer toutes les fenêtres OpenCV
    picam2.stop()
    cv2.destroyAllWindows()
    print("Caméra et fenêtres fermées.")
