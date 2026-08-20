import subprocess
import pyautogui
import time

# Abre o Bloco de Notas

subprocess.Popen([
    "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "https://www.google.com"
])
 #Aguarda abrir
time.sleep(2)
pyautogui.hotkey("ctrl", "l")
# Digita o texto


time.sleep(2)
pyautogui.write("https://dontpad.com/adelso", interval=0.1)
pyautogui.press("enter")

pyautogui.write("Esse é um teste de automação na tela!")
# Aguarda um pouco
time.sleep(3)

#pyautogui.click(x=2425, y=477)
#   pyautogui.click(x=2425, y=477)
#pyautogui.click(3401, 210)
#time.sleep(4)
#pyautogui.click(2845, 397)
#time.sleep(3)
#print(pyautogui.position())

# Fecha o Bloco de Notas
#pyautogui.hotkey("alt", "f4")