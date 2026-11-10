# 🏥 Reabilitação Pós-AVC: Rastreamento de Exercícios com Visão Computacional

**Submissão para:** Inteligência Artificial para a Medicina: Uma Maratona Global de Hackathon Estudantil sobre o Futuro da Saúde

## 📌 Visão Geral do Projeto
Este projeto utiliza Inteligência Artificial e Visão Computacional (MediaPipe e OpenCV) para automatizar o rastreamento e a contagem de exercícios físicos na reabilitação de pacientes pós-Acidente Vascular Cerebral (AVC). 
O sistema monitoriza os ângulos articulares em tempo real através de uma webcam padrão, promovendo a adesão ao tratamento em casa e fornecendo feedback visual imediato sem necessidade de hardware dispendioso.

## ✨ Funcionalidades
* **Rastreamento Biomecânico em Tempo Real:** Deteção de pontos de articulação (ombro, cotovelo, pulso) utilizando o modelo MediaPipe Pose.
* **Cálculo Geométrico Automático:** Medição contínua da amplitude de movimento (graus de flexão/extensão).
* **Contador de Repetições Inteligente:** Registo automático de repetições com base em limiares clínicos pré-definidos (ex: flexão acima de 85° e extensão abaixo de 30°).
* **Interface Visual Integrada:** Exibição do esqueleto virtual e dados de desempenho sobrepostos no vídeo do paciente.

## 🛠️ Pré-requisitos e Configuração do Ambiente
Para garantir a estabilidade do sistema e evitar conflitos de dependências com a API do MediaPipe, é **estritamente necessário** utilizar as versões exatas listadas abaixo.

* **Linguagem:** Python 3.11 (Não suportado nativamente em Python 3.12 ou 3.13)
* **Bibliotecas Principais:** OpenCV, MediaPipe (v0.10.14) e NumPy.

### Passo a Passo de Instalação para Avaliadores
1. Instale o [Python 3.11](https://www.python.org/downloads/release/python-3119/) e certifique-se de marcar a opção **"Add python.exe to PATH"** na janela inicial do instalador.
2. Clone este repositório e abra a pasta do projeto num terminal.
3. Instale as dependências com as versões específicas executando os comandos:
   ```bash
   pip install opencv-python numpy
   pip install mediapipe==0.10.14
