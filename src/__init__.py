"""Package de détection de plaques d'immatriculation pour Raspberry Pi."""

__version__ = "1.0.0"
__author__ = "Assistant"
__description__ = "Système de détection de plaques d'immatriculation utilisant OpenCV et Tesseract"

from .license_plate_detector import LicensePlateDetector
from .camera_manager import CameraManager
from .plate_detector import PlateDetector
from .ocr_processor import OCRProcessor

__all__ = [
    'LicensePlateDetector',
    'CameraManager', 
    'PlateDetector',
    'OCRProcessor'
]
