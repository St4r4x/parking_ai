import time

import imutils
import numpy as np
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
        img = cv2.resize(image_array, (620, 480))
        # convert to grey scale
        gray = cv2.cvtColor(image_array, cv2.COLOR_BGR2GRAY)
        gray = cv2.bilateralFilter(gray, 11, 17, 17)

        edged = cv2.Canny(gray, 30, 200)  # Perform Edge detection
        cnts = cv2.findContours(
            edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        cnts = imutils.grab_contours(cnts)
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:10]
        screenCnt = None
        # loop over our contours
        for c in cnts:
            # approximate the contour
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.018 * peri, True)
            # if our approximated contour has four points, then
            # we can assume that we have found our screen
            if len(approx) == 4:
                screenCnt = approx
                break

        # Masking the part other than the number plate
        mask = np.zeros(gray.shape, np.uint8)
        new_image = cv2.drawContours(mask, [screenCnt], 0, 255, -1,)
        new_image = cv2.bitwise_and(img, img, mask=mask)

        (x, y) = np.where(mask == 255)
        (topx, topy) = (np.min(x), np.min(y))
        (bottomx, bottomy) = (np.max(x), np.max(y))
        Cropped = gray[topx:bottomx+1, topy:bottomy+1]

        # Read the number plate
        text = pytesseract.image_to_string(Cropped, config='--psm 11')
        print("Detected Number is:", text)

        # Attendre 1 seconde avant la prochaine capture
        time.sleep(1)

except KeyboardInterrupt:
    print("\nArrêt de la capture demandé par l'utilisateur.")

finally:
    picam2.stop()
    print("Caméra arrêtée.")
