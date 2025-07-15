# Détection de Plaques d'Immatriculation sur Raspberry Pi

Ce projet utilise un Raspberry Pi 3B+ et une caméra Pi pour détecter et reconnaître en temps réel les plaques d'immatriculation à partir d'un flux vidéo. Le script est conçu pour fonctionner sans interface graphique (headless), en affichant les numéros de plaque détectés directement dans le terminal.

## Matériel Requis

- Raspberry Pi 3B+ (ou modèle supérieur)
- Caméra pour Raspberry Pi (Pi Camera)
- Une alimentation stable pour le Raspberry Pi

## Installation

Suivez ces étapes pour configurer votre Raspberry Pi.

### 1. Mettre à jour le système

Assurez-vous que votre système d'exploitation est à jour :

```bash
sudo apt-get update
sudo apt-get upgrade
```

### 2. Installer les dépendances système

Ce projet repose sur **OpenCV** pour le traitement d'image et **Tesseract OCR** pour la reconnaissance de caractères. Installez-les avec les commandes suivantes :

```bash

# Installer la bibliothèque Picamera2
sudo apt-get install -y python3-picamera2

# Installer OpenCV pour Python 3
sudo apt install python3-opencv

# Installer le moteur Tesseract OCR
sudo apt-get install tesseract-ocr
```

## Utilisation

Une fois l'installation terminée, vous pouvez lancer le script de détection.

```bash
python main.py
```

Le script démarrera et affichera le message `Démarrage de la détection en arrière-plan...`. Lorsqu'une plaque d'immatriculation est détectée et reconnue, le numéro s'affichera dans le terminal.

Pour arrêter le script, appuyez sur `Ctrl+C`.

## Fonctionnement

Le processus de détection se déroule en plusieurs étapes pour chaque image capturée par la caméra :

1.  **Capture d'image** : Une image est capturée depuis la caméra Pi.
2.  **Prétraitement** : L'image est convertie en niveaux de gris et un filtre est appliqué pour réduire le bruit.
3.  **Détection des contours** : L'algorithme de Canny est utilisé pour trouver les contours dans l'image.
4.  **Localisation de la plaque** : Le script recherche des contours rectangulaires qui ressemblent à une plaque d'immatriculation.
5.  **Extraction de la plaque** : Si une plaque potentielle est trouvée, elle est recadrée du reste de l'image.
6.  **Reconnaissance de caractères (OCR)** : L'image de la plaque est envoyée à Tesseract, qui tente de lire les caractères.
7.  **Affichage** : Le texte reconnu est affiché dans le terminal.
