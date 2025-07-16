"""Module principal pour le système de détection de plaques d'immatriculation."""

import time
from camera_manager import CameraManager
from plate_detector import PlateDetector
from ocr_processor import OCRProcessor
from config import LOOP_DELAY


class LicensePlateDetector:
    """Système principal de détection de plaques d'immatriculation."""
    
    def __init__(self):
        self.camera_manager = CameraManager()
        self.plate_detector = PlateDetector()
        self.ocr_processor = OCRProcessor()
        
    def run(self):
        """Exécute le système de détection en boucle continue."""
        try:
            with self.camera_manager:
                print("Démarrage de la détection en arrière-plan. Appuyez sur Ctrl+C pour arrêter.")
                
                while True:
                    # Capturer l'image
                    image_array = self.camera_manager.capture_array()
                    
                    # Détecter la plaque
                    plate_image = self.plate_detector.detect_plate(image_array)
                    
                    # Si une plaque est détectée, traiter avec OCR
                    if plate_image is not None:
                        text = self.ocr_processor.process_plate_image(plate_image)
                        if text:
                            print(f"Numéro détecté : {text}")
                    
                    # Petite pause pour ne pas surcharger le CPU
                    time.sleep(LOOP_DELAY)
                    
        except KeyboardInterrupt:
            print("\nArrêt de la détection demandé par l'utilisateur.")
        finally:
            self.ocr_processor.cleanup_temp_file()
            print("Caméra arrêtée.")
