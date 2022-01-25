from pynput.mouse import Button, Controller
from selenium import webdriver
import pandas
from time import sleep
import random
import time

def DatosIn1():

    tabla= pandas.read_csv("Tabla5m.csv")

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


    contador3 = 0
    while contador3 < 5:
        contador3 += 1

        mouse = Controller()


        mouse.position = (350, 226)
        mouse.click(Button.left, 1)

        sleep(random.randint(12, 18))

        hora = time.strftime("%H.%M.%S")

        # GENERAL

        precio = float(
            driver.find_element_by_xpath('.//div[@class="tv-symbol-price-quote__value js-symbol-last"]').text)

        # OSILADORES

        RSI = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]').text
        RSI = RSI.replace('−', '-')
        RSI = float(RSI)
        Estocastico = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[3]/td[2]').text
        Estocastico = Estocastico.replace('−', '-')
        Estocastico = float(Estocastico)
        MACD = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[2]').text
        MACD = MACD.replace('−', '-')
        MACD = float(MACD)

        ICPB = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[4]/td[2]').text
        ICPB = ICPB.replace('−', '-')
        ICPB = float(ICPB)
        IMDM = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[2]').text
        IMDM = IMDM.replace('−', '-')
        IMDM = float(IMDM)
        OA = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[6]/td[2]').text
        OA = OA.replace('−', '-')
        OA = float(OA)

        RSIR = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[9]/td[2]').text
        RSIR = RSIR.replace('−', '-')
        RSIR = float(RSIR)
        Williams = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[10]/td[2]').text
        Williams = Williams.replace('−', '-')
        Williams = float(Williams)

        OU = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[12]/td[2]').text
        OU = OU.replace('−', '-')
        OU = float(OU)

        volumen = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[3]/div[3]/div[1]').text
        volumen = volumen.replace('K', '')
        volumen = float(volumen)

        Datos5m = {'1': precio, '2': ['-'], '3': RSI, '4': ['-'], '5': Estocastico, '6': ['-'], '7': MACD, '8': ['-'],'9': IMDM, '10': ['-'], '11': ICPB, '12': ['-'], '13': OA, '14': ['-'],'15': RSIR, '16': ['-'], '17': Williams, '18': ['-'], '19': OA, '20': ['-'],
                   '21': hora, '22': volumen, '23':['-']}
        tabla = tabla.append(Datos5m, ignore_index=True)

        # ACTUALIZO LA PAGINA

        driver.refresh()

        sleep(random.randint(12, 18))

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\Tabla5m.csv', index=False, header=True)
    tabla1 = tabla.drop([1, 2, 3, 4], axis=0)



    contador = 0


    while contador < 155:
        contador += 1

        mouse = Controller()


        sleep(1)

        mouse.position = (350, 226)
        mouse.click(Button.left, 1)

        sleep(random.randint(12, 18))

        hora = time.strftime("%H.%M.%S")

        # GENERAL

        precio = float(
            driver.find_element_by_xpath('.//div[@class="tv-symbol-price-quote__value js-symbol-last"]').text)

        # OSILADORES
        RSI = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[2]/td[2]').text
        RSI = RSI.replace('−', '-')
        RSI = float(RSI)

        Estocastico = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[3]/td[2]').text
        Estocastico = Estocastico.replace('−', '-')
        Estocastico = float(Estocastico)
        MACD = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[2]').text
        MACD = MACD.replace('−', '-')
        MACD = float(MACD)

        ICPB = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[4]/td[2]').text
        ICPB = ICPB.replace('−', '-')
        ICPB = float(ICPB)
        IMDM = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[2]').text
        IMDM = IMDM.replace('−', '-')
        IMDM = float(IMDM)
        OA = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[6]/td[2]').text
        OA = OA.replace('−', '-')
        OA = float(OA)

        RSIR = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[9]/td[2]').text
        RSIR = RSIR.replace('−', '-')
        RSIR = float(RSIR)
        Williams = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[10]/td[2]').text
        Williams = Williams.replace('−', '-')
        Williams = float(Williams)

        OU = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[12]/td[2]').text
        OU = OU.replace('−', '-')
        OU = float(OU)

        volumen = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[3]/div[3]/div[1]').text
        volumen = volumen.replace('K', '')
        volumen = float(volumen)

        volumenV = float(tabla1.iloc[-1, 21])
        volumenN = volumen
        volumenP = float((volumenN - volumenV) / 0.1)


        RSIV = float(tabla1.iloc[-1, 2])
        RSIN = RSI
        RSIP = float((RSIN - RSIV) / 0.1)

        EstocasticoV = float(tabla1.iloc[-1, 4])
        EstocasticoN = Estocastico
        EstocasticoP = float((EstocasticoN - EstocasticoV) / 0.1)

        MACDV = float(tabla1.iloc[-1, 6])
        MACDN = MACD
        MACDP = float((MACDN - MACDV) / 0.1)

        IMDMV = float(tabla1.iloc[-1, 8])
        IMDMN = IMDM
        IMDMP = float((IMDMN - IMDMV) / 0.1)

        ICPBV = float(tabla1.iloc[-1, 10])
        ICPBN = ICPB
        ICPBP = float((ICPBN - ICPBV) / 0.1)

        OAV = float(tabla1.iloc[-1, 12])
        OAN = OA
        OAP = float((OAN - OAV) / 0.1)

        RSIRV = float(tabla1.iloc[-1, 14])
        RSIRN = RSIR
        RSIRP = float((RSIRN - RSIRV) / 0.1)

        WilliamsV = float(tabla1.iloc[-1, 16])
        WilliamsN = Williams
        WilliamsP = float((WilliamsN - WilliamsV) / 0.1)

        OUV = float(tabla1.iloc[-1, 18])
        OUN =OU
        OUP = float((OUN - OUV) / 0.1)



        Datos5m = {'1': precio, '2': ['-'], '3': RSI, '4': RSIP, '5': Estocastico, '6': EstocasticoP, '7': MACD,
                   '8': MACDP, '9': IMDM, '10': IMDMP, '11': ICPB, '12': ICPBP, '13': OA,
                   '14': OAP, '15': RSIR, '16': RSIRP, '17': Williams, '18': WilliamsP, '19': OU,
                   '20': OUP, '21': hora, '22':volumen,'23':volumenP}

        tabla1 = tabla1.append(Datos5m, ignore_index=True)

        # ACTUALIZO LA PAGINA

        driver.refresh()

        sleep(random.randint(12, 18))


    tabla2 = tabla1.drop([1, 2, 3, 4,5,6,7,8], axis=0)
    tabla2.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\Tabla5m.csv', index=False, header=True)

    return


