# Importar as bibliotecas

import cv2
import mediapipe as mp

def main():
    # Captura do video pelo webcam
    cap = cv2.VideoCapture(0)

    # Realizar a captura
    while True:
        # Obter a imagem
        _,imagem = cap.read()

        # Inverter a imagem
        imagem = cv2.flip(imagem, 1)

        # Mostrar a imagem de captura
        cv2.imshow('Handing Tracking', imagem)

        # Tempo de atualização da captura
        cv2.waitKey(1)

if __name__ == '__main__':
    main()