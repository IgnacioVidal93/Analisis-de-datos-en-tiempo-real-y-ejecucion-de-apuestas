import pandas

def AnalisisIMDM():

    tablaleida5M = pandas.read_csv("TablaLeida5m.csv")
    tabla = tablaleida5M
    Largo = tabla.shape[0]
    tablaC1= pandas.read_csv("convinacionesIMDM.csv")

    while (Largo > 2):
        Largo -= 1
        MACD = float(tabla.iat[Largo, 7])
        MACDP = float(tabla.iat[Largo, 8])
        VOLP = float(tabla.iat[Largo, 19])

        D1= MACD
        D2= MACDP

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

                        a = tablaC1.iat[K, 1]
                        b = float(a)
                        c = b + 1
                        tablaC1.iat[K, 1] = c

                        Acierto = 2
                        Porsentaje = 3
                        Dato = 22
                        while Acierto < 9:

                            Dato5 = float(tabla.iat[Largo, Dato])
                            if Dato5 == 1:
                                a1 = tablaC1.iat[K, Acierto]
                                b1 = float(a1)
                                c1 = b1 + 1
                                tablaC1.iat[K, Acierto] = c1
                            p = tablaC1.iat[K, Acierto]
                            p1 = float(p)
                            d = p1 * 100 / c
                            tablaC1.iat[K, Porsentaje] = d
                            Acierto += 2
                            Porsentaje += 2
                            Dato += 1
    tablaC1.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesIMDM.csv', index=False, header=True)


def AnalisisIMDMW():

    tablaleida5M = pandas.read_csv("TablaLeida5m.csv")
    tabla = tablaleida5M
    Largo = tabla.shape[0]
    tablaC1= pandas.read_csv("convinacionesIMDM.csv")
    f = 0

    while (Largo > 2 and f<120):
        f+=1
        Largo -= 1
        MACD = float(tabla.iat[Largo, 7])
        MACDP = float(tabla.iat[Largo, 8])
        VOLP = float(tabla.iat[Largo, 19])

        D1= MACD
        D2= MACDP

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

                        a = tablaC1.iat[K, 1]
                        b = float(a)
                        c = b + 1
                        tablaC1.iat[K, 1] = c

                        Acierto = 2
                        Porsentaje = 3
                        Dato = 22
                        while Acierto < 9:

                            Dato5 = float(tabla.iat[Largo, Dato])
                            if Dato5 == 1:
                                a1 = tablaC1.iat[K, Acierto]
                                b1 = float(a1)
                                c1 = b1 + 1
                                tablaC1.iat[K, Acierto] = c1
                            p = tablaC1.iat[K, Acierto]
                            p1 = float(p)
                            d = p1 * 100 / c
                            tablaC1.iat[K, Porsentaje] = d
                            Acierto += 2
                            Porsentaje += 2
                            Dato += 1
    tablaC1.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinacionesIMDM.csv', index=False, header=True)
