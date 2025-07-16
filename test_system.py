#!/usr/bin/env python3
"""Script de test pour vérifier les imports et la configuration."""

import sys
import os

# Ajouter le dossier src au path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

def test_imports():
    """Test les imports des modules."""
    print("🔍 Test des imports...")
    
    try:
        from config import CAMERA_SIZE, LOOP_DELAY
        print("✅ config.py - OK")
        print(f"   CAMERA_SIZE: {CAMERA_SIZE}")
        print(f"   LOOP_DELAY: {LOOP_DELAY}")
    except ImportError as e:
        print(f"❌ config.py - ERREUR: {e}")
        return False
    
    try:
        from camera_manager import CameraManager
        print("✅ camera_manager.py - OK")
    except ImportError as e:
        print(f"❌ camera_manager.py - ERREUR: {e}")
        print("   Vérifiez que python3-picamera2 est installé")
    
    try:
        from plate_detector import PlateDetector
        print("✅ plate_detector.py - OK")
    except ImportError as e:
        print(f"❌ plate_detector.py - ERREUR: {e}")
        print("   Vérifiez que python3-opencv et python3-numpy sont installés")
    
    try:
        from ocr_processor import OCRProcessor
        print("✅ ocr_processor.py - OK")
    except ImportError as e:
        print(f"❌ ocr_processor.py - ERREUR: {e}")
        print("   Vérifiez que python3-opencv est installé")
    
    try:
        from license_plate_detector import LicensePlateDetector
        print("✅ license_plate_detector.py - OK")
    except ImportError as e:
        print(f"❌ license_plate_detector.py - ERREUR: {e}")
    
    return True

def test_system_dependencies():
    """Test les dépendances système."""
    print("\n🔍 Test des dépendances système...")
    
    import subprocess
    
    # Test Tesseract
    try:
        result = subprocess.run(['tesseract', '--version'], 
                              capture_output=True, text=True)
        print("✅ tesseract-ocr - OK")
    except FileNotFoundError:
        print("❌ tesseract-ocr - NON INSTALLÉ")
        print("   Installez avec: sudo apt-get install -y tesseract-ocr")
    
    # Test caméra (si disponible)
    try:
        result = subprocess.run(['vcgencmd', 'get_camera'], 
                              capture_output=True, text=True)
        if 'detected=1' in result.stdout:
            print("✅ Caméra Pi - DÉTECTÉE")
        else:
            print("⚠️  Caméra Pi - NON DÉTECTÉE")
    except FileNotFoundError:
        print("ℹ️  Commande vcgencmd non disponible (normal si pas sur Pi)")

if __name__ == "__main__":
    print("🚀 Test du système de détection de plaques\n")
    test_imports()
    test_system_dependencies()
    print("\n✅ Test terminé!")
