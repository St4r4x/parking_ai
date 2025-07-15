import cv2
import numpy as np
from picamera2 import PiCamera2

picam2 = PiCamera2()

config = picam2.create_preview_configuration(main={"size": (640, 480)})
picam2.configure(config)

picam2.start()

print("Camera started. Press 'q' to quit.")

while True:
    frame = picam2.capture_array()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    cv2.imshow("Camera Feed", gray_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
cv2.destroyAllWindows()
picam2.stop()