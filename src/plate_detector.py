"""Détecteur de plaques d'immatriculation utilisant OpenCV."""

import cv2
import numpy as np
from .config import (
    BILATERAL_FILTER_D, BILATERAL_FILTER_SIGMA_COLOR, 
    BILATERAL_FILTER_SIGMA_SPACE, CANNY_LOW_THRESHOLD, 
    CANNY_HIGH_THRESHOLD, APPROX_EPSILON_FACTOR, MAX_CONTOURS
)


class PlateDetector:
    """Détecteur de plaques d'immatriculation."""
    
    def __init__(self):
        pass
    
    def preprocess_image(self, image_array):
        """Prétraite l'image pour la détection de contours."""
        # Convertir en niveaux de gris pour le traitement
        gray = cv2.cvtColor(image_array, cv2.COLOR_RGB2GRAY)
        gray = cv2.bilateralFilter(
            gray, 
            BILATERAL_FILTER_D, 
            BILATERAL_FILTER_SIGMA_COLOR, 
            BILATERAL_FILTER_SIGMA_SPACE
        )
        return gray
    
    def find_plate_contour(self, gray_image):
        """Trouve le contour de la plaque d'immatriculation."""
        # Détection des contours
        edged = cv2.Canny(gray_image, CANNY_LOW_THRESHOLD, CANNY_HIGH_THRESHOLD)
        
        # Remplacement de imutils.grab_contours
        contours_tuple = cv2.findContours(
            edged.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
        )
        cnts = contours_tuple[0] if len(contours_tuple) == 2 else contours_tuple[1]
        
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:MAX_CONTOURS]
        
        # Boucle sur les contours pour trouver un rectangle
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, APPROX_EPSILON_FACTOR * peri, True)
            if len(approx) == 4:
                return approx
        
        return None
    
    def extract_plate_region(self, gray_image, contour):
        """Extrait la région de la plaque à partir du contour."""
        if contour is None:
            return None
            
        # Masquer tout sauf la plaque
        mask = np.zeros(gray_image.shape, np.uint8)
        cv2.drawContours(mask, [contour], 0, 255, -1)
        
        # Extraire la plaque de l'image en niveaux de gris
        (x, y) = np.where(mask == 255)
        if x.size > 0 and y.size > 0:  # S'assurer que la plaque n'est pas vide
            (topx, topy) = (np.min(x), np.min(y))
            (bottomx, bottomy) = (np.max(x), np.max(y))
            cropped = gray_image[topx:bottomx + 1, topy:bottomy + 1]
            return cropped
        
        return None
    
    def detect_plate(self, image_array):
        """Détecte et extrait une plaque d'immatriculation de l'image."""
        gray = self.preprocess_image(image_array)
        contour = self.find_plate_contour(gray)
        
        if contour is not None:
            plate_region = self.extract_plate_region(gray, contour)
            return plate_region
        
        return None
