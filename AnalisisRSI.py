import pandas

def AnalisisRSI():

    tablaleida5M = pandas.read_csv("TablaLeida5m.csv")
    tabla = tablaleida5M
    Largo = tabla.shape[0]
    tablaRSI= pandas.read_csv("convinacionesRSI.csv")

    while (Largo > 2):
        Largo -= 1
        RSI = float(tabla.iat[Largo, 1])
        RSIP = float(tabla.iat[Largo, 2])
        VOLP = float(tabla.iat[Largo, 19])
        D1= RSI
        D2= RSIP

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
                    if D1 == r and D2 == e and VOLP == m:

                        a = tablaRSI.iat[K, 1]
                        b = float(a)
                        c = b + 1
                        tablaRSI.iat[K, 1] = c

                        Acierto = 2
                        Porsentaje = 3
                        Dato = 22
                        while Acierto < 9:

                            Dato5 = float(tabla.iat[Largo, Dato])
                            if Dato5 == 1:
                                a1 = tablaRSI.iat[K, Acierto]
                                b1 = float(a1)
                                c1 = b1 + 1
                                tablaRSI.iat[K, Acierto] = c1
                            p = tablaRSI.iat[K, Acierto]
                            p1 = float(p)
                            d = p1 * 100 / c
                            tablaRSI.iat[K, Porsentaje] = d
                            Acierto += 2
                            Porsentaje += 2
                            Dato += 1
    tablaRSI.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesRSI.csv', index=False, header=True)


def AnalisisRSIW():

    tablaleida5M = pandas.read_csv("TablaLeida5m.csv")
    tabla = tablaleida5M
    Largo = tabla.shape[0]
    tablaRSI= pandas.read_csv("convinacionesRSI.csv")
    f = 0

    while (Largo > 2 and f<120):
        f+=1
        Largo -= 1
        RSI = float(tabla.iat[Largo, 1])
        RSIP = float(tabla.iat[Largo, 2])
        VOLP = float(tabla.iat[Largo, 19])
        Dato = float(tabla.iat[Largo, 0])
        D1= RSI
        D2= RSIP

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
                    if D1 == r and D2 == e and VOLP == m:

                        a = tablaRSI.iat[K, 1]
                        b = float(a)
                        c = b + 1
                        tablaRSI.iat[K, 1] = c

                        Acierto = 2
                        Porsentaje = 3
                        Dato = 22
                        while Acierto < 9:

                            Dato5 = float(tabla.iat[Largo, Dato])
                            if Dato5 == 1:
                                a1 = tablaRSI.iat[K, Acierto]
                                b1 = float(a1)
                                c1 = b1 + 1
                                tablaRSI.iat[K, Acierto] = c1
                            p = tablaRSI.iat[K, Acierto]
                            p1 = float(p)
                            d = p1 * 100 / c
                            tablaRSI.iat[K, Porsentaje] = d
                            Acierto += 2
                            Porsentaje += 2
                            Dato += 1
    tablaRSI.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesRSI.csv', index=False, header=True)

