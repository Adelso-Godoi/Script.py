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
pyautogui.write("https://ti.cloudti.tech", interval=0.1)
time.sleep(1)
pyautogui.press("enter")

# Aguarda um pouco
time.sleep(2)
#print(pyautogui.position())
# pyautogui.click(x=2425, y=477)
pyautogui.click(2425, 477)
pyautogui.click(3401, 210)
time.sleep(4)
pyautogui.click(2845, 397)
time.sleep(3)
#print(pyautogui.position())

# Fecha o Bloco de Notas
#pyautogui.hotkey("alt", "f4")