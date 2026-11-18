# Importar as bibliotecas
import cv2
import mediapipe as mp

class Detector:
    '''Classe responsável pela detecção das mãos''' 
    def __init__(self,
                modo=False,
                max_maos=2,
                deteccao_confianca=0.5,
                rastreia_confianca=0.5,
                cor_pontos=(0,0,255),
                cor_conexoes=(255,255,255)
            ):
        '''Função responsavel por inicializar a classe
            :param mode: Modo da captura da imagem. Se True, a detecção e o rastreio serão feitos
            a todo momento; deixa muito travado. Se False, não são feitas a detecção e rastreio a todo momento; pode perder 
            por alguns instantes as marcações, porém não trava
            :param max_maos: Quantidade máxima de mãos para serem detectadas
            :param deteccao_confianca: Percentual da taxa de detecção da mão. Se for menor do que este limite,
            a detecção não ocorre
            :param rastreio_confianca: Percentual da taxa de rastreio dos pontos da mão. Se for menor que este
            limite, o rastreio dos pontos não é realizado.
            :param cor_pontos: Cor dos pontos
            :param cor_conexoes: Cor das conexoes
        '''
        # Inicializar os parâmetros
        self.modo = modo
        self.max_maos = max_maos
        self.deteccao_confianca = deteccao_confianca
        self.rastreio_confianca = rastreia_confianca
        self.cor_pontos = cor_pontos
        self.cor_conexoes = cor_conexoes

        # Inicializar os módulos de detecção das mãos
        self.maos_mp = mp.solutions.hands
        self.maos = self.maos_mp.Hands(
            self.modo,
            self.max_maos,
            1,
            self.deteccao_confianca,
            self.rastreio_confianca
        )

        # Função para desenhar os pontos na mãos
        self.desenho_mp = mp.solutions.drawing_utils

        # Configurações do desenho dos pontos
        self.desenho_config_pontos = self.desenho_mp.DrawingSpec(color=self.cor_pontos)

        # Configurações do desenho das conexões
        self.desenho_config_pontos = self.desenho_mp.DrawingSpec(color=self.cor_conexoes)

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