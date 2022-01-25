import pandas


def creoconvinaciones():


    Columnas = {'1': ['Valor'], '2': ['Salio'], '3': ['Acerto a 3 '], '4': ['porsentaje3'], '5': ['Acerto a 35 '], '6': ['porsentaje35'] ,'7': ['Acerto a 4 '], '8': ['porsentaje4'], '9': ['Acerto a 45 '], '10': ['porsentaje45'], '11': ['Acerto a 5 '], '12': ['porsentaje5']}

    Tablaconvinaciones1 = pandas.DataFrame(Columnas)

    tabla = Tablaconvinaciones1
    a = 0

    while a < 27:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinaciones1.csv', index=False, header=True)

    Tablaconvinaciones2 = pandas.DataFrame(Columnas)

    tabla = Tablaconvinaciones2
    a = 0

    while a < 27:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinaciones2.csv', index=False, header=True)

    Tablaconvinaciones3 = pandas.DataFrame(Columnas)

    tabla = Tablaconvinaciones3
    a = 0

    while a < 2:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinaciones3.csv', index=False, header=True)

    TablaconvinacionesRSI1 = pandas.DataFrame(Columnas)

    tabla = TablaconvinacionesRSI1
    a = 0

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesRSI1.csv', index=False, header=True)

    TablaconvinacionesEsto1 = pandas.DataFrame(Columnas)

    tabla = TablaconvinacionesEsto1
    a = 0

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesEsto1.csv', index=False, header=True)

    TablaconvinacionesMACD1 = pandas.DataFrame(Columnas)

    tabla = TablaconvinacionesMACD1
    a = 0

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesMACD1.csv', index=False, header=True)

    TablaconvinacionesRSI = pandas.DataFrame(Columnas)
    tabla = TablaconvinacionesRSI
    a = 0

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesRSI.csv', index=False, header=True)

    TablaconvinacionesEsto = pandas.DataFrame(Columnas)

    tabla = TablaconvinacionesEsto
    a = 0

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesEsto.csv', index=False, header=True)

    TablaconvinacionesMACD = pandas.DataFrame(Columnas)

    tabla = TablaconvinacionesMACD
    a = 0

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesMACD.csv', index=False, header=True)






    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesIMDM.csv', index=False, header=True)

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesIMDM1.csv', index=False, header=True)


    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesICPB.csv', index=False, header=True)


    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesICPB1.csv', index=False, header=True)

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesOA.csv', index=False, header=True)

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesOA1.csv', index=False, header=True)

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesRSIR.csv', index=False, header=True)

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesRSIR1.csv', index=False, header=True)

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesWilliams.csv', index=False, header=True)

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesWilliams1.csv', index=False, header=True)

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesOU.csv', index=False, header=True)

    while a < 24:
        a += 1
        Datos = {'1': a, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0, '10': 0, '11': 0, '12': 0}
        tabla = tabla.append(Datos, ignore_index=True)

    tabla.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesOU1.csv', index=False, header=True)


