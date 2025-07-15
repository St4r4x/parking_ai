import time

from picamera2 import Picamera2

picam2 = Picamera2()
# Utiliser une configuration adaptée à la capture en mémoire
camera_config = picam2.create_still_configuration()
picam2.configure(camera_config)
picam2.start()

# Laisser le temps à la caméra de s'ajuster à la lumière
time.sleep(2)


try:
    print("Démarrage de la capture en mémoire. Appuyez sur Ctrl+C pour arrêter.")

    # Boucle de capture en continu
    while True:
        # Capturer l'image sous forme de tableau NumPy
        image_array = picam2.capture_array()

        print(
            f"Image capturée et stockée. Dimensions : {image_array.shape}")

        # Attendre 1 seconde avant la prochaine capture
        time.sleep(1)

except KeyboardInterrupt:
    print("\nArrêt de la capture demandé par l'utilisateur.")

finally:
    picam2.stop()
    print("Caméra arrêtée.")

    # Afficher un résumé des images capturées
    if captured_images:
        print(f"Total d'images stockées en mémoire : {len(captured_images)}")
        print(f"Dimensions de la dernière image : {captured_images[-1].shape}")
    else:
        print("Aucune image n'a été capturée.")
