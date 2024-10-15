import pyautogui
import time
import cv2

# Caminho da imagem do botão pular
imagem = 'files/pular.png'

# Loop infinito para verificar a imagem na tela constantemente 
while True:
    try:
         # Tentar encontrar o botão pular na tela
        posicao = pyautogui.locateOnScreen(imagem, confidence=0.8)

    # Se o botão pular for encontrado
        if posicao:
           print(f"Botão encontrado em {posicao}")
        
        # Clique no centro de pular
           pyautogui.click(pyautogui.center(posicao))

        # Pausa para não clicar várias vezes
           time.sleep(2)
        else: 
        # Se o botão não for encontrado, volta para o início do loop
         print("...")
    except pyautogui.ImageNotFoundException:
        print("Imagem não encontrada. Tentando novamente...")
    

        time.sleep(1)