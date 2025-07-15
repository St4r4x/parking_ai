import cv2
import sys

def launch_webcam():
    """Lance la webcam et affiche le flux vidéo en temps réel"""
    
    # Initialiser la capture vidéo (0 = webcam par défaut)
    cap = cv2.VideoCapture(0)
    
    # Vérifier si la webcam est accessible
    if not cap.isOpened():
        print("Erreur: Impossible d'accéder à la webcam")
        return False
    
    print("Webcam lancée. Appuyez sur 'q' pour quitter.")
    
    try:
        while True:
            # Capturer une frame
            ret, frame = cap.read()
            
            if not ret:
                print("Erreur: Impossible de lire la frame")
                break
            
            # Afficher la frame
            cv2.imshow('Webcam', frame)
            
            # Quitter si 'q' est pressé
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
                
    except KeyboardInterrupt:
        print("\nArrêt demandé par l'utilisateur")
    
    finally:
        # Libérer les ressources
        cap.release()
        cv2.destroyAllWindows()
        print("Webcam fermée")
    
    return True

if __name__ == "__main__":
    success = launch_webcam()
    if not success:
        sys.exit(1)