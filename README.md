# Hand Tracking 🖐️

Projeto de rastreamento e detecção de mãos em tempo real utilizando **Python**, **OpenCV** e **MediaPipe**.

O objetivo é detectar mãos através da webcam, identificar seus pontos de referência (*landmarks*) e obter suas coordenadas para possibilitar o desenvolvimento de aplicações baseadas em reconhecimento de gestos.

## 🚀 Tecnologias utilizadas

- **Python** – Linguagem de programação.
- **OpenCV** – Captura e processamento de imagens em tempo real.
- **MediaPipe** – Detecção e rastreamento de mãos.

## ✨ Funcionalidades

- Captura de vídeo em tempo real através da webcam.
- Detecção de até duas mãos simultaneamente.
- Identificação dos 21 pontos de referência (*landmarks*) de cada mão.
- Desenho dos pontos e das conexões entre eles.
- Conversão das coordenadas proporcionais para coordenadas em pixels.
- Personalização das cores dos pontos e das conexões.
- Seleção de pontos específicos para destaque na imagem.
- Configuração dos níveis de confiança da detecção e do rastreamento.

## 📁 Estrutura do projeto

```text
projeto_hand_tracking/
│
├── handing_tracking.py
├── README.md
└── venv/
```

## ⚙️ Instalação

### 1. Clone o repositório

```bash
git clone <URL_DO_REPOSITORIO>
```

### 2. Acesse a pasta do projeto

```bash
cd projeto_hand_tracking
```

### 3. Crie um ambiente virtual

```bash
python -m venv venv
```

### 4. Ative o ambiente virtual

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate
```

### 5. Instale as dependências

```bash
pip install opencv-python mediapipe
```

## ▶️ Como executar

Com o ambiente virtual ativado, execute:

```bash
python handing_tracking.py
```

A webcam será inicializada e o sistema começará a detectar as mãos, desenhando os pontos de referência e suas conexões em tempo real.

Para encerrar a execução, pressione a tecla **ESC**.

## 🖐️ Pontos de referência (Landmarks)

O MediaPipe identifica 21 pontos em cada mão, permitindo obter informações sobre a posição dos dedos e da palma.

| Identificação | Ponto |
|---|---|
| 0 | Pulso |
| 1–4 | Polegar |
| 5–8 | Indicador |
| 9–12 | Médio |
| 13–16 | Anelar |
| 17–20 | Mínimo |

As coordenadas dos pontos são convertidas de valores proporcionais para pixels, permitindo localizar cada ponto na imagem capturada.

## 🔧 Personalização

A classe `Detector` permite personalizar os parâmetros de detecção:

```python
detector = Detector(
    modo=False,
    max_maos=2,
    deteccao_confianca=0.5,
    rastreia_confianca=0.5,
    cor_pontos=(0, 0, 255),
    cor_conexoes=(255, 255, 255)
)
```

Também é possível selecionar um ponto específico para destaque:

```python
lista_pontos = detector.encontrar_pontos(
    imagem=imagem,
    ponto_detectado=8
)
```

Nesse exemplo, o ponto 8 representa a ponta do dedo indicador.

## 📌 Objetivo do projeto

Este projeto faz parte dos estudos de processamento de imagens e visão computacional, explorando técnicas de detecção e rastreamento de mãos.

A estrutura desenvolvida também serve como base para futuras implementações, como:

- Reconhecimento de gestos com as mãos.
- Identificação de dedos levantados.
- Controle de aplicações por gestos.
- Interação com interfaces utilizando movimentos das mãos.

## 👨‍💻 Autor

Desenvolvido como projeto de estudos em **Python, OpenCV, MediaPipe e Visão Computacional**.
