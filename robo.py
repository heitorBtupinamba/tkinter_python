import pyautogui
from time import sleep

pyautogui.click(981,616, duration=2)
pyautogui.write("heitor123")
pyautogui.press("enter")
pyautogui.press("enter")
pyautogui.click(62,44, duration=2)
#ADICIONAR PRODUTOS
with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:
        id_prod = linha.split(',')[0]
        nome = linha.split(',')[1]
        qntd = linha.split(',')[2]
        preco = linha.split(',')[3]

        pyautogui.click(260,84)
        pyautogui.write(id_prod)
        pyautogui.click(226,146, duration=1)
        pyautogui.write(nome)
        pyautogui.click(228,215, duration=1)
        pyautogui.write(qntd)
        pyautogui.click(228,278, duration=1)
        pyautogui.write(preco)
        pyautogui.click(230,322, duration=1)
        pyautogui.press('enter')
