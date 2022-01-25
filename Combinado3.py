import pandas

def Analisiscombinado3():

    tablaleida5M = pandas.read_csv("TablaLeida5m.csv")
    tabla = tablaleida5M
    Largo = tabla.shape[0]
    tablaC3= pandas.read_csv("convinaciones3.csv")

    while (Largo > 2):
        Largo -= 1
        RSI = float(tabla.iat[Largo, 1])
        Esto = float(tabla.iat[Largo, 3])
        MACD = float(tabla.iat[Largo, 5])

        if RSI <3 and Esto <3 and MACD <3:

            a = tablaC3.iat[1, 1]
            b = float(a)
            c = b + 1
            tablaC3.iat[1, 1] = c

            Acierto = 2
            Porsentaje = 3
            Dato = 9

            while Acierto < 11:

                Dato5 = float(tabla.iat[Largo, Dato])
                if Dato5 == 1:

                    a1 = tablaC3.iat[1, Acierto]
                    b1 = float(a1)
                    c1 = b1 + 1
                    tablaC3.iat[1, Acierto] = c1
                p = tablaC3.iat[1, Acierto]
                p1 = float(p)
                d = p1 * 100 / c
                tablaC3.iat[1, Porsentaje] = d
                Acierto += 2
                Porsentaje += 2
                Dato += 1

        if RSI >6 and Esto >6 and MACD >6:

            a = tablaC3.iat[2, 1]
            b = float(a)
            c = b + 1
            tablaC3.iat[2, 1] = c

            Acierto = 2
            Porsentaje = 3
            Dato = 9
            while Acierto < 11:

                Dato5 = float(tabla.iat[Largo, Dato])
                if Dato5 == 1:
                    a1 = tablaC3.iat[2, Acierto]
                    b1 = float(a1)
                    c1 = b1 + 1
                    tablaC3.iat[2, Acierto] = c1
                p = tablaC3.iat[2, Acierto]
                p1 = float(p)
                d = p1 * 100 / c
                tablaC3.iat[2, Porsentaje] = d
                Acierto += 2
                Porsentaje += 2
                Dato += 1

    tablaC3.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinaciones3.csv', index=False, header=True)

def Analisiscombinado3W():

    tablaleida5M = pandas.read_csv("TablaLeida5m.csv")
    tabla = tablaleida5M
    Largo = tabla.shape[0]
    tablaC3= pandas.read_csv("convinaciones3.csv")
    f = 0

    while (Largo > 2 and f<120):
        f+=1
        Largo -= 1
        RSI = float(tabla.iat[Largo, 1])
        Esto = float(tabla.iat[Largo, 3])
        MACD = float(tabla.iat[Largo, 5])

        if RSI < 3 and Esto < 3 and MACD < 3:

            a = tablaC3.iat[1, 1]
            b = float(a)
            c = b + 1
            tablaC3.iat[1, 1] = c

            Acierto = 2
            Porsentaje = 3
            Dato = 9
            while Acierto < 11:

                Dato5 = float(tabla.iat[Largo, Dato])
                if Dato5 == 1:
                    a1 = tablaC3.iat[1, Acierto]
                    b1 = float(a1)
                    c1 = b1 + 1
                    tablaC3.iat[1, Acierto] = c1
                p = tablaC3.iat[1, Acierto]
                p1 = float(p)
                d = p1 * 100 / c
                tablaC3.iat[1, Porsentaje] = d
                Acierto += 2
                Porsentaje += 2
                Dato += 1

        if RSI > 6 and Esto > 6 and MACD > 6:

            a = tablaC3.iat[2, 1]
            b = float(a)
            c = b + 1
            tablaC3.iat[2, 1] = c

            Acierto = 2
            Porsentaje = 3
            Dato = 9
            while Acierto < 11:

                Dato5 = float(tabla.iat[Largo, Dato])
                if Dato5 == 1:
                    a1 = tablaC3.iat[2, Acierto]
                    b1 = float(a1)
                    c1 = b1 + 1
                    tablaC3.iat[2, Acierto] = c1
                p = tablaC3.iat[2, Acierto]
                p1 = float(p)
                d = p1 * 100 / c
                tablaC3.iat[2, Porsentaje] = d
                Acierto += 2
                Porsentaje += 2
                Dato += 1

    tablaC3.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinaciones3.csv', index=False, header=True)
