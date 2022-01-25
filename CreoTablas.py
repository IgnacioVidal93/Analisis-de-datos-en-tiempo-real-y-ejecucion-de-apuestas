import pandas

def Tablas():
    Columnas = {'1': ['Precio'], '2': ['Mayor o Menor 5m'],  '3': ['RSI'], '4': ['Pendiente RSI'],
                '5': ['Oscilador Estocastico'], '6': ['Pendiente Oscilador Estocastico'], '7': ['Nivel MACD'],
                '8': ['Pendiente Nivel MACD'], '9': ['IMDM'], '10': ['Pendiente IMDM'],
                '11': ['ICPB'], '12': ['Pendiente ICPB'], '13': ['OA'],
                '14': ['Pendiente OA'], '15': ['RSIR'], '16': ['Pendiente RSIR'],
                '17': ['Williamso'], '18': ['Pendiente Williams'], '19': ['OU'],
                '20': ['Pendiente OU'],'21': ['Hora'], '22': ['Volumen'] , '23': ['Volumen Pendiente'] , '24': ['Mayor o Menor 1.5m'], '25': ['Mayor o Menor 2.5m'], '26': ['Mayor o Menor 3.5m'], '27': ['Mayor o Menor 4.5m']}

    Columnas2 = {'1': ['5M'], '2': ['RSI'], '3': ['Aceleracion RSI'], '4': ['Oscilador Estocastico'],
                 '5': ['Aceleracion de Oscilador Estocastico'], '6': ['Nivel MACD'], '7': ['Aceleracion de Nivel MACD'], '8': ['IMDM'], '9': ['Aceleracion IMDM'], '10': ['ICBP'],
                 '11': ['Aceleracion de ICBP'], '12': ['OA'], '13': ['Aceleracion de OA'],'14': ['RSIR'], '15': ['Aceleracion RSIR'], '16': ['Williams'],
                 '17': ['Aceleracion de Williams'], '18': ['OU'], '19': ['Aceleracion de OU'], '20': ['Volumen '], '21': ['Volumen Pendiente'], '22': ['Hora'], '23': ['Mayor o Menor 1.5m'], '24': ['Mayor o Menor 2.5m'], '25': ['Mayor o Menor 3.5m'], '26': ['Mayor o Menor 4.5m']}

    # PORSENTAJES  Columnas3 =  {'1' : ['Precio'],  '2' : ['Mayor o Menor 5m'], '3' : ['RSI'],'4' : ['Pendiente RSI'], '5' : ['Oscilador Estocastico'],'6' : ['Pendiente Oscilador Estocastico'], '7' : ['Nivel MACD'], '8' : ['Pendiente Nivel MACD'], '9' : ['Hora'] }

    # Tabla con indicadores a 5 minutos

    TablaDatos5m = pandas.DataFrame(Columnas)

    # Tabla con datos analizados  a 5 minuto

    tablaleida5M = pandas.DataFrame(Columnas2)

    # Tabla con porsentajes

    # porsentajes5M= pandas.DataFrame(Columnas3)

    TablaDatos5m.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\Tabla5m.csv', index=False, header=True)
    tablaleida5M.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\TablaLeida5m.csv', index=False, header=True)
    # porsentajes5M.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\Porsentajes5m.csv', index= False, header= True)

    return
