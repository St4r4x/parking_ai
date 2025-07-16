# Détection de Plaques d'Immatriculation sur Raspberry Pi

Ce projet utilise un Raspberry Pi et une caméra Pi pour détecter et reconnaître en temps réel les plaques d'immatriculation. Le système fonctionne en mode headless et affiche les numéros détectés dans le terminal.

## Structure du Projet

```text
parking_ai/
├── main.py                          # Point d'entrée principal
├── install.sh                       # Script d'installation automatique
├── test_system.py                   # Script de test des dépendances
├── README.md                        # Documentation
└── src/                             # Code source modulaire
    ├── __init__.py                  # Package initialization
    ├── license_plate_detector.py    # Orchestrateur principal
    ├── camera_manager.py            # Gestion de la caméra
    ├── plate_detector.py            # Détection de plaques
    ├── ocr_processor.py             # Traitement OCR
    └── config.py                    # Configuration des paramètres
```

## Matériel Requis

- Raspberry Pi 3B+ (ou modèle supérieur)
- Caméra pour Raspberry Pi (Pi Camera)
- Alimentation stable pour le Raspberry Pi

## Installation

### Installation automatique (recommandée)

Utilisez le script d'installation fourni :

```bash
chmod +x install.sh
./install.sh
```

### Installation manuelle

Si vous préférez installer manuellement les dépendances :

```bash
# Mettre à jour le système
sudo apt-get update

# Installer les dépendances système
sudo apt-get install -y python3-pip python3-opencv python3-numpy tesseract-ocr tesseract-ocr-fra

# Installer picamera2 pour Raspberry Pi
sudo apt-get install -y python3-picamera2
```

## Utilisation

### Test du système

Avant de lancer le programme principal, vous pouvez tester que tout fonctionne :

```bash
python3 test_system.py
```

### Lancement du programme

```bash
python3 main.py
```

Le programme démarrera et affichera `Démarrage de la détection en arrière-plan...`.

Pour arrêter le script, appuyez sur `Ctrl+C`.

## Fonctionnement

Le processus de détection se déroule en plusieurs étapes pour chaque image capturée par la caméra :

1. **Capture d'image** : Une image est capturée depuis la caméra Pi
2. **Prétraitement** : L'image est convertie en niveaux de gris et filtrée pour réduire le bruit
3. **Détection des contours** : L'algorithme de Canny trouve les contours dans l'image
4. **Localisation de la plaque** : Recherche de contours rectangulaires ressemblant à une plaque
5. **Extraction de la plaque** : La plaque potentielle est recadrée du reste de l'image
6. **Reconnaissance OCR** : Tesseract lit les caractères de la plaque
7. **Affichage** : Le texte reconnu est affiché dans le terminal

## Configuration

Les paramètres peuvent être modifiés dans `src/config.py` :

- `CAMERA_SIZE` : Taille de l'image de la caméra (par défaut 1024x576)
- `CANNY_LOW_THRESHOLD` / `CANNY_HIGH_THRESHOLD` : Seuils de détection des contours
- `TESSERACT_PSM` : Mode de segmentation de page pour Tesseract
- `TESSERACT_LANG` : Langue de reconnaissance (par défaut 'eng')
- `LOOP_DELAY` : Délai entre chaque capture (par défaut 0.1 secondes)

## Dépannage

### Erreurs communes

- **ImportError: attempted relative import with no known parent package**
  - Solution : Les imports ont été corrigés pour utiliser des imports absolus
- **ModuleNotFoundError: No module named 'picamera2'**
  - Solution : Installez avec `sudo apt-get install -y python3-picamera2`
- **ModuleNotFoundError: No module named 'cv2'**
  - Solution : Installez avec `sudo apt-get install -y python3-opencv`
- **Erreur de caméra** : Assurez-vous que la caméra Pi est bien connectée et activée
  - Vérifiez avec `vcgencmd get_camera`
- **Tesseract non trouvé** : Vérifiez que `tesseract-ocr` est installé
  - Testez avec `tesseract --version`
- **Performances lentes** : Augmentez `LOOP_DELAY` dans la configuration
- **Détection imprécise** : Ajustez les seuils dans `config.py`

### Prérequis système

Assurez-vous que votre Raspberry Pi est configuré correctement :

```bash
# Activer la caméra (si nécessaire)
sudo raspi-config
# Interface Options > Camera > Enable

# Redémarrer après activation
sudo reboot
```
