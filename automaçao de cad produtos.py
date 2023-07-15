import pyautogui
from time import sleep

sleep(3)

pyautogui.click(962, 610, duration=0.2)
pyautogui.click(990, 543)
pyautogui.write('admin')
pyautogui.click(982, 578)
pyautogui.write('admin')
pyautogui.click(965, 607, duration=0.2)
pyautogui.click(992, 547)
pyautogui.write('gabriel')
pyautogui.click(1001, 584)
pyautogui.write('123456')
pyautogui.click(836, 610, duration=0.2)


with open('produtos.txt', 'r') as arquivo:
    for linha in arquivo:

        produto = linha.split(',')[0]
        quantidade = linha.split(',')[1]
        preco = linha.split(',')[2]

        pyautogui.click(636,528)
        pyautogui.write(produto)
        pyautogui.click(623,558)
        pyautogui.write(quantidade)
        pyautogui.click(612,597)
        pyautogui.write(preco)
        pyautogui.click(520, 788)

        sleep(1)
