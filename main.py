import os
import subprocess
import time

import cv2
import numpy as np
from picamera2 import Picamera2

picam2 = Picamera2()
# Utiliser une configuration adaptée à la capture en mémoire
camera_config = picam2.create_still_configuration(main={"size": (1024, 576)})
picam2.configure(camera_config)
picam2.start()

# Laisser le temps à la caméra de s'ajuster à la lumière
time.sleep(2)

# Créer un nom de fichier temporaire pour l'image de la plaque
temp_image_path = "/tmp/plate.png"

try:
    print("Démarrage de la détection en arrière-plan. Appuyez sur Ctrl+C pour arrêter.")

    # Boucle de capture en continu
    while True:
        # Capturer l'image sous forme de tableau NumPy (format RGB)
        image_array = picam2.capture_array()

        # Convertir en niveaux de gris pour le traitement
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        gray = cv2.bilateralFilter(gray, 11, 17, 17)

        edged = cv2.Canny(gray, 30, 200)  # Détection des contours

        # Remplacement de imutils.grab_contours
        contours_tuple = cv2.findContours(
            edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = contours_tuple[0] if len(
            contours_tuple) == 2 else contours_tuple[1]

        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
        screenCnt = None

        # Boucle sur les contours
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * peri, True)
            if len(approx) == 4:
                screenCnt = approx
                break

        # Si un contour de plaque est trouvé, le traiter
        if screenCnt is not None:
            # Masquer tout sauf la plaque
            mask = np.zeros(gray.shape, np.uint8)
            cv2.drawContours(mask, [screenCnt], 0, 255, -1)

            # Extraire la plaque de l'image en niveaux de gris
            (x, y) = np.where(mask == 255)
            if x.size > 0 and y.size > 0:  # S'assurer que la plaque n'est pas vide
                (topx, topy) = (np.min(x), np.min(y))
                (bottomx, bottomy) = (np.max(x), np.max(y))
                Cropped = gray[topx:bottomx + 1, topy:bottomy + 1]

                # Sauvegarder l'image recadrée temporairement
                cv2.imwrite(temp_image_path, Cropped)

                # Utiliser subprocess pour appeler Tesseract
                try:
                    result = subprocess.run(
                        ['tesseract', temp_image_path, 'stdout',
                            '--psm', '11', '-l', 'eng'],
                        capture_output=True,
                        text=True,
                        check=True
                    )
                    text = result.stdout.strip()
                    if text:
                        print(f"Numéro détecté : {text}")
                except (subprocess.CalledProcessError, FileNotFoundError):
                    # Ignore les erreurs si tesseract ne trouve rien ou n'est pas installé
                    pass

        # Petite pause pour ne pas surcharger le CPU
        time.sleep(0.1)

except KeyboardInterrupt:
    print("\nArrêt de la détection demandé par l'utilisateur.")

finally:
    picam2.stop()
    # Supprimer le fichier temporaire
    if os.path.exists(temp_image_path):
        os.remove(temp_image_path)
    print("Caméra arrêtée.")
