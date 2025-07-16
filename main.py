#!/usr/bin/env python3
"""Point d'entrée principal pour le système de détection de plaques d'immatriculation."""

import sys
import os

# Ajouter le dossier src au path Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from license_plate_detector import LicensePlateDetector


def main():
    """Fonction principale."""
    detector = LicensePlateDetector()
    detector.run()


if __name__ == "__main__":
    main()
