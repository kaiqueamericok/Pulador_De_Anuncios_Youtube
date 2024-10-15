<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>README - Script de Automação de Clique</title>
</head>
<body>
    <h1>Automação de Clique no Botão "Pular"</h1>

    <p>Este script foi desenvolvido para automatizar a tarefa de encontrar e clicar em um botão "pular" em uma interface gráfica. O código utiliza a biblioteca <code>PyAutoGUI</code> para realizar a automação e a função <code>locateOnScreen</code> para detectar a presença da imagem do botão na tela.</p>

    <h2>Funcionalidade</h2>
    <ul>
        <li>Localiza a imagem do botão "pular" em uma interface gráfica.</li>
        <li>Clica automaticamente no botão, caso ele seja encontrado.</li>
        <li>Repete o processo indefinidamente até que o programa seja encerrado.</li>
        <li>Inclui pausas de 2 segundos entre os cliques para evitar ações repetidas em um curto intervalo de tempo.</li>
    </ul>

    <h2>Pré-requisitos</h2>
    <p>Certifique-se de que as seguintes bibliotecas Python estejam instaladas no seu ambiente:</p>
    <ul>
        <li><a href="https://pyautogui.readthedocs.io/en/latest/">PyAutoGUI</a> (biblioteca principal para a automação na tela)</li>
        <li><a href="https://docs.opencv.org/">OpenCV</a> (embora não usada diretamente, pode ser útil para trabalhar com imagens)</li>
    </ul>

    <h2>Instalação</h2>
    <pre><code>pip install pyautogui opencv-python</code></pre>

    <h2>Como Usar</h2>
    <p>Siga os passos abaixo para executar o script:</p>
    <ol>
        <li>Capture uma imagem do botão "pular" na interface gráfica que você deseja automatizar.</li>
        <li>Salve a imagem em um diretório local e atualize a variável <code>imagem</code> no código com o caminho correto da imagem.</li>
        <li>Execute o script em seu ambiente Python.</li>
    </ol>

    <h3>Exemplo de Uso:</h3>
    <pre><code>
import pyautogui
import time

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
            print("...")

    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(1)
    </code></pre>

    <h2>Considerações</h2>
    <p>Esse script utiliza um loop infinito para garantir que o botão seja encontrado e clicado sempre que estiver disponível na tela. No entanto, recomenda-se adicionar uma condição de saída ou monitoramento mais avançado caso seja utilizado em cenários mais complexos.</p>

    <h2>Licença</h2>
    <p>Este projeto está licenciado sob a <strong>MIT License</strong>.</p>
</body>
</html>
