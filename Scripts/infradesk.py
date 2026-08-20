import subprocess
import pyautogui    
import time


subprocess.Popen([
    "C:\Program Files\Google\Chrome\Application\chrome.exe",
    "https://www.google.com"
])


time.sleep(2)
pyautogui.hotkey("ctrl", "l")

time.sleep(2)
pyautogui.write("https://infradesk.drugovich.com.br/login", interval=0.1)
time.sleep(1)

pyautogui.press("enter")
time.sleep(2)

pyautogui.click(3761, 715)
pyautogui.write("admin")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("S3rv3rP@nel!")
time.sleep(1)
pyautogui.press("enter")
time.sleep(4)
#botao = pyautogui.locateCenterOnScreen("verifica.jpg")


pyautogui.click(4660, 457)
time.sleep(2)
#botao = pyautogui.locateCenterOnScreen("confirmar.jpg", confidence=0.5)
#print(botao)
#if botao:
#    pyautogui.click(botao)
#if botao:
#    pyautogui.click(botao)

pyautogui.click(3823, 790)
print(pyautogui.position())

