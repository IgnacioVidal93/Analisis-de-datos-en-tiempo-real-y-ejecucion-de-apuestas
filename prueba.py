from pynput.mouse import Button, Controller
from selenium import webdriver
from time import sleep
driver = webdriver.Chrome('./chromedriver.exe')


driver.get('https://es.tradingview.com/symbols/AUDUSD/technicals/')
driver.set_window_size(1380, 450)
driver.set_window_position(0, 0)
sleep(1)
mouse = Controller()

mouse.position = (1360, 300)
sleep(0.5)
mouse.click(Button.left, 1)
sleep(0.5)
mouse.click(Button.left, 1)
sleep(0.5)
mouse.position = (1360, 430)
sleep(0.5)
mouse.click(Button.left, 1)
sleep(0.5)
mouse.click(Button.left, 1)
sleep(0.5)
mouse.position = (350, 220)
sleep(0.5)
mouse.click(Button.left, 1)
sleep(0.5)


#Prueba IQ
mouse.position = (650, 480)
sleep(0.5)
mouse.click(Button.left, 1)
sleep(0.5)
#ABRE RELOJ
mouse.position = (1330, 355)
sleep(0.5)
mouse.click(Button.left, 1)
sleep(0.5)

#CUANDO ESTA AABAJO
#2MINUTOS
mouse.position = (1084, 466)
sleep(1.5)
#3MINUTOS
mouse.position = (1084, 488)
sleep(1.5)
#4MINUTOS
mouse.position = (1084, 520)
sleep(1.5)
#5MINUTOS
mouse.position = (1084, 540)
mouse.click(Button.left, 1)
sleep(1.5)





#CUANDO ESTA AARRIBA
#2MINUTOS
#mouse.position = (1084, 448)
#sleep(1.5)
#3MINUTOS
#mouse.position = (1084, 467)
#sleep(1.5)
#4MINUTOS
#mouse.position = (1084, 489)
#sleep(1.5)
#5MINUTOS
#mouse.position = (1084, 512)
#mouse.click(Button.left, 1)
#sleep(1.5)



#APUESTA SUBE
#mouse.position = (1311, 601)
#APUESTA BAJA
mouse.position = (1314, 672)
sleep(0.5)
mouse.click(Button.left, 1)
sleep(0.5)
