import requests
import time
from CreoTablas import Tablas
from DatosInicial import DatosIn1
from Creorangos1 import analisis
from AnalisisRSI import AnalisisRSI
from AnalisisEsto import AnalisisEsto
from AnalisisMACD import AnalisisMACD
from AnalisisRSI import AnalisisRSIW
from AnalisisEsto import AnalisisEstoW
from AnalisisMACD import AnalisisMACDW
from AnalisisRSI1 import AnalisisRSI1
from AnalisisEsto1 import AnalisisEsto1
from AnalisisMACD1 import AnalisisMACD1
from AnalisisRSI1 import AnalisisRSI1W
from AnalisisEsto1 import AnalisisEsto1W
from AnalisisMACD1 import AnalisisMACD1W
from Combinado1 import Analisiscombinado1
from Combinado1 import Analisiscombinado1W
from Combinado2 import Analisiscombinado2
from Combinado2 import Analisiscombinado2W
from Combinado3 import Analisiscombinado3
from Combinado3 import Analisiscombinado3W
from AnalisisENTIEMPOREAL import Tiemporeal
from ANALISISDATOS import analisis2
from Convinaciones import creoconvinaciones
from AnalisisIMDM import AnalisisIMDM
from AnalisisICPB import AnalisisICPB
from AnalisisOA import AnalisisOA
from AnalisisIMDM import AnalisisIMDMW
from AnalisisICPB import AnalisisICPBW
from AnalisisOA import AnalisisOAW
from AnalisisIMDM1 import AnalisisIMDM1
from AnalisisICPB1 import AnalisisICPB1
from AnalisisOA1 import AnalisisOA1
from AnalisisIMDM1 import AnalisisIMDMW1
from AnalisisICPB1 import AnalisisICPBW1
from AnalisisOA1 import AnalisisOAW1
from AnalisisRSIR import AnalisisRSIR
from AnalisisWilliams import AnalisisWilliams
from AnalisisOU import AnalisisOU
from AnalisisRSIR import AnalisisRSIRW
from AnalisisWilliams import AnalisisWilliamsW
from AnalisisOU import AnalisisOUW
from AnalisisRSIR1 import AnalisisRSIR1
from AnalisisWilliams1 import AnalisisWilliams1
from AnalisisOU1 import AnalisisOU1
from AnalisisRSIR1 import AnalisisRSIRW1
from AnalisisWilliams1 import AnalisisWilliamsW1
from AnalisisOU1 import AnalisisOUW1


#ENVIO HORA DE COMIENZO

hora = time.strftime("%H.%M.%S")
requests.post('https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',data={'chat_id': '1214441101', 'text': hora})

analisis()

AnalisisRSI()

AnalisisRSI1()

AnalisisEsto()

AnalisisEsto1()

AnalisisMACD()

AnalisisMACD1()

AnalisisIMDM()

AnalisisIMDM1()

AnalisisICPB()

AnalisisICPB1()

AnalisisOA()

AnalisisOA1()

AnalisisRSIR()

AnalisisRSIR1()

AnalisisWilliams()

AnalisisWilliams1()

AnalisisOU()

AnalisisOU1()

Analisiscombinado1()

Analisiscombinado2()

Analisiscombinado3()


a=2
while a>1:

    Tiemporeal()

    analisis2()

    creoconvinaciones()

    AnalisisRSIW()

    AnalisisRSI1W()

    AnalisisEstoW()

    AnalisisEsto1W()

    AnalisisMACDW()

    AnalisisMACD1W()

    AnalisisIMDMW()

    AnalisisIMDMW1()

    AnalisisICPBW()

    AnalisisICPBW1()

    AnalisisOAW()

    AnalisisOAW1()

    AnalisisRSIRW()

    AnalisisRSIRW1()

    AnalisisWilliamsW()

    AnalisisWilliamsW1()

    AnalisisOUW()

    AnalisisOUW1()

    Analisiscombinado1W()

    Analisiscombinado2W()

    Analisiscombinado3W()

    hora = time.strftime("%H:%M")

    j = str(hora)
    b = 'Tablas Actualizadas: '  + j
    requests.post('https://api.telegram.org/bot1045875495:AAEp5RBtZ1Oi5E7KcrasZ0UybcICE8rpSOk/sendMessage',
                  data={'chat_id': '1214441101', 'text': b})

