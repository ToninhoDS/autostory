import pyautogui
import time

def automate_task():
    # Função para clicar no ponto X
    def click_at_x():
        pyautogui.click()  # Clica no ponto X
        time.sleep(0.5)
        pyautogui.click()  # Segunda vez no ponto X
        time.sleep(0.5)

    # Função para mover e aplicar as combinações de teclas
    def move_and_click():
        # Movimento do boneco de 0 até X (representado por setas para a direita)
        pyautogui.press('right', presses=10, interval=0.1)  # Ajuste o número de pressões e intervalo conforme necessário

        for _ in range(3):  # Faça isso 3 vezes
            pyautogui.press('space')  # Pular
            time.sleep(0.5)
            pyautogui.press('space')  # Segunda vez de pular
            click_at_x()  # Clicar no X

        # Pressionar Ctrl, depois End e Del
        pyautogui.hotkey('ctrl')
        time.sleep(0.5)
        pyautogui.press('end')
        time.sleep(0.5)
        pyautogui.press('del')

        # Movimento de volta para o ponto 0 (representado por setas para a esquerda)
        pyautogui.press('left', presses=10, interval=0.1)  # Ajuste o número de pressões e intervalo conforme necessário

        for _ in range(1):  # Apenas uma vez
            pyautogui.press('space')  # Pular
            pyautogui.press('down')  # Setas para baixo

    # Executar a tarefa e repetir a cada 5 minutos
    while True:
        move_and_click()
        time.sleep(300)  # Espera 5 minutos (300 segundos) antes de repetir

if __name__ == "__main__":
    automate_task()
