"""Processeur OCR utilisant Tesseract pour la reconnaissance de texte."""

import os
import subprocess
import cv2
from .config import TEMP_IMAGE_PATH, TESSERACT_PSM, TESSERACT_LANG


class OCRProcessor:
    """Processeur OCR pour la reconnaissance de texte sur les plaques."""
    
    def __init__(self):
        self.temp_image_path = TEMP_IMAGE_PATH
        
    def save_plate_image(self, plate_image):
        """Sauvegarde l'image de la plaque temporairement."""
        cv2.imwrite(self.temp_image_path, plate_image)
    
    def run_tesseract(self):
        """Exécute Tesseract OCR sur l'image temporaire."""
        try:
            result = subprocess.run(
                ['tesseract', self.temp_image_path, 'stdout',
                 '--psm', TESSERACT_PSM, '-l', TESSERACT_LANG],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except (subprocess.CalledProcessError, FileNotFoundError):
            # Ignore les erreurs si tesseract ne trouve rien ou n'est pas installé
            return None
    
    def cleanup_temp_file(self):
        """Supprime le fichier temporaire."""
        if os.path.exists(self.temp_image_path):
            os.remove(self.temp_image_path)
    
    def process_plate_image(self, plate_image):
        """Traite l'image de la plaque et retourne le texte reconnu."""
        if plate_image is None:
            return None
            
        self.save_plate_image(plate_image)
        text = self.run_tesseract()
        
        # Nettoyer les espaces et retourner le texte s'il n'est pas vide
        if text:
            return text.strip()
        return None
    
    def __del__(self):
        """Nettoyage automatique du fichier temporaire."""
        self.cleanup_temp_file()
