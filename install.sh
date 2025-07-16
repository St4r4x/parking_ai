#!/bin/bash
# Script d'installation pour le système de détection de plaques

echo "Installation du système de détection de plaques d'immatriculation..."

# Mise à jour du système
echo "Mise à jour du système..."
sudo apt-get update

# Installation des dépendances système
echo "Installation des dépendances système..."
sudo apt-get install -y python3-pip python3-opencv python3-numpy tesseract-ocr tesseract-ocr-fra

# Installation de picamera2 pour Raspberry Pi
echo "Installation de picamera2..."
sudo apt-get install -y python3-picamera2

echo "Installation terminée!"
echo "Pour utiliser le système:"
echo "Lancez le programme: python3 main.py"
