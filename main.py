import cv2
import mediapipe as mp
import numpy as np

# Configuração Padrão do MediaPipe
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_desenho = mp.solutions.drawing_utils

# Variáveis do Exercício
contador = 0
estado = None

def calcular_angulo(a, b, c):
    a = np.array(a) # Ombro
    b = np.array(b) # Cotovelo
    c = np.array(c) # Pulso
    radianos = np.arctan2(c[1]-b[1], c[0]-b[0]) - np.arctan2(a[1]-b[1], a[0]-b[0])
    angulo = np.abs(radianos*180.0/np.pi)
    if angulo > 180.0:
        angulo = 360 - angulo
    return angulo

cap = cv2.VideoCapture(0)

while cap.isOpened():
    sucesso, frame = cap.read()
    if not sucesso:
        break
        
    imagem_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    resultado = pose.process(imagem_rgb)
    
    if resultado.pose_landmarks:
        mp_desenho.draw_landmarks(frame, resultado.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        
        try:
            landmarks = resultado.pose_landmarks.landmark
            
            # MUDANÇA: Coordenadas alteradas para o braço DIREITO (RIGHT)
            ombro = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            cotovelo = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            pulso = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x, landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            angulo = calcular_angulo(ombro, cotovelo, pulso)
            
            # Lógica de Fisioterapia: Contar repetições
            if angulo > 85:
                estado = "cima"
            if angulo < 30 and estado == "cima":
                estado = "baixo"
                contador += 1
            
            # Mostrar os dados na tela
            cv2.putText(frame, f'Angulo: {int(angulo)}', (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            cv2.putText(frame, f'Repeticoes: {contador}', (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
        except:
            pass

    cv2.imshow('Reabilitacao AVC', frame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()