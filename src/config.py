"""Configuration des paramètres du système de détection de plaques."""

# Configuration de la caméra
CAMERA_SIZE = (1024, 576)
CAMERA_WARMUP_TIME = 2  # secondes

# Configuration de l'OCR
TEMP_IMAGE_PATH = "/tmp/plate.png"
TESSERACT_PSM = "11"  # Page segmentation mode
TESSERACT_LANG = "eng"  # Langue

# Configuration du traitement d'image
BILATERAL_FILTER_D = 11
BILATERAL_FILTER_SIGMA_COLOR = 17
BILATERAL_FILTER_SIGMA_SPACE = 17
CANNY_LOW_THRESHOLD = 30
CANNY_HIGH_THRESHOLD = 200
APPROX_EPSILON_FACTOR = 0.018
MAX_CONTOURS = 10

# Configuration du système
LOOP_DELAY = 0.1  # secondes entre chaque itération
