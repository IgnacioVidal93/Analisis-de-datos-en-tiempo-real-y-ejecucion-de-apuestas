import pandas
import numpy

def analisis():

    tabla = pandas.read_csv("Tabla5m.csv")

    Largo = tabla.shape[0]

    maximoRSI = float(numpy.nanmax(tabla.iloc[2:-1, 2].values))
    minimoRSI = float(numpy.nanmin(tabla.iloc[2:-1, 2].values))

    MitadRSI = (maximoRSI + minimoRSI) / 2
    PcuartoRSI = (MitadRSI + minimoRSI) / 2
    TcuartoRSI = (MitadRSI + maximoRSI) / 2
    PoctavoRSI = (minimoRSI + PcuartoRSI) / 2
    ToctavoRSI = (PcuartoRSI + MitadRSI) / 2
    QoctavoRSI = (MitadRSI + TcuartoRSI) / 2
    SoctavoRSI = (TcuartoRSI + maximoRSI) / 2

    # PARA ESTOCASTICO

    maximoESTOCASTICO = float(numpy.nanmax(tabla.iloc[2:-1, 4].values))
    minimoESTOCASTICO = float(numpy.nanmin(tabla.iloc[2:-1, 4].values))

    MitadESTOCASTICO = (maximoESTOCASTICO + minimoESTOCASTICO) / 2
    PcuartoESTOCASTICO = (MitadESTOCASTICO + minimoESTOCASTICO) / 2
    TcuartoESTOCASTICO = (MitadESTOCASTICO + maximoESTOCASTICO) / 2
    PoctavoESTOCASTICO = (minimoESTOCASTICO + PcuartoESTOCASTICO) / 2
    ToctavoESTOCASTICO = (PcuartoESTOCASTICO + MitadESTOCASTICO) / 2
    QoctavoESTOCASTICO = (MitadESTOCASTICO + TcuartoESTOCASTICO) / 2
    SoctavoESTOCASTICO = (TcuartoESTOCASTICO + maximoESTOCASTICO) / 2

    # PARA MACD

    maximoMACD = float(numpy.nanmax(tabla.iloc[2:-1, 6].values))
    minimoMACD = float(numpy.nanmin(tabla.iloc[2:-1, 6].values))

    MitadMACD = (maximoMACD + minimoMACD) / 2
    PcuartoMACD = (MitadMACD + minimoMACD) / 2
    TcuartoMACD = (MitadMACD + maximoMACD) / 2
    PoctavoMACD = (minimoMACD + PcuartoMACD) / 2
    ToctavoMACD = (PcuartoMACD + MitadMACD) / 2
    QoctavoMACD = (MitadMACD + TcuartoMACD) / 2
    SoctavoMACD = (TcuartoMACD + maximoMACD) / 2

    # Rango pendiente RSI

    # PARA Pendiente

    maximoRSIPP = float(numpy.nanmax(tabla.iloc[2:-1, 3].values))
    minimoRSIPP = 0
    maximoRSIPN = 0
    minimoRSIPN = float(numpy.nanmin(tabla.iloc[2:-1, 3].values))

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

    # Para pendiente

    maximoESTOCASTICOPP = float(numpy.nanmax(tabla.iloc[2:-1, 5].values))
    minimoESTOCASTICOPP = 0
    maximoESTOCASTICOPN = 0
    minimoESTOCASTICOPN = float(numpy.nanmin(tabla.iloc[2:-1, 5].values))

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

    # PARA PENDIENTE

    maximoMACDPP = float(numpy.nanmax(tabla.iloc[2:-1, 7].values))
    minimoMACDPP = 0
    maximoMACDPN = 0
    minimoMACDPN = float(numpy.nanmin(tabla.iloc[2:-1, 7].values))

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

    maximoICPB = float(numpy.nanmax(tabla.iloc[2:-1, 10].values))
    minimoICPB = float(numpy.nanmin(tabla.iloc[2:-1, 10].values))

    MitadICPB = (maximoICPB + minimoICPB) / 2
    PcuartoICPB = (MitadICPB + minimoICPB) / 2
    TcuartoICPB = (MitadICPB + maximoICPB) / 2
    PoctavoICPB = (minimoICPB + PcuartoICPB) / 2
    ToctavoICPB = (PcuartoICPB + MitadICPB) / 2
    QoctavoICPB = (MitadICPB + TcuartoICPB) / 2
    SoctavoICPB = (TcuartoICPB + maximoICPB) / 2

    # PARA Pendiente

    maximoICPBPP = float(numpy.nanmax(tabla.iloc[2:-1, 11].values))
    minimoICPBPP = 0
    maximoICPBPN = 0
    minimoICPBPN = float(numpy.nanmin(tabla.iloc[2:-1, 11].values))

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

    maximoIMDM = float(numpy.nanmax(tabla.iloc[2:-1, 8].values))
    minimoIMDM = float(numpy.nanmin(tabla.iloc[2:-1, 8].values))

    MitadIMDM = (maximoIMDM + minimoIMDM) / 2
    PcuartoIMDM = (MitadIMDM + minimoIMDM) / 2
    TcuartoIMDM = (MitadIMDM + maximoIMDM) / 2
    PoctavoIMDM = (minimoIMDM + PcuartoIMDM) / 2
    ToctavoIMDM = (PcuartoIMDM + MitadIMDM) / 2
    QoctavoIMDM = (MitadIMDM + TcuartoIMDM) / 2
    SoctavoIMDM = (TcuartoIMDM + maximoIMDM) / 2

    # PARA Pendiente

    maximoIMDMPP = float(numpy.nanmax(tabla.iloc[2:-1, 9].values))
    minimoIMDMPP = 0
    maximoIMDMPN = 0
    minimoIMDMPN = float(numpy.nanmin(tabla.iloc[2:-1, 9].values))

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

    maximoOA = float(numpy.nanmax(tabla.iloc[2:-1, 12].values))
    minimoOA = float(numpy.nanmin(tabla.iloc[2:-1, 12].values))

    MitadOA = (maximoOA + minimoOA) / 2
    PcuartoOA = (MitadOA + minimoOA) / 2
    TcuartoOA = (MitadOA + maximoOA) / 2
    PoctavoOA = (minimoOA + PcuartoOA) / 2
    ToctavoOA = (PcuartoOA + MitadOA) / 2
    QoctavoOA = (MitadOA + TcuartoOA) / 2
    SoctavoOA = (TcuartoOA + maximoOA) / 2

    #PARA Pendiente

    maximoOAPP = float(numpy.nanmax(tabla.iloc[2:-1, 13].values))
    minimoOAPP = 0
    maximoOAPN = 0
    minimoOAPN = float(numpy.nanmin(tabla.iloc[2:-1, 13].values))

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

    maximoRSIR = float(numpy.nanmax(tabla.iloc[2:-1, 14].values))
    minimoRSIR = float(numpy.nanmin(tabla.iloc[2:-1, 14].values))

    MitadRSIR = (maximoRSIR + minimoRSIR) / 2
    PcuartoRSIR = (MitadRSIR + minimoRSIR) / 2
    TcuartoRSIR = (MitadRSIR + maximoRSIR) / 2
    PoctavoRSIR = (minimoRSIR + PcuartoRSIR) / 2
    ToctavoRSIR = (PcuartoRSIR + MitadRSIR) / 2
    QoctavoRSIR = (MitadRSIR + TcuartoRSIR) / 2
    SoctavoRSIR = (TcuartoRSIR + maximoRSIR) / 2

    # PARA Pendiente

    maximoRSIRPP = float(numpy.nanmax(tabla.iloc[2:-1, 15].values))
    minimoRSIRPP = 0
    maximoRSIRPN = 0
    minimoRSIRPN = float(numpy.nanmin(tabla.iloc[2:-1, 15].values))

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

    maximoWilliams = float(numpy.nanmax(tabla.iloc[2:-1, 16].values))
    minimoWilliams = float(numpy.nanmin(tabla.iloc[2:-1, 16].values))

    MitadWilliams = (maximoWilliams + minimoWilliams) / 2
    PcuartoWilliams = (MitadWilliams + minimoWilliams) / 2
    TcuartoWilliams = (MitadWilliams + maximoWilliams) / 2
    PoctavoWilliams = (minimoWilliams + PcuartoWilliams) / 2
    ToctavoWilliams = (PcuartoWilliams + MitadWilliams) / 2
    QoctavoWilliams = (MitadWilliams + TcuartoWilliams) / 2
    SoctavoWilliams = (TcuartoWilliams + maximoWilliams) / 2

    # PARA Pendiente

    maximoWilliamsPP = float(numpy.nanmax(tabla.iloc[2:-1, 17].values))
    minimoWilliamsPP = 0
    maximoWilliamsPN = 0
    minimoWilliamsPN = float(numpy.nanmin(tabla.iloc[2:-1, 17].values))

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

    maximoOU = float(numpy.nanmax(tabla.iloc[2:-1, 18].values))
    minimoOU = float(numpy.nanmin(tabla.iloc[2:-1, 18].values))

    MitadOU = (maximoOU + minimoOU) / 2
    PcuartoOU = (MitadOU + minimoOU) / 2
    TcuartoOU = (MitadOU + maximoOU) / 2
    PoctavoOU = (minimoOU + PcuartoOU) / 2
    ToctavoOU = (PcuartoOU + MitadOU) / 2
    QoctavoOU = (MitadOU + TcuartoOU) / 2
    SoctavoOU = (TcuartoOU + maximoOU) / 2

    # PARA Pendiente

    maximoOUPP = float(numpy.nanmax(tabla.iloc[2:-1, 19].values))
    minimoOUPP = 0
    maximoOUPN = 0
    minimoOUPN = float(numpy.nanmin(tabla.iloc[2:-1, 19].values))

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







    TablaDatos5m = tabla

    tabla = TablaDatos5m
    Largo = tabla.shape[0]

    while (Largo > 11):

        Largo -= 1
        precioactual = float(tabla.iloc[Largo, 0])
        precioanterior = float(tabla.iloc[Largo - 9, 0])
        if precioactual > precioanterior:
            tabla.iat[Largo - 9, 1] = 1
        if precioactual < precioanterior:
            tabla.iat[Largo - 9, 1] = 2
        if precioactual == precioanterior:
            tabla.iat[Largo - 9, 1] = 0

        # para 1.5 m
        precioactual = float(tabla.iloc[Largo, 0])
        precioanterior = float(tabla.iloc[Largo - 4, 0])
        if precioactual > precioanterior:
            tabla.iat[Largo - 4, 22] = 1
        if precioactual < precioanterior:
            tabla.iat[Largo - 4, 22] = 2
        if precioactual == precioanterior:
            tabla.iat[Largo - 4, 22] = 0
        # para 2.5m
        precioactual = float(tabla.iloc[Largo, 0])
        precioanterior = float(tabla.iloc[Largo - 6, 0])
        if precioactual > precioanterior:
            tabla.iat[Largo - 6, 23] = 1
        if precioactual < precioanterior:
            tabla.iat[Largo - 6, 23] = 2
        if precioactual == precioanterior:
            tabla.iat[Largo - 6, 23] = 0
        # para 3.5m
        precioactual = float(tabla.iloc[Largo, 0])
        precioanterior = float(tabla.iloc[Largo - 8, 0])
        if precioactual > precioanterior:
            tabla.iat[Largo - 8, 24] = 1
        if precioactual < precioanterior:
            tabla.iat[Largo - 8, 24] = 2
        if precioactual == precioanterior:
            tabla.iat[Largo - 8, 24] = 0
        # para 4.5m
        precioactual = float(tabla.iloc[Largo, 0])
        precioanterior = float(tabla.iloc[Largo - 10, 0])
        if precioactual > precioanterior:
            tabla.iat[Largo - 10, 25] = 1
        if precioactual < precioanterior:
            tabla.iat[Largo - 10, 25] = 2
        if precioactual == precioanterior:
            tabla.iat[Largo - 10, 25] = 0



    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\Tabla5m.csv', index=False, header=True)

    TablaDatos5m = tabla
    tabla = TablaDatos5m
    Largo = tabla.shape[0]
    Largo = Largo - 11
    tablaleida5M= pandas.read_csv("TablaLeida5m.csv")


    while (Largo > 3):

        Largo -= 1
        DatoRSI = float(tabla.iat[Largo, 2])
        DatoRSIP = float(tabla.iat[Largo, 3])
        DatoESTOCASTICO = float(tabla.iat[Largo, 4])
        DatoESTOCASTICOP = float(tabla.iat[Largo, 5])
        DatoMACD = float(tabla.iat[Largo, 6])
        DatoMACDP = float(tabla.iat[Largo, 7])
        DatoIMDM = float(tabla.iat[Largo, 8])
        DatoIMDMP = float(tabla.iat[Largo, 9])
        DatoICPB = float(tabla.iat[Largo, 10])
        DatoICPBP = float(tabla.iat[Largo, 11])
        DatoOA = float(tabla.iat[Largo, 12])
        DatoOAP = float(tabla.iat[Largo, 13])
        DatoRSIR = float(tabla.iat[Largo, 14])
        DatoRSIRP = float(tabla.iat[Largo, 15])
        DatoWilliams = float(tabla.iat[Largo, 16])
        DatoWilliamsP = float(tabla.iat[Largo, 17])
        DatoOU = float(tabla.iat[Largo, 18])
        DatoOUP = float(tabla.iat[Largo, 19])

        DatoVolumenP = float(tabla.iat[Largo, 22])

        Hora = tabla.iat[Largo, 20]
        Dato5m = tabla.iat[Largo, 1]
        Dato3m = tabla.iat[Largo, 22]
        Dato35m = tabla.iat[Largo, 23]
        Dato4m = tabla.iat[Largo, 24]
        Dato45m = tabla.iat[Largo, 25]

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


        Datos5m = {'1': Dato5m, '2': MRSI, '3': MRSIP, '4': MESTOCASTICO, '5': MESTOCASTICOP, '6': MMACD, '7': MMACDP,'8': MIMDM, '9': MIMDMP, '10': MICPB, '11': MICPBP, '12': MOA, '13': MOAP,'14': MRSIR, '15': MRSIRP, '16': MWilliams, '17': MWilliamsP, '18': MOU, '19': MOUP,
                   '20': MVOLP,'21': MVOLP, '22': Hora, '23': Dato3m, '24': Dato35m, '25': Dato4m, '26': Dato45m}
        tablaleida5M = tablaleida5M.append(Datos5m, ignore_index=True)
    tablaleida5M.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\TablaLeida5m.csv', index=False, header=True)

