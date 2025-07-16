"""Gestionnaire de caméra pour la capture d'images."""

import time
from picamera2 import Picamera2
from config import CAMERA_SIZE, CAMERA_WARMUP_TIME


class CameraManager:
    """Gestionnaire de la caméra Raspberry Pi."""
    
    def __init__(self):
        self.picam2 = Picamera2()
        self.is_started = False
        
    def start(self):
        """Démarre la caméra avec la configuration appropriée."""
        if not self.is_started:
            camera_config = self.picam2.create_still_configuration(
                main={"size": CAMERA_SIZE}
            )
            self.picam2.configure(camera_config)
            self.picam2.start()
            
            # Laisser le temps à la caméra de s'ajuster à la lumière
            time.sleep(CAMERA_WARMUP_TIME)
            self.is_started = True
            
    def capture_array(self):
        """Capture une image sous forme de tableau NumPy."""
        if not self.is_started:
            raise RuntimeError("La caméra n'est pas démarrée")
        return self.picam2.capture_array()
    
    def stop(self):
        """Arrête la caméra."""
        if self.is_started:
            self.picam2.stop()
            self.is_started = False
            
    def __enter__(self):
        """Support du context manager."""
        self.start()
        return self
        
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Support du context manager."""
        self.stop()
