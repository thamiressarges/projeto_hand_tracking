
# Importar as bibliotecas
import cv2
import mediapipe as mp


class Detector:
    '''Classe responsável pela detecção das mãos'''

    def __init__(
        self,
        modo=False,
        max_maos=2,
        deteccao_confianca=0.5,
        rastreia_confianca=0.5,
        cor_pontos=(0, 0, 255),
        cor_conexoes=(255, 255, 255)
    ):
        '''Função responsável por inicializar a classe

        :param modo: Modo da captura da imagem.
        :param max_maos: Quantidade máxima de mãos detectadas.
        :param deteccao_confianca: Confiança mínima da detecção.
        :param rastreia_confianca: Confiança mínima do rastreamento.
        :param cor_pontos: Cor dos pontos.
        :param cor_conexoes: Cor das conexões.
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
            static_image_mode=self.modo,
            max_num_hands=self.max_maos,
            model_complexity=1,
            min_detection_confidence=self.deteccao_confianca,
            min_tracking_confidence=self.rastreio_confianca
        )

        # Função para desenhar os pontos nas mãos
        self.desenho_mp = mp.solutions.drawing_utils

        # Configurações do desenho dos pontos
        self.desenho_config_pontos = self.desenho_mp.DrawingSpec(
            color=self.cor_pontos
        )

        # Configurações do desenho das conexões
        self.desenho_config_conexoes = self.desenho_mp.DrawingSpec(
            color=self.cor_conexoes
        )

    def encontrar_maos(self, imagem, desenho=True):
        '''
        Função responsável por detectar a(s) mão(s).

        :param imagem: Imagem capturada.
        :param desenho: Desenhar os pontos e as conexões nas mãos.
        :return: Imagem com a detecção.
        '''

        # Converter a imagem de BGR para RGB
        imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

        # Passar a imagem convertida para o detector
        self.resultado = self.maos.process(imagem_rgb)

        # Verificar se alguma mão foi detectada
        if self.resultado.multi_hand_landmarks:
            for pontos in self.resultado.multi_hand_landmarks:

                if desenho:
                    # Desenhar os pontos nas mãos detectadas
                    self.desenho_mp.draw_landmarks(
                        imagem,
                        pontos,
                        self.maos_mp.HAND_CONNECTIONS,
                        self.desenho_config_pontos,
                        self.desenho_config_conexoes
                    )

        return imagem

    def fechar(self):
        # Liberar os recursos do MediaPipe
        self.maos.close()


def main():

    # Inicializar o detector
    detector = Detector()

    # Captura do vídeo pela webcam
    cap = cv2.VideoCapture(0)

    # Verificar se a webcam foi inicializada
    if not cap.isOpened():
        print("Erro ao abrir a webcam!")
        detector.fechar()
        return

    # Realizar a captura
    while True:

        # Obter a imagem
        sucesso, imagem = cap.read()

        # Verificar se a captura foi realizada
        if not sucesso:
            print("Erro ao capturar imagem da webcam!")
            break

        # Inverter a imagem
        imagem = cv2.flip(imagem, 1)

        # Detectar as mãos
        imagem = detector.encontrar_maos(imagem)

        # Mostrar a imagem de captura
        cv2.imshow('Handing Tracking', imagem)

        # Finalizar ao pressionar ESC
        if cv2.waitKey(1) & 0xFF == 27:
            break

    # Liberar os recursos
    cap.release()
    detector.fechar()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
