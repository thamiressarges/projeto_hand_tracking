
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

    def encontrar_pontos(self, imagem, mao_num=0, desenho=True, cor=(255,0,255), raio=7, ponto_detectado=0):
        """
        Função responsável por encontrar a posição dos pontos da(s) mão(s).
        :param imagem: Imagem capturada.
        :param mao_num: Número da mão detectada.
        :param desenho: Desenhar o ponto encontrado.
        :param cor: Tupla com a cor do ponto (BGR).
        :param raio: Raio do círculo do ponto.
        :param ponto_detectado: Ponto a ser detectado
        :return: Lista com os pontos detectados.
        """

        # Lista com os pontos detectados
        lista_pontos = []

        # Verificar se alguma não foi detectada
        if self.resultado.multi_hand_landmarks:
            # Obter os pontos da mão detectada, não de todas
            mao = self.resultado.multi_hand_landmarks[mao_num]

            # Obter as informações dos pontos
            for id, ponto in enumerate(mao.landmark):
                # Obter as dimensões da imagem capturada
                altura, largura, _ = imagem.shape

                # Transformar a posição do ponto de proporção para pixel
                centro_x, centro_y = int(ponto.x * largura), int(ponto.y * altura)

                # Adicionar os pontos da maõ detectada na lista
                lista_pontos.append([id, centro_x, centro_y])

                # Colocar um circulo em um ponto
                if desenho:
                    if id == ponto_detectado:
                        cv2.circle(
                            imagem, # Imagem da captura
                            (centro_x, centro_y), # Centro do círculo,
                            raio, # raio do circulo
                            cor, # cor do circulo
                            cv2.FILLED # espessura
                        )
            
            return lista_pontos


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

        # Lista com os pontos
        lista_pontos = detector.encontrar_pontos(imagem=imagem, ponto_detectado=8)

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
