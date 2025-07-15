import os
import time

from picamera2 import Picamera2

# Créer un dossier pour sauvegarder les images s'il n'existe pas
output_dir = "captures"
os.makedirs(output_dir, exist_ok=True)

picam2 = Picamera2()
# Il n'est pas nécessaire d'avoir une configuration de prévisualisation pour la capture de fichiers
camera_config = picam2.create_still_configuration()
picam2.configure(camera_config)
picam2.start()

# Laisser le temps à la caméra de s'ajuster à la lumière
time.sleep(2)

try:
    print("Démarrage de la capture en continu. Appuyez sur Ctrl+C pour arrêter.")
    while True:
        # Générer un nom de fichier unique avec un horodatage
        timestamp = time.strftime("%Y%m%d-%H%M%S")
        filepath = os.path.join(output_dir, f"capture_{timestamp}.jpg")

        # Capturer l'image
        picam2.capture_file(filepath)
        print(f"Image capturée : {filepath}")

        # Attendre un court instant avant la prochaine capture
        time.sleep(1)  # Capturer une image chaque seconde

except KeyboardInterrupt:
    print("\nArrêt de la capture.")

finally:
    picam2.stop()
    print("Caméra arrêtée.")
