import random
import time
from time import sleep
import numpy
import pandas
from pynput.mouse import Button, Controller
from selenium import webdriver
import requests


def Tiemporeal():

    catidaddehoras=2


    driver = webdriver.Chrome('./chromedriver.exe')

    driver.get('https://es.tradingview.com/symbols/AUDUSD/technicals/')

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


    tabla = pandas.read_csv("Tabla5m.csv")

    tablaC1 = pandas.read_csv("convinaciones1.csv")
    tablaC2 = pandas.read_csv("convinaciones2.csv")
    tablaC3 = pandas.read_csv("convinaciones3.csv")
    tablaRSI = pandas.read_csv("convinacionesRSI.csv")
    tablaRSI1 = pandas.read_csv("convinacionesRSI1.csv")
    tablaEsto = pandas.read_csv("convinacionesEsto.csv")
    tablaEsto1 = pandas.read_csv("convinacionesEsto1.csv")
    tablaMACD = pandas.read_csv("convinacionesMACD.csv")
    tablaMACD1 = pandas.read_csv("convinacionesMACD1.csv")
    tablaIMDM = pandas.read_csv("convinacionesIMDM.csv")
    tablaIMDM1 = pandas.read_csv("convinacionesIMDM1.csv")
    tablaICPB = pandas.read_csv("convinacionesICPB.csv")
    tablaICPB1 = pandas.read_csv("convinacionesICPB1.csv")
    tablaOA = pandas.read_csv("convinacionesOA.csv")
    tablaOA1 = pandas.read_csv("convinacionesOA1.csv")
    tablaRSIR = pandas.read_csv("convinacionesRSIR.csv")
    tablaRSIR1 = pandas.read_csv("convinacionesRSIR1.csv")
    tablaWilliams = pandas.read_csv("convinacionesWilliams.csv")
    tablaWilliams1 = pandas.read_csv("convinacionesWilliams1.csv")
    tablaOU = pandas.read_csv("convinacionesOU.csv")
    tablaOU1 = pandas.read_csv("convinacionesOU1.csv")

    Largo = tabla.shape[0]
    cantidadaanalizar = 120 * catidaddehoras
    fin = Largo - cantidadaanalizar

    # RANGOS
    # RANGO RSI
    if fin < 2:
        maximoRSI = float(numpy.nanmax(tabla.iloc[2:-1, 2].values))
        minimoRSI = float(numpy.nanmin(tabla.iloc[2:-1, 2].values))

    if fin > 2:
        maximoRSI = float(numpy.nanmax(tabla.iloc[fin:-1, 2].values))
        minimoRSI = float(numpy.nanmin(tabla.iloc[fin:-1, 2].values))

    MitadRSI = (maximoRSI + minimoRSI) / 2
    PcuartoRSI = (MitadRSI + minimoRSI) / 2
    TcuartoRSI = (MitadRSI + maximoRSI) / 2
    PoctavoRSI = (minimoRSI + PcuartoRSI) / 2
    ToctavoRSI = (PcuartoRSI + MitadRSI) / 2
    QoctavoRSI = (MitadRSI + TcuartoRSI) / 2
    SoctavoRSI = (TcuartoRSI + maximoRSI) / 2

    # Rango pendiente RSI

    # PARA Pendiente
    if fin < 2:
        maximoRSIPP = float(numpy.nanmax(tabla.iloc[2:-1, 3].values))
        minimoRSIPP = 0
        maximoRSIPN = 0
        minimoRSIPN = float(numpy.nanmin(tabla.iloc[2:-1, 3].values))

    if fin > 2:
        maximoRSIPP = float(numpy.nanmax(tabla.iloc[fin:-1, 3].values))
        minimoRSIPP = 0
        maximoRSIPN = 0
        minimoRSIPN = float(numpy.nanmin(tabla.iloc[fin:-1, 3].values))

    # PARA POSITIVA

    MitadRSIPP = (maximoRSIPP + minimoRSIPP) / 2
    PcuartoRSIPP = (MitadRSIPP + minimoRSIPP) / 2
    TcuartoRSIPP = (MitadRSIPP + maximoRSIPP) / 2
    PoctavoRSIPP = (minimoRSIPP + PcuartoRSIPP) / 2
    ToctavoRSIPP = (PcuartoRSIPP + MitadRSIPP) / 2
    QoctavoRSIPP = (MitadRSIPP + TcuartoRSIPP) / 2
    SoctavoRSIPP = (TcuartoRSIPP + maximoRSIPP) / 2

    # PARA NEGATIVA

    MitadRSIPN = (maximoRSIPN + minimoRSIPN) / 2
    PcuartoRSIPN = (MitadRSIPN + minimoRSIPN) / 2
    TcuartoRSIPN = (MitadRSIPN + maximoRSIPN) / 2
    PoctavoRSIPN = (minimoRSIPN + PcuartoRSIPN) / 2
    ToctavoRSIPN = (PcuartoRSIPN + MitadRSIPN) / 2
    QoctavoRSIPN = (MitadRSIPN + TcuartoRSIPN) / 2
    SoctavoRSIPN = (TcuartoRSIPN + maximoRSIPN) / 2

    # PARA ESTOCASTICO
    if fin < 2:
        maximoESTOCASTICO = float(numpy.nanmax(tabla.iloc[2:-1, 4].values))
        minimoESTOCASTICO = float(numpy.nanmin(tabla.iloc[2:-1, 4].values))
    if fin > 2:
        maximoESTOCASTICO = float(numpy.nanmax(tabla.iloc[fin:-1, 4].values))
        minimoESTOCASTICO = float(numpy.nanmin(tabla.iloc[fin:-1, 4].values))

    MitadESTOCASTICO = (maximoESTOCASTICO + minimoESTOCASTICO) / 2
    PcuartoESTOCASTICO = (MitadESTOCASTICO + minimoESTOCASTICO) / 2
    TcuartoESTOCASTICO = (MitadESTOCASTICO + maximoESTOCASTICO) / 2
    PoctavoESTOCASTICO = (minimoESTOCASTICO + PcuartoESTOCASTICO) / 2
    ToctavoESTOCASTICO = (PcuartoESTOCASTICO + MitadESTOCASTICO) / 2
    QoctavoESTOCASTICO = (MitadESTOCASTICO + TcuartoESTOCASTICO) / 2
    SoctavoESTOCASTICO = (TcuartoESTOCASTICO + maximoESTOCASTICO) / 2

    # Para pendiente
    if fin < 2:
        maximoESTOCASTICOPP = float(numpy.nanmax(tabla.iloc[2:-1, 5].values))
        minimoESTOCASTICOPP = 0
        maximoESTOCASTICOPN = 0
        minimoESTOCASTICOPN = float(numpy.nanmin(tabla.iloc[2:-1, 5].values))
    if fin > 2:
        maximoESTOCASTICOPP = float(numpy.nanmax(tabla.iloc[fin:-1, 5].values))
        minimoESTOCASTICOPP = 0
        maximoESTOCASTICOPN = 0
        minimoESTOCASTICOPN = float(numpy.nanmin(tabla.iloc[fin:-1, 5].values))

    # Para positivo

    MitadESTOCASTICOPP = (maximoESTOCASTICOPP + minimoESTOCASTICOPP) / 2
    PcuartoESTOCASTICOPP = (MitadESTOCASTICOPP + minimoESTOCASTICOPP) / 2
    TcuartoESTOCASTICOPP = (MitadESTOCASTICOPP + maximoESTOCASTICOPP) / 2
    PoctavoESTOCASTICOPP = (minimoESTOCASTICOPP + PcuartoESTOCASTICOPP) / 2
    ToctavoESTOCASTICOPP = (PcuartoESTOCASTICOPP + MitadESTOCASTICOPP) / 2
    QoctavoESTOCASTICOPP = (MitadESTOCASTICOPP + TcuartoESTOCASTICOPP) / 2
    SoctavoESTOCASTICOPP = (TcuartoESTOCASTICOPP + maximoESTOCASTICOPP) / 2

    # Para Negativo

    MitadESTOCASTICOPN = (maximoESTOCASTICOPN + minimoESTOCASTICOPN) / 2
    PcuartoESTOCASTICOPN = (MitadESTOCASTICOPN + minimoESTOCASTICOPN) / 2
    TcuartoESTOCASTICOPN = (MitadESTOCASTICOPN + maximoESTOCASTICOPN) / 2
    PoctavoESTOCASTICOPN = (minimoESTOCASTICOPN + PcuartoESTOCASTICOPN) / 2
    ToctavoESTOCASTICOPN = (PcuartoESTOCASTICOPN + MitadESTOCASTICOPN) / 2
    QoctavoESTOCASTICOPN = (MitadESTOCASTICOPN + TcuartoESTOCASTICOPN) / 2
    SoctavoESTOCASTICOPN = (TcuartoESTOCASTICOPN + maximoESTOCASTICOPN) / 2

    # PARA MACD
    if fin < 2:
        maximoMACD = float(numpy.nanmax(tabla.iloc[2:-1, 6].values))
        minimoMACD = float(numpy.nanmin(tabla.iloc[2:-1, 6].values))
    if fin > 2:
        maximoMACD = float(numpy.nanmax(tabla.iloc[fin:-1, 6].values))
        minimoMACD = float(numpy.nanmin(tabla.iloc[fin:-1, 6].values))

    MitadMACD = (maximoMACD + minimoMACD) / 2
    PcuartoMACD = (MitadMACD + minimoMACD) / 2
    TcuartoMACD = (MitadMACD + maximoMACD) / 2
    PoctavoMACD = (minimoMACD + PcuartoMACD) / 2
    ToctavoMACD = (PcuartoMACD + MitadMACD) / 2
    QoctavoMACD = (MitadMACD + TcuartoMACD) / 2
    SoctavoMACD = (TcuartoMACD + maximoMACD) / 2

    # PARA PENDIENTE
    if fin < 2:
        maximoMACDPP = float(numpy.nanmax(tabla.iloc[2:-1, 7].values))
        minimoMACDPP = 0
        maximoMACDPN = 0
        minimoMACDPN = float(numpy.nanmin(tabla.iloc[2:-1, 7].values))
    if fin > 2:
        maximoMACDPP = float(numpy.nanmax(tabla.iloc[fin:-1, 7].values))
        minimoMACDPP = 0
        maximoMACDPN = 0
        minimoMACDPN = float(numpy.nanmin(tabla.iloc[fin:-1, 7].values))

    # POSITIVA

    MitadMACDPP = (maximoMACDPP + minimoMACDPP) / 2
    PcuartoMACDPP = (MitadMACDPP + minimoMACDPP) / 2
    TcuartoMACDPP = (MitadMACDPP + maximoMACDPP) / 2
    PoctavoMACDPP = (minimoMACDPP + PcuartoMACDPP) / 2
    ToctavoMACDPP = (PcuartoMACDPP + MitadMACDPP) / 2
    QoctavoMACDPP = (MitadMACDPP + TcuartoMACDPP) / 2
    SoctavoMACDPP = (TcuartoMACDPP + maximoMACDPP) / 2

    # NEGATIVA

    MitadMACDPN = (maximoMACDPN + minimoMACDPN) / 2
    PcuartoMACDPN = (MitadMACDPN + minimoMACDPN) / 2
    TcuartoMACDPN = (MitadMACDPN + maximoMACDPN) / 2
    PoctavoMACDPN = (minimoMACDPN + PcuartoMACDPN) / 2
    ToctavoMACDPN = (PcuartoMACDPN + MitadMACDPN) / 2
    QoctavoMACDPN = (MitadMACDPN + TcuartoMACDPN) / 2
    SoctavoMACDPN = (TcuartoMACDPN + maximoMACDPN) / 2

    # PARA ICPB

    if fin < 2:
        maximoICPB = float(numpy.nanmax(tabla.iloc[2:-1, 10].values))
        minimoICPB = float(numpy.nanmin(tabla.iloc[2:-1, 10].values))
    if fin > 2:
        maximoICPB = float(numpy.nanmax(tabla.iloc[fin:-1, 10].values))
        minimoICPB = float(numpy.nanmin(tabla.iloc[fin:-1, 10].values))

    MitadICPB = (maximoICPB + minimoICPB) / 2
    PcuartoICPB = (MitadICPB + minimoICPB) / 2
    TcuartoICPB = (MitadICPB + maximoICPB) / 2
    PoctavoICPB = (minimoICPB + PcuartoICPB) / 2
    ToctavoICPB = (PcuartoICPB + MitadICPB) / 2
    QoctavoICPB = (MitadICPB + TcuartoICPB) / 2
    SoctavoICPB = (TcuartoICPB + maximoICPB) / 2

    # PARA Pendiente
    if fin < 2:
        maximoICPBPP = float(numpy.nanmax(tabla.iloc[2:-1, 11].values))
        minimoICPBPP = 0
        maximoICPBPN = 0
        minimoICPBPN = float(numpy.nanmin(tabla.iloc[2:-1, 11].values))
    if fin > 2:
        maximoICPBPP = float(numpy.nanmax(tabla.iloc[fin:-1, 11].values))
        minimoICPBPP = 0
        maximoICPBPN = 0
        minimoICPBPN = float(numpy.nanmin(tabla.iloc[fin:-1, 11].values))

    # PARA POSITIVA

    MitadICPBPP = (maximoICPBPP + minimoICPBPP) / 2
    PcuartoICPBPP = (MitadICPBPP + minimoICPBPP) / 2
    TcuartoICPBPP = (MitadICPBPP + maximoICPBPP) / 2
    PoctavoICPBPP = (minimoICPBPP + PcuartoICPBPP) / 2
    ToctavoICPBPP = (PcuartoICPBPP + MitadICPBPP) / 2
    QoctavoICPBPP = (MitadICPBPP + TcuartoICPBPP) / 2
    SoctavoICPBPP = (TcuartoICPBPP + maximoICPBPP) / 2

    # PARA NEGATIVA

    MitadICPBPN = (maximoICPBPN + minimoICPBPN) / 2
    PcuartoICPBPN = (MitadICPBPN + minimoICPBPN) / 2
    TcuartoICPBPN = (MitadICPBPN + maximoICPBPN) / 2
    PoctavoICPBPN = (minimoICPBPN + PcuartoICPBPN) / 2
    ToctavoICPBPN = (PcuartoICPBPN + MitadICPBPN) / 2
    QoctavoICPBPN = (MitadICPBPN + TcuartoICPBPN) / 2
    SoctavoICPBPN = (TcuartoICPBPN + maximoICPBPN) / 2

    # PARA IMDM
    if fin < 2:
        maximoIMDM = float(numpy.nanmax(tabla.iloc[2:-1, 8].values))
        minimoIMDM = float(numpy.nanmin(tabla.iloc[2:-1, 8].values))
    if fin > 2:
        maximoIMDM = float(numpy.nanmax(tabla.iloc[fin:-1, 8].values))
        minimoIMDM = float(numpy.nanmin(tabla.iloc[fin:-1, 8].values))


    MitadIMDM = (maximoIMDM + minimoIMDM) / 2
    PcuartoIMDM = (MitadIMDM + minimoIMDM) / 2
    TcuartoIMDM = (MitadIMDM + maximoIMDM) / 2
    PoctavoIMDM = (minimoIMDM + PcuartoIMDM) / 2
    ToctavoIMDM = (PcuartoIMDM + MitadIMDM) / 2
    QoctavoIMDM = (MitadIMDM + TcuartoIMDM) / 2
    SoctavoIMDM = (TcuartoIMDM + maximoIMDM) / 2

    # PARA Pendiente
    if fin < 2:
        maximoIMDMPP = float(numpy.nanmax(tabla.iloc[2:-1, 9].values))
        minimoIMDMPP = 0
        maximoIMDMPN = 0
        minimoIMDMPN = float(numpy.nanmin(tabla.iloc[2:-1, 9].values))
    if fin > 2:
        maximoIMDMPP = float(numpy.nanmax(tabla.iloc[fin:-1, 9].values))
        minimoIMDMPP = 0
        maximoIMDMPN = 0
        minimoIMDMPN = float(numpy.nanmin(tabla.iloc[fin:-1, 9].values))

    # PARA POSITIVA

    MitadIMDMPP = (maximoIMDMPP + minimoIMDMPP) / 2
    PcuartoIMDMPP = (MitadIMDMPP + minimoIMDMPP) / 2
    TcuartoIMDMPP = (MitadIMDMPP + maximoIMDMPP) / 2
    PoctavoIMDMPP = (minimoIMDMPP + PcuartoIMDMPP) / 2
    ToctavoIMDMPP = (PcuartoIMDMPP + MitadIMDMPP) / 2
    QoctavoIMDMPP = (MitadIMDMPP + TcuartoIMDMPP) / 2
    SoctavoIMDMPP = (TcuartoIMDMPP + maximoIMDMPP) / 2

    # PARA NEGATIVA

    MitadIMDMPN = (maximoIMDMPN + minimoIMDMPN) / 2
    PcuartoIMDMPN = (MitadIMDMPN + minimoIMDMPN) / 2
    TcuartoIMDMPN = (MitadIMDMPN + maximoIMDMPN) / 2
    PoctavoIMDMPN = (minimoIMDMPN + PcuartoIMDMPN) / 2
    ToctavoIMDMPN = (PcuartoIMDMPN + MitadIMDMPN) / 2
    QoctavoIMDMPN = (MitadIMDMPN + TcuartoIMDMPN) / 2
    SoctavoIMDMPN = (TcuartoIMDMPN + maximoIMDMPN) / 2

    # PARA OA
    if fin < 2:
        maximoOA = float(numpy.nanmax(tabla.iloc[2:-1, 12].values))
        minimoOA = float(numpy.nanmin(tabla.iloc[2:-1, 12].values))
    if fin > 2:
        maximoOA = float(numpy.nanmax(tabla.iloc[fin:-1, 12].values))
        minimoOA = float(numpy.nanmin(tabla.iloc[fin:-1, 12].values))

    MitadOA = (maximoOA + minimoOA) / 2
    PcuartoOA = (MitadOA + minimoOA) / 2
    TcuartoOA = (MitadOA + maximoOA) / 2
    PoctavoOA = (minimoOA + PcuartoOA) / 2
    ToctavoOA = (PcuartoOA + MitadOA) / 2
    QoctavoOA = (MitadOA + TcuartoOA) / 2
    SoctavoOA = (TcuartoOA + maximoOA) / 2

    # PARA Pendiente
    if fin < 2:
        maximoOAPP = float(numpy.nanmax(tabla.iloc[2:-1, 13].values))
        minimoOAPP = 0
        maximoOAPN = 0
        minimoOAPN = float(numpy.nanmin(tabla.iloc[2:-1, 13].values))
    if fin > 2:
        maximoOAPP = float(numpy.nanmax(tabla.iloc[fin:-1, 13].values))
        minimoOAPP = 0
        maximoOAPN = 0
        minimoOAPN = float(numpy.nanmin(tabla.iloc[fin:-1, 13].values))

    # PARA POSITIVA

    MitadOAPP = (maximoOAPP + minimoOAPP) / 2
    PcuartoOAPP = (MitadOAPP + minimoOAPP) / 2
    TcuartoOAPP = (MitadOAPP + maximoOAPP) / 2
    PoctavoOAPP = (minimoOAPP + PcuartoOAPP) / 2
    ToctavoOAPP = (PcuartoOAPP + MitadOAPP) / 2
    QoctavoOAPP = (MitadOAPP + TcuartoOAPP) / 2
    SoctavoOAPP = (TcuartoOAPP + maximoOAPP) / 2

    # PARA NEGATIVA

    MitadOAPN = (maximoOAPN + minimoOAPN) / 2
    PcuartoOAPN = (MitadOAPN + minimoOAPN) / 2
    TcuartoOAPN = (MitadOAPN + maximoOAPN) / 2
    PoctavoOAPN = (minimoOAPN + PcuartoOAPN) / 2
    ToctavoOAPN = (PcuartoOAPN + MitadOAPN) / 2
    QoctavoOAPN = (MitadOAPN + TcuartoOAPN) / 2
    SoctavoOAPN = (TcuartoOAPN + maximoOAPN) / 2

    # PARA RSIR
    if fin < 2:
        maximoRSIR = float(numpy.nanmax(tabla.iloc[2:-1, 14].values))
        minimoRSIR = float(numpy.nanmin(tabla.iloc[2:-1, 14].values))
    if fin > 2:
        maximoRSIR = float(numpy.nanmax(tabla.iloc[fin:-1, 14].values))
        minimoRSIR = float(numpy.nanmin(tabla.iloc[fin:-1, 14].values))

    MitadRSIR = (maximoRSIR + minimoRSIR) / 2
    PcuartoRSIR = (MitadRSIR + minimoRSIR) / 2
    TcuartoRSIR = (MitadRSIR + maximoRSIR) / 2
    PoctavoRSIR = (minimoRSIR + PcuartoRSIR) / 2
    ToctavoRSIR = (PcuartoRSIR + MitadRSIR) / 2
    QoctavoRSIR = (MitadRSIR + TcuartoRSIR) / 2
    SoctavoRSIR = (TcuartoRSIR + maximoRSIR) / 2

    # PARA Pendiente
    if fin < 2:
        maximoRSIRPP = float(numpy.nanmax(tabla.iloc[2:-1, 15].values))
        minimoRSIRPP = 0
        maximoRSIRPN = 0
        minimoRSIRPN = float(numpy.nanmin(tabla.iloc[2:-1, 15].values))
    if fin > 2:
        maximoRSIRPP = float(numpy.nanmax(tabla.iloc[fin:-1, 15].values))
        minimoRSIRPP = 0
        maximoRSIRPN = 0
        minimoRSIRPN = float(numpy.nanmin(tabla.iloc[fin:-1, 15].values))

    # PARA POSITIVA

    MitadRSIRPP = (maximoRSIRPP + minimoRSIRPP) / 2
    PcuartoRSIRPP = (MitadRSIRPP + minimoRSIRPP) / 2
    TcuartoRSIRPP = (MitadRSIRPP + maximoRSIRPP) / 2
    PoctavoRSIRPP = (minimoRSIRPP + PcuartoRSIRPP) / 2
    ToctavoRSIRPP = (PcuartoRSIRPP + MitadRSIRPP) / 2
    QoctavoRSIRPP = (MitadRSIRPP + TcuartoRSIRPP) / 2
    SoctavoRSIRPP = (TcuartoRSIRPP + maximoRSIRPP) / 2

    # PARA NEGATIVA

    MitadRSIRPN = (maximoRSIRPN + minimoRSIRPN) / 2
    PcuartoRSIRPN = (MitadRSIRPN + minimoRSIRPN) / 2
    TcuartoRSIRPN = (MitadRSIRPN + maximoRSIRPN) / 2
    PoctavoRSIRPN = (minimoRSIRPN + PcuartoRSIRPN) / 2
    ToctavoRSIRPN = (PcuartoRSIRPN + MitadRSIRPN) / 2
    QoctavoRSIRPN = (MitadRSIRPN + TcuartoRSIRPN) / 2
    SoctavoRSIRPN = (TcuartoRSIRPN + maximoRSIRPN) / 2

    # PARA Williams
    if fin < 2:
        maximoWilliams = float(numpy.nanmax(tabla.iloc[2:-1, 16].values))
        minimoWilliams = float(numpy.nanmin(tabla.iloc[2:-1, 16].values))
    if fin > 2:
        maximoWilliams = float(numpy.nanmax(tabla.iloc[fin:-1, 16].values))
        minimoWilliams = float(numpy.nanmin(tabla.iloc[fin:-1, 16].values))

    MitadWilliams = (maximoWilliams + minimoWilliams) / 2
    PcuartoWilliams = (MitadWilliams + minimoWilliams) / 2
    TcuartoWilliams = (MitadWilliams + maximoWilliams) / 2
    PoctavoWilliams = (minimoWilliams + PcuartoWilliams) / 2
    ToctavoWilliams = (PcuartoWilliams + MitadWilliams) / 2
    QoctavoWilliams = (MitadWilliams + TcuartoWilliams) / 2
    SoctavoWilliams = (TcuartoWilliams + maximoWilliams) / 2

    # PARA Pendiente
    if fin < 2:
        maximoWilliamsPP = float(numpy.nanmax(tabla.iloc[2:-1, 17].values))
        minimoWilliamsPP = 0
        maximoWilliamsPN = 0
        minimoWilliamsPN = float(numpy.nanmin(tabla.iloc[2:-1, 17].values))
    if fin > 2:
        maximoWilliamsPP = float(numpy.nanmax(tabla.iloc[fin:-1, 17].values))
        minimoWilliamsPP = 0
        maximoWilliamsPN = 0
        minimoWilliamsPN = float(numpy.nanmin(tabla.iloc[fin:-1, 17].values))

    # PARA POSITIVA

    MitadWilliamsPP = (maximoWilliamsPP + minimoWilliamsPP) / 2
    PcuartoWilliamsPP = (MitadWilliamsPP + minimoWilliamsPP) / 2
    TcuartoWilliamsPP = (MitadWilliamsPP + maximoWilliamsPP) / 2
    PoctavoWilliamsPP = (minimoWilliamsPP + PcuartoWilliamsPP) / 2
    ToctavoWilliamsPP = (PcuartoWilliamsPP + MitadWilliamsPP) / 2
    QoctavoWilliamsPP = (MitadWilliamsPP + TcuartoWilliamsPP) / 2
    SoctavoWilliamsPP = (TcuartoWilliamsPP + maximoWilliamsPP) / 2

    # PARA NEGATIVA

    MitadWilliamsPN = (maximoWilliamsPN + minimoWilliamsPN) / 2
    PcuartoWilliamsPN = (MitadWilliamsPN + minimoWilliamsPN) / 2
    TcuartoWilliamsPN = (MitadWilliamsPN + maximoWilliamsPN) / 2
    PoctavoWilliamsPN = (minimoWilliamsPN + PcuartoWilliamsPN) / 2
    ToctavoWilliamsPN = (PcuartoWilliamsPN + MitadWilliamsPN) / 2
    QoctavoWilliamsPN = (MitadWilliamsPN + TcuartoWilliamsPN) / 2
    SoctavoWilliamsPN = (TcuartoWilliamsPN + maximoWilliamsPN) / 2

    # PARA OU
    if fin < 2:
        maximoOU = float(numpy.nanmax(tabla.iloc[2:-1, 18].values))
        minimoOU = float(numpy.nanmin(tabla.iloc[2:-1, 18].values))
    if fin > 2:
        maximoOU = float(numpy.nanmax(tabla.iloc[fin:-1, 18].values))
        minimoOU = float(numpy.nanmin(tabla.iloc[fin:-1, 18].values))

    MitadOU = (maximoOU + minimoOU) / 2
    PcuartoOU = (MitadOU + minimoOU) / 2
    TcuartoOU = (MitadOU + maximoOU) / 2
    PoctavoOU = (minimoOU + PcuartoOU) / 2
    ToctavoOU = (PcuartoOU + MitadOU) / 2
    QoctavoOU = (MitadOU + TcuartoOU) / 2
    SoctavoOU = (TcuartoOU + maximoOU) / 2

    # PARA Pendiente
    if fin < 2:
        maximoOUPP = float(numpy.nanmax(tabla.iloc[2:-1, 19].values))
        minimoOUPP = 0
        maximoOUPN = 0
        minimoOUPN = float(numpy.nanmin(tabla.iloc[2:-1, 19].values))
    if fin > 2:
        maximoOUPP = float(numpy.nanmax(tabla.iloc[fin:-1, 19].values))
        minimoOUPP = 0
        maximoOUPN = 0
        minimoOUPN = float(numpy.nanmin(tabla.iloc[fin:-1, 19].values))
    # PARA POSITIVA

    MitadOUPP = (maximoOUPP + minimoOUPP) / 2
    PcuartoOUPP = (MitadOUPP + minimoOUPP) / 2
    TcuartoOUPP = (MitadOUPP + maximoOUPP) / 2
    PoctavoOUPP = (minimoOUPP + PcuartoOUPP) / 2
    ToctavoOUPP = (PcuartoOUPP + MitadOUPP) / 2
    QoctavoOUPP = (MitadOUPP + TcuartoOUPP) / 2
    SoctavoOUPP = (TcuartoOUPP + maximoOUPP) / 2

    # PARA NEGATIVA

    MitadOUPN = (maximoOUPN + minimoOUPN) / 2
    PcuartoOUPN = (MitadOUPN + minimoOUPN) / 2
    TcuartoOUPN = (MitadOUPN + maximoOUPN) / 2
    PoctavoOUPN = (minimoOUPN + PcuartoOUPN) / 2
    ToctavoOUPN = (PcuartoOUPN + MitadOUPN) / 2
    QoctavoOUPN = (MitadOUPN + TcuartoOUPN) / 2
    SoctavoOUPN = (TcuartoOUPN + maximoOUPN) / 2


    # Maximizo



    contador = 0


    while contador < 30:
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
        DatoRSI = float(RSI)
        #Wiliams
        Estocastico = driver.find_element_by_xpath(
        '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[9]/td[2]').text
        Estocastico = Estocastico.replace('−', '-')
        Estocastico = float(Estocastico)
        DatoESTOCASTICO = float(Estocastico)
        MACD = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[8]/td[2]').text
        MACD = MACD.replace('−', '-')
        MACD = float(MACD)
        DatoMACD = float(MACD)

        volumen = driver.find_element_by_xpath('//*[@id="anchor-page-1"]/div/div[3]/div[3]/div[3]/div[1]').text
        volumen = volumen.replace('K', '')
        volumen = float(volumen)

        volumenV = float(tabla.iloc[-1, 9])
        volumenN = volumen
        volumenP = float((volumenN - volumenV) / 0.1)
        DatoVolumenP=volumenP


        RSIV = float(tabla.iloc[-1, 2])
        RSIN = RSI
        RSIP = float((RSIN - RSIV) / 0.1)
        DatoRSIP=RSIP

        EstocasticoV = float(tabla.iloc[-1, 4])
        EstocasticoN = Estocastico
        EstocasticoP = float((EstocasticoN - EstocasticoV) / 0.1)
        DatoESTOCASTICOP=EstocasticoP

        MACDV = float(tabla.iloc[-1, 6])
        MACDN = MACD
        MACDP = float((MACDN - MACDV) / 0.1)
        DatoMACDP=MACDP

        ICPB = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[4]/td[2]').text
        ICPB = ICPB.replace('−', '-')
        ICPB = float(ICPB)
        DatoICPB=ICPB
        IMDM = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[5]/td[2]').text
        IMDM = IMDM.replace('−', '-')
        IMDM = float(IMDM)
        DatoIMDM=IMDM
        OA = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[6]/td[2]').text
        OA = OA.replace('−', '-')
        OA = float(OA)
        DatoOA=OA

        RSIR = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[9]/td[2]').text
        RSIR = RSIR.replace('−', '-')
        RSIR = float(RSIR)
        DatoRSIR=RSIR
        Williams = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[10]/td[2]').text
        Williams = Williams.replace('−', '-')
        Williams = float(Williams)
        DatoWilliams=Williams

        OU = driver.find_element_by_xpath(
            '//*[@id="technicals-root"]/div/div/div[3]/div[1]/div[2]/table/tbody/tr[12]/td[2]').text
        OU = OU.replace('−', '-')
        OU = float(OU)
        DatoOU=OU

        IMDMV = float(tabla.iloc[-1, 8])
        IMDMN = IMDM
        IMDMP = float((IMDMN - IMDMV) / 0.1)
        DatoIMDMP=IMDMP

        ICPBV = float(tabla.iloc[-1, 10])
        ICPBN = ICPB
        ICPBP = float((ICPBN - ICPBV) / 0.1)
        DatoICPBP=ICPBP

        OAV = float(tabla.iloc[-1, 12])
        OAN = OA
        OAP = float((OAN - OAV) / 0.1)
        DatoOAP=OAP

        RSIRV = float(tabla.iloc[-1, 14])
        RSIRN = RSIR
        RSIRP = float((RSIRN - RSIRV) / 0.1)
        DatoRSIRP=RSIRP

        WilliamsV = float(tabla.iloc[-1, 16])
        WilliamsN = Williams
        WilliamsP = float((WilliamsN - WilliamsV) / 0.1)
        DatoWilliamsP= WilliamsP

        OUV = float(tabla.iloc[-1, 18])
        OUN =OU
        OUP = float((OUN - OUV) / 0.1)
        DatoOUP=OUP


        Datos5m = {'1': precio, '2': ['-'], '3': RSI, '4': RSIP, '5': Estocastico, '6': EstocasticoP, '7': MACD,
                   '8': MACDP,'9': IMDM, '10': IMDMP, '11': ICPB, '12': ICPBP, '13': OA,
                   '14': OAP, '15': RSIR, '16': RSIRP, '17': Williams, '18': WilliamsP, '19': OU,
                   '20': OUP, '21': hora, '22':volumen,'23':volumenP}

        tabla = tabla.append(Datos5m, ignore_index=True)

        # ACTUALIZO LA PAGINA

        driver.refresh()

        sleep(random.randint(12, 18))

        if DatoRSI > MitadRSI:
            if DatoRSI > TcuartoRSI:
                if DatoRSI > SoctavoRSI:
                    MRSI = 8
                else:
                    MRSI = 7
            else:
                if DatoRSI > QoctavoRSI:
                    MRSI = 6
                else:
                    MRSI = 5

        else:
            if DatoRSI > PcuartoRSI:
                if DatoRSI > ToctavoRSI:
                    MRSI = 4
                else:
                    MRSI = 3
            else:
                if DatoRSI > PoctavoRSI:
                    MRSI = 2
                else:
                    MRSI = 1

        if DatoESTOCASTICO > MitadESTOCASTICO:
            if DatoESTOCASTICO > TcuartoESTOCASTICO:
                if DatoESTOCASTICO > SoctavoESTOCASTICO:
                    MESTOCASTICO = 8
                else:
                    MESTOCASTICO = 7
            else:
                if DatoESTOCASTICO > QoctavoESTOCASTICO:
                    MESTOCASTICO = 6
                else:
                    MESTOCASTICO = 5

        else:
            if DatoESTOCASTICO > PcuartoESTOCASTICO:
                if DatoESTOCASTICO > ToctavoESTOCASTICO:
                    MESTOCASTICO = 4
                else:
                    MESTOCASTICO = 3
            else:
                if DatoESTOCASTICO > PoctavoESTOCASTICO:
                    MESTOCASTICO = 2
                else:
                    MESTOCASTICO = 1

        if DatoMACD > MitadMACD:
            if DatoMACD > TcuartoMACD:
                if DatoMACD > SoctavoMACD:
                    MMACD = 8
                else:
                    MMACD = 7
            else:
                if DatoMACD > QoctavoMACD:
                    MMACD = 6
                else:
                    MMACD = 5
        else:
            if DatoMACD > PcuartoMACD:
                if DatoMACD > ToctavoMACD:
                    MMACD = 4
                else:
                    MMACD = 3
            else:
                if DatoMACD > PoctavoMACD:
                    MMACD = 2
                else:
                    MMACD = 1

        # rangeo pendientes
        if DatoRSIP > 0:
            if DatoRSIP > MitadRSIPP:
                if DatoRSIP > TcuartoRSIPP:
                    if DatoRSIP > SoctavoRSIPP:
                        MRSIP = 4
                    else:
                        MRSIP = 4
                else:
                    if DatoRSIP > QoctavoRSIPP:
                        MRSIP = 4
                    else:
                        MRSIP = 4

            else:
                if DatoRSIP > PcuartoRSIPP:
                    if DatoRSIP > ToctavoRSIPP:
                        MRSIP = 3
                    else:
                        MRSIP = 3
                else:
                    if DatoRSIP > PoctavoRSIPP:
                        MRSIP = 3
                    else:
                        MRSIP = 3
        else:
            if DatoRSIP > MitadRSIPN:
                if DatoRSIP > TcuartoRSIPN:
                    if DatoRSIP > SoctavoRSIPN:
                        MRSIP = 2
                    else:
                        MRSIP = 2
                else:
                    if DatoRSIP > QoctavoRSIPN:
                        MRSIP = 2
                    else:
                        MRSIP = 2
            else:
                if DatoRSIP > PcuartoRSIPN:
                    if DatoRSIP > ToctavoRSIPN:
                        MRSIP = 1
                    else:
                        MRSIP = 1
                else:
                    if DatoRSIP > PoctavoRSIPN:
                        MRSIP = 1
                    else:
                        MRSIP = 1

        if DatoESTOCASTICOP > 0:
            if DatoESTOCASTICOP > MitadESTOCASTICOPP:
                if DatoESTOCASTICOP > TcuartoESTOCASTICOPP:
                    if DatoESTOCASTICOP > SoctavoESTOCASTICOPP:
                        MESTOCASTICOP = 4
                    else:
                        MESTOCASTICOP = 4
                else:
                    if DatoESTOCASTICOP > QoctavoESTOCASTICOPP:
                        MESTOCASTICOP = 4
                    else:
                        MESTOCASTICOP = 4
            else:
                if DatoESTOCASTICOP > PcuartoESTOCASTICOPP:
                    if DatoESTOCASTICOP > ToctavoESTOCASTICOPP:
                        MESTOCASTICOP = 3
                    else:
                        MESTOCASTICOP = 3
                else:
                    if DatoESTOCASTICOP > PoctavoESTOCASTICOPP:
                        MESTOCASTICOP = 3
                    else:
                        MESTOCASTICOP = 3

        else:
            if DatoESTOCASTICOP > MitadESTOCASTICOPN:
                if DatoESTOCASTICOP > TcuartoESTOCASTICOPN:
                    if DatoESTOCASTICOP > SoctavoESTOCASTICOPN:
                        MESTOCASTICOP = 2
                    else:
                        MESTOCASTICOP = 2
                else:
                    if DatoESTOCASTICOP > QoctavoESTOCASTICOPN:
                        MESTOCASTICOP = 2
                    else:
                        MESTOCASTICOP = 2
            else:
                if DatoESTOCASTICOP > PcuartoESTOCASTICOPN:
                    if DatoESTOCASTICOP > ToctavoESTOCASTICOPN:
                        MESTOCASTICOP = 1
                    else:
                        MESTOCASTICOP = 1
                else:
                    if DatoESTOCASTICOP > PoctavoESTOCASTICOPN:
                        MESTOCASTICOP = 1
                    else:
                        MESTOCASTICOP = 1

        if DatoMACDP > 0:
            if DatoMACDP > MitadMACDPP:
                if DatoMACDP > TcuartoMACDPP:
                    if DatoMACDP > SoctavoMACDPP:
                        MMACDP = 4
                    else:
                        MMACDP = 4
                else:
                    if DatoMACDP > QoctavoMACDPP:
                        MMACDP = 4
                    else:
                        MMACDP = 4
            else:
                if DatoMACDP > PcuartoMACDPP:
                    if DatoMACDP > ToctavoMACDPP:
                        MMACDP = 3
                    else:
                        MMACDP = 3
                else:
                    if DatoMACDP > PoctavoMACDPP:
                        MMACDP = 3
                    else:
                        MMACDP = 3
        else:
            if DatoMACDP > MitadMACDPN:
                if DatoMACDP > TcuartoMACDPN:
                    if DatoMACDP > SoctavoMACDPN:
                        MMACDP = 2
                    else:
                        MMACDP = 2
                else:
                    if DatoMACDP > QoctavoMACDPN:
                        MMACDP = 2
                    else:
                        MMACDP = 2
            else:
                if DatoMACDP > PcuartoMACDPN:
                    if DatoMACDP > ToctavoMACDPN:
                        MMACDP = 1
                    else:
                        MMACDP = 1
                else:
                    if DatoMACDP > PoctavoMACDPN:
                        MMACDP = 1
                    else:
                        MMACDP = 1

        if DatoVolumenP > 0:
            MVOLP = 1
        else:
            MVOLP = 2

        if DatoIMDM > MitadIMDM:
            if DatoIMDM > TcuartoIMDM:
                if DatoIMDM > SoctavoIMDM:
                    MIMDM = 8
                else:
                    MIMDM = 7
            else:
                if DatoIMDM > QoctavoIMDM:
                    MIMDM = 6
                else:
                    MIMDM = 5

        else:
            if DatoIMDM > PcuartoIMDM:
                if DatoIMDM > ToctavoIMDM:
                    MIMDM = 4
                else:
                    MIMDM = 3
            else:
                if DatoIMDM > PoctavoIMDM:
                    MIMDM = 2
                else:
                    MIMDM = 1


        # rangeo pendientes
        if DatoIMDMP > 0:
            if DatoIMDMP > MitadIMDMPP:
                if DatoIMDMP > TcuartoIMDMPP:
                    if DatoIMDMP > SoctavoIMDMPP:
                        MIMDMP = 4
                    else:
                        MIMDMP = 4
                else:
                    if DatoIMDMP > QoctavoIMDMPP:
                        MIMDMP = 4
                    else:
                        MIMDMP = 4

            else:
                if DatoIMDMP > PcuartoIMDMPP:
                    if DatoIMDMP > ToctavoIMDMPP:
                        MIMDMP = 3
                    else:
                        MIMDMP = 3
                else:
                    if DatoIMDMP > PoctavoIMDMPP:
                        MIMDMP = 3
                    else:
                        MIMDMP = 3
        else:
            if DatoIMDMP > MitadIMDMPN:
                if DatoIMDMP > TcuartoIMDMPN:
                    if DatoIMDMP > SoctavoIMDMPN:
                        MIMDMP = 2
                    else:
                        MIMDMP = 2
                else:
                    if DatoIMDMP > QoctavoIMDMPN:
                        MIMDMP = 2
                    else:
                        MIMDMP = 2
            else:
                if DatoIMDMP > PcuartoIMDMPN:
                    if DatoIMDMP > ToctavoIMDMPN:
                        MIMDMP = 1
                    else:
                        MIMDMP = 1
                else:
                    if DatoIMDMP > PoctavoIMDMPN:
                        MIMDMP = 1
                    else:
                        MIMDMP = 1




        if DatoICPB > MitadICPB:
            if DatoICPB > TcuartoICPB:
                if DatoICPB > SoctavoICPB:
                    MICPB = 8
                else:
                    MICPB = 7
            else:
                if DatoICPB > QoctavoICPB:
                    MICPB = 6
                else:
                    MICPB = 5

        else:
            if DatoICPB > PcuartoICPB:
                if DatoICPB > ToctavoICPB:
                    MICPB = 4
                else:
                    MICPB = 3
            else:
                if DatoICPB > PoctavoICPB:
                    MICPB = 2
                else:
                    MICPB = 1

        # rangeo pendientes
        if DatoICPBP > 0:
            if DatoICPBP > MitadICPBPP:
                if DatoICPBP > TcuartoICPBPP:
                    if DatoICPBP > SoctavoICPBPP:
                        MICPBP = 4
                    else:
                        MICPBP = 4
                else:
                    if DatoICPBP > QoctavoICPBPP:
                        MICPBP = 4
                    else:
                        MICPBP = 4

            else:
                if DatoICPBP > PcuartoICPBPP:
                    if DatoICPBP > ToctavoICPBPP:
                        MICPBP = 3
                    else:
                        MICPBP = 3
                else:
                    if DatoICPBP > PoctavoICPBPP:
                        MICPBP = 3
                    else:
                        MICPBP = 3
        else:
            if DatoICPBP > MitadICPBPN:
                if DatoICPBP > TcuartoICPBPN:
                    if DatoICPBP > SoctavoICPBPN:
                        MICPBP = 2
                    else:
                        MICPBP = 2
                else:
                    if DatoICPBP > QoctavoICPBPN:
                        MICPBP = 2
                    else:
                        MICPBP = 2
            else:
                if DatoICPBP > PcuartoICPBPN:
                    if DatoICPBP > ToctavoICPBPN:
                        MICPBP = 1
                    else:
                        MICPBP = 1
                else:
                    if DatoICPBP > PoctavoICPBPN:
                        MICPBP = 1
                    else:
                        MICPBP = 1





        if DatoOA > MitadOA:
            if DatoOA > TcuartoOA:
                if DatoOA > SoctavoOA:
                    MOA = 8
                else:
                    MOA = 7
            else:
                if DatoOA > QoctavoOA:
                    MOA = 6
                else:
                    MOA = 5

        else:
            if DatoOA > PcuartoOA:
                if DatoOA > ToctavoOA:
                    MOA = 4
                else:
                    MOA = 3
            else:
                if DatoOA > PoctavoOA:
                    MOA = 2
                else:
                    MOA = 1

            # rangeo pendientes
        if DatoOAP > 0:
            if DatoOAP > MitadOAPP:
                if DatoOAP > TcuartoOAPP:
                    if DatoOAP > SoctavoOAPP:
                        MOAP = 4
                    else:
                        MOAP = 4
                else:
                    if DatoOAP > QoctavoOAPP:
                        MOAP = 4
                    else:
                        MOAP = 4

            else:
                if DatoOAP > PcuartoOAPP:
                    if DatoOAP > ToctavoOAPP:
                        MOAP = 3
                    else:
                        MOAP = 3
                else:
                    if DatoOAP > PoctavoOAPP:
                        MOAP = 3
                    else:
                        MOAP = 3
        else:
            if DatoOAP > MitadOAPN:
                if DatoOAP > TcuartoOAPN:
                    if DatoOAP > SoctavoOAPN:
                        MOAP = 2
                    else:
                        MOAP = 2
                else:
                    if DatoOAP > QoctavoOAPN:
                        MOAP = 2
                    else:
                        MOAP = 2
            else:
                if DatoOAP > PcuartoOAPN:
                    if DatoOAP > ToctavoOAPN:
                        MOAP = 1
                    else:
                        MOAP = 1
                else:
                    if DatoOAP > PoctavoOAPN:
                        MOAP = 1
                    else:
                        MOAP = 1

        if DatoRSIR > MitadRSIR:
            if DatoRSIR > TcuartoRSIR:
                if DatoRSIR > SoctavoRSIR:
                    MRSIR = 8
                else:
                    MRSIR = 7
            else:
                if DatoRSIR > QoctavoRSIR:
                    MRSIR = 6
                else:
                    MRSIR = 5

        else:
            if DatoRSIR > PcuartoRSIR:
                if DatoRSIR > ToctavoRSIR:
                    MRSIR = 4
                else:
                    MRSIR = 3
            else:
                if DatoRSIR > PoctavoRSIR:
                    MRSIR = 2
                else:
                    MRSIR = 1

            # rangeo pendientes
        if DatoRSIRP > 0:
            if DatoRSIRP > MitadRSIRPP:
                if DatoRSIRP > TcuartoRSIRPP:
                    if DatoRSIRP > SoctavoRSIRPP:
                        MRSIRP = 4
                    else:
                        MRSIRP = 4
                else:
                    if DatoRSIRP > QoctavoRSIRPP:
                        MRSIRP = 4
                    else:
                        MRSIRP = 4

            else:
                if DatoRSIRP > PcuartoRSIRPP:
                    if DatoRSIRP > ToctavoRSIRPP:
                        MRSIRP = 3
                    else:
                        MRSIRP = 3
                else:
                    if DatoRSIRP > PoctavoRSIRPP:
                        MRSIRP = 3
                    else:
                        MRSIRP = 3
        else:
            if DatoRSIRP > MitadRSIRPN:
                if DatoRSIRP > TcuartoRSIRPN:
                    if DatoRSIRP > SoctavoRSIRPN:
                        MRSIRP = 2
                    else:
                        MRSIRP = 2
                else:
                    if DatoRSIRP > QoctavoRSIRPN:
                        MRSIRP = 2
                    else:
                        MRSIRP = 2
            else:
                if DatoRSIRP > PcuartoRSIRPN:
                    if DatoRSIRP > ToctavoRSIRPN:
                        MRSIRP = 1
                    else:
                        MRSIRP = 1
                else:
                    if DatoRSIRP > PoctavoRSIRPN:
                        MRSIRP = 1
                    else:
                        MRSIRP = 1

        if DatoWilliams > MitadWilliams:
            if DatoWilliams > TcuartoWilliams:
                if DatoWilliams > SoctavoWilliams:
                    MWilliams = 8
                else:
                    MWilliams = 7
            else:
                if DatoWilliams > QoctavoWilliams:
                    MWilliams = 6
                else:
                    MWilliams = 5

        else:
            if DatoWilliams > PcuartoWilliams:
                if DatoWilliams > ToctavoWilliams:
                    MWilliams = 4
                else:
                    MWilliams = 3
            else:
                if DatoWilliams > PoctavoWilliams:
                    MWilliams = 2
                else:
                    MWilliams = 1

            # rangeo pendientes
        if DatoWilliamsP > 0:
            if DatoWilliamsP > MitadWilliamsPP:
                if DatoWilliamsP > TcuartoWilliamsPP:
                    if DatoWilliamsP > SoctavoWilliamsPP:
                        MWilliamsP = 4
                    else:
                        MWilliamsP = 4
                else:
                    if DatoWilliamsP > QoctavoWilliamsPP:
                        MWilliamsP = 4
                    else:
                        MWilliamsP = 4

            else:
                if DatoWilliamsP > PcuartoWilliamsPP:
                    if DatoWilliamsP > ToctavoWilliamsPP:
                        MWilliamsP = 3
                    else:
                        MWilliamsP = 3
                else:
                    if DatoWilliamsP > PoctavoWilliamsPP:
                        MWilliamsP = 3
                    else:
                        MWilliamsP = 3
        else:
            if DatoWilliamsP > MitadWilliamsPN:
                if DatoWilliamsP > TcuartoWilliamsPN:
                    if DatoWilliamsP > SoctavoWilliamsPN:
                        MWilliamsP = 2
                    else:
                        MWilliamsP = 2
                else:
                    if DatoWilliamsP > QoctavoWilliamsPN:
                        MWilliamsP = 2
                    else:
                        MWilliamsP = 2
            else:
                if DatoWilliamsP > PcuartoWilliamsPN:
                    if DatoWilliamsP > ToctavoWilliamsPN:
                        MWilliamsP = 1
                    else:
                        MWilliamsP = 1
                else:
                    if DatoWilliamsP > PoctavoWilliamsPN:
                        MWilliamsP = 1
                    else:
                        MWilliamsP = 1


        if DatoOU > MitadOU:
            if DatoOU > TcuartoOU:
                if DatoOU > SoctavoOU:
                    MOU = 8
                else:
                    MOU = 7
            else:
                if DatoOU > QoctavoOU:
                    MOU = 6
                else:
                    MOU = 5

        else:
            if DatoOU > PcuartoOU:
                if DatoOU > ToctavoOU:
                    MOU = 4
                else:
                    MOU = 3
            else:
                if DatoOU > PoctavoOU:
                    MOU = 2
                else:
                    MOU = 1

            # rangeo pendientes
        if DatoOUP > 0:
            if DatoOUP > MitadOUPP:
                if DatoOUP > TcuartoOUPP:
                    if DatoOUP > SoctavoOUPP:
                        MOUP = 4
                    else:
                        MOUP = 4
                else:
                    if DatoOUP > QoctavoOUPP:
                        MWOUP = 4
                    else:
                        MOUP = 4

            else:
                if DatoOUP > PcuartoOUPP:
                    if DatoOUP > ToctavoOUPP:
                        MOUP = 3
                    else:
                        MOUP = 3
                else:
                    if DatoOUP > PoctavoOUPP:
                        MOUP = 3
                    else:
                        MOUP = 3
        else:
            if DatoOUP > MitadOUPN:
                if DatoOUP > TcuartoOUPN:
                    if DatoOUP > SoctavoOUPN:
                        MOUP = 2
                    else:
                        MOUP = 2
                else:
                    if DatoOUP > QoctavoOUPN:
                        MOUP = 2
                    else:
                        MOUP = 2
            else:
                if DatoOUP > PcuartoOUPN:
                    if DatoOUP > ToctavoOUPN:
                        MOUP = 1
                    else:
                        MOUP = 1
                else:
                    if DatoOUP > PoctavoOUPN:
                        MOUP = 1
                    else:
                        MOUP = 1




        #ANALISIS Y AVISO

        #Convinado1

        fa=3

        K=0
        r=0
        while r<3:
            r+=1
            e = 0
            while e<3:
                e+=1
                m = 0
                while m<3:
                    m+=1
                    K += 1
                    if MRSI == r and MESTOCASTICO == e and MMACD == m:
                        tablaC=tablaC1
                        o=tablaC.iat[K, 1]
                        o=float(o)
                        o = o - fa
                        p3=tablaC.iat[K, 3]
                        p3= float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35= float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4= float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45=float(p45)


                        if o>5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 3 MINUTOS (' + a + '%)'
                            requests.post('https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3= 100 - p3
                            a = str(p3)
                            b = 'BAJA A 3 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3.5 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35= 100-p35
                            a = str(p35)
                            b = 'BAJA A 3.5 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4= 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 4.5 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45= 100 -p45
                            a = str(p45)
                            b = 'BAJA A 4.5 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)


        #Convinado2

        K=0
        r=5

        while r<8:
            r+=1
            e = 5
            while e<8:
                e+=1
                m = 5
                while m<8:
                    m+=1
                    K += 1
                    if MRSI == r and MESTOCASTICO == e and MMACD == m:
                        tablaC = tablaC2
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)


                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 3 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            #mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 3 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3.5 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35= 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3.5 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4= 100-p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 4.5 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 4.5 MINUTOS (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)



        if MRSI <3  and MESTOCASTICO <3 and MMACD <3:
            tablaC = tablaC3
            o = tablaC.iat[1, 1]
            o = float(o)
            o= o - fa
            p3 = tablaC.iat[1, 3]
            p3 = float(p3)
            p35 = tablaC.iat[1, 5]
            p35 = float(p35)
            p4 = tablaC.iat[1, 7]
            p4 = float(p4)
            p45 = tablaC.iat[1, 9]
            p45 = float(p45)


            if o > 5 and p3 > 75:
                a = str(p3)
                b = 'SUBE A 3 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post('https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                              data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                mouse.position = (1311, 601)
                # APUESTA BAJA
                # mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p3 < 25:
                p3 = 100 - p3
                a = str(p3)
                b = 'BAJA A 3 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                # mouse.position = (1311, 601)
                # APUESTA BAJA
                mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p35 > 75:
                a = str(p35)
                b = 'SUBE A 3.5 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                mouse.position = (1311, 601)
                # APUESTA BAJA
                # mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p35 < 25:
                p35 = 100 - p35
                a = str(p35)
                b = 'BAJA A 3.5 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                # mouse.position = (1311, 601)
                # APUESTA BAJA
                mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p4 > 75:
                a = str(p4)
                b = 'SUBE A 4 MINUTOS NIVEL 2  (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                mouse.position = (1311, 601)
                # APUESTA BAJA
                # mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p4 < 25:
                p4 = 100 - p4
                a = str(p4)
                b = 'BAJA A 4 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                # mouse.position = (1311, 601)
                # APUESTA BAJA
                mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p45 > 75:
                a = str(p45)
                b = 'SUBE A 4.5 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                mouse.position = (1311, 601)
                # APUESTA BAJA
                # mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p45 < 25:
                p45 = 100 - p45
                a = str(p45)
                b = 'BAJA A 4.5 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                # mouse.position = (1311, 601)
                # APUESTA BAJA
                mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)


        if MRSI >6  and MESTOCASTICO >6 and MMACD >6:
            tablaC = tablaC3
            o = tablaC.iat[2, 1]
            o = float(o)
            o = o - fa
            p3 = tablaC.iat[2, 3]
            p3 = float(p3)
            p35 = tablaC.iat[2, 5]
            p35 = float(p35)
            p4 = tablaC.iat[2, 7]
            p4 = float(p4)
            p45 = tablaC.iat[2, 9]
            p45 = float(p45)


            if o > 5 and p3 > 75:
                a = str(p3)
                b = 'SUBE A 3 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post('https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                              data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                mouse.position = (1311, 601)
                # APUESTA BAJA
                # mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p3 < 25:
                p3 = 100 - p3
                a = str(p3)
                b = 'BAJA A 3 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                # mouse.position = (1311, 601)
                # APUESTA BAJA
                mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p35 > 75:
                a = str(p35)
                b = 'SUBE A 3.5 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                mouse.position = (1311, 601)
                # APUESTA BAJA
                # mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p35 < 25:
                p35 = 100 - p35
                a = str(p35)
                b = 'BAJA A 3.5 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                # mouse.position = (1311, 601)
                # APUESTA BAJA
                mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p4 > 75:
                a = str(p4)
                b = 'SUBE A 4 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                mouse.position = (1311, 601)
                # APUESTA BAJA
                # mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p4 < 25:
                p4 = 100 - p4
                a = str(p4)
                b = 'BAJA A 4 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                mouse.position = (1084, 520)
                # 5MINUTOS
                # mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                # mouse.position = (1311, 601)
                # APUESTA BAJA
                mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p45 > 75:
                a = str(p45)
                b = 'SUBE A 4.5 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                mouse.position = (1311, 601)
                # APUESTA BAJA
                # mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
            if o > 5 and p45 < 25:
                p45 = 100 - p45
                a = str(p45)
                b = 'BAJA A 4.5 MINUTOS NIVEL 2 (' + a + '%)'
                requests.post(
                    'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                    data={'chat_id': '1214441101', 'text': b})
                # Prueba IQ
                mouse.position = (650, 480)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # ABRE RELOJ
                mouse.position = (1330, 355)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)
                # 2MINUTOS
                # mouse.position = (1084, 466)
                # 3MINUTOS
                # mouse.position = (1084, 488)
                # 4MINUTOS
                # mouse.position = (1084, 520)
                # 5MINUTOS
                mouse.position = (1084, 540)
                mouse.click(Button.left, 1)
                sleep(1.5)
                # APUESTA SUBE
                # mouse.position = (1311, 601)
                # APUESTA BAJA
                mouse.position = (1314, 672)
                sleep(0.5)
                mouse.click(Button.left, 1)
                sleep(0.5)



        K=0
        r=0
        while r<3:
            r+=1
            e = 0
            while e<4:
                e+=1
                m = 0
                while m<2:
                    m+=1
                    K += 1
                    if MRSI == r and MRSIP == e and MVOLP == m:
                        tablaC = tablaRSI
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='RSI'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

        K = 0
        r = 5
        while r < 8:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MRSI == r and MRSIP == e and MVOLP == m:
                        tablaC = tablaRSI1

                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='RSI'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)


        K = 0
        r = 0
        while r < 3:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MESTOCASTICO == r and MESTOCASTICOP == e and MVOLP == m:
                        tablaC = tablaEsto
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='ESTOCASTICO'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)


        K = 0
        r = 5
        while r<8:
            r+=1
            e = 0
            while e<4:
                e+=1
                m = 0
                while m<2:
                    m+=1
                    K += 1
                    if MESTOCASTICO == r and MESTOCASTICOP == e and MVOLP == m:
                        tablaC = tablaEsto1
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='ESTOCASTICO'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)




        K = 0
        r = 0
        while r < 3:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MMACD == r and MMACDP == e and MVOLP == m:
                        tablaC = tablaMACD
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='MACD'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)





        K=0
        r=5
        while r<8:
            r+=1
            e = 0
            while e<4:
                e+=1
                m = 0
                while m<2:
                    m+=1
                    K += 1
                    if MMACD == r and MMACDP == e and MVOLP == m:
                        tablaC = tablaMACD1
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='MACD'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

        K = 0
        r = 0
        while r < 3:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MIMDM == r and MIMDMP == e and MVOLP == m:
                        tablaC = tablaIMDM
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='IMDM'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)



        K = 0
        r = 5
        while r < 8:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MIMDM == r and MIMDMP == e and MVOLP == m:
                        tablaC = tablaIMDM1
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='IMDM'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

        K = 0
        r = 0
        while r < 3:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MICPB == r and MICPBP == e and MVOLP == m:
                        tablaC = tablaICPB
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='ICPB'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
        K = 0
        r = 5
        while r < 8:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MICPB == r and MICPBP == e and MVOLP == m:
                        tablaC = tablaICPB1
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='ICPB'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

        K = 0
        r = 0
        while r < 3:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MOA == r and MOAP == e and MVOLP == m:
                        tablaC = tablaOA
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='OA'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

        K = 0
        r = 5
        while r < 8:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MOA == r and MOAP == e and MVOLP == m:
                        tablaC = tablaOA1
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='OA'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

        K = 0
        r = 0
        while r < 3:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MRSIR == r and MRSIRP == e and MVOLP == m:
                        tablaC = tablaRSIR
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='RSIR'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

        K = 0
        r = 5
        while r < 8:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MRSIR == r and MRSIRP == e and MVOLP == m:
                        tablaC = tablaRSIR1
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='RSIR'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

        K = 0
        r = 0
        while r < 3:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MWilliams == r and MWilliamsP == e and MVOLP == m:
                        tablaC = tablaWilliams
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='Williams'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

        K = 0
        r = 5
        while r < 8:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MWilliams == r and MWilliamsP == e and MVOLP == m:
                        tablaC = tablaWilliams1
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='Williams'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)


        K = 0
        r = 0
        while r < 3:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MOU == r and MOUP == e and MVOLP == m:
                        tablaC = tablaOU
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - fa
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='OU'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

        K = 0
        r = 5
        while r < 8:
            r += 1
            e = 0
            while e < 4:
                e += 1
                m = 0
                while m < 2:
                    m += 1
                    K += 1
                    if MOU == r and MOUP == e and MVOLP == m:
                        tablaC = tablaOU1
                        o = tablaC.iat[K, 1]
                        o = float(o)
                        o = o - 5
                        p3 = tablaC.iat[K, 3]
                        p3 = float(p3)
                        p35 = tablaC.iat[K, 5]
                        p35 = float(p35)
                        p4 = tablaC.iat[K, 7]
                        p4 = float(p4)
                        p45 = tablaC.iat[K, 9]
                        p45 = float(p45)
                        g='OU'

                        if o > 5 and p3 > 75:
                            a = str(p3)
                            b = 'SUBE A 2 MINUTOS'+ g + '(' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p3 < 25:
                            p3 = 100 - p3
                            a = str(p3)
                            b = 'BAJA A 2 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 > 75:
                            a = str(p35)
                            b = 'SUBE A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p35 < 25:
                            p35 = 100 - p35
                            a = str(p35)
                            b = 'BAJA A 3 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 > 75:
                            a = str(p4)
                            b = 'SUBE A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p4 < 25:
                            p4 = 100 - p4
                            a = str(p4)
                            b = 'BAJA A 4 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            mouse.position = (1084, 520)
                            # 5MINUTOS
                            # mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 > 75:
                            a = str(p45)
                            b = 'SUBE A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            mouse.position = (1311, 601)
                            # APUESTA BAJA
                            # mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                        if o > 5 and p45 < 25:
                            p45 = 100 - p45
                            a = str(p45)
                            b = 'BAJA A 5 MINUTOS '+ g + ' (' + a + '%)'
                            requests.post(
                                'https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                                data={'chat_id': '1214441101', 'text': b})
                            # Prueba IQ
                            mouse.position = (650, 480)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # ABRE RELOJ
                            mouse.position = (1330, 355)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)
                            # 2MINUTOS
                            # mouse.position = (1084, 466)
                            # 3MINUTOS
                            # mouse.position = (1084, 488)
                            # 4MINUTOS
                            # mouse.position = (1084, 520)
                            # 5MINUTOS
                            mouse.position = (1084, 540)
                            mouse.click(Button.left, 1)
                            sleep(1.5)
                            # APUESTA SUBE
                            # mouse.position = (1311, 601)
                            # APUESTA BAJA
                            mouse.position = (1314, 672)
                            sleep(0.5)
                            mouse.click(Button.left, 1)
                            sleep(0.5)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\Tabla5m.csv', index=False, header=True)