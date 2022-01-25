import pandas

def Analisiscombinado1():

    tablaleida5M = pandas.read_csv("TablaLeida5m.csv")
    tabla = tablaleida5M
    Largo = tabla.shape[0]
    tablaC1= pandas.read_csv("convinaciones1.csv")

    while (Largo > 2):
        Largo -= 1
        RSI = float(tabla.iat[Largo, 1])
        Esto = float(tabla.iat[Largo, 3])
        MACD = float(tabla.iat[Largo, 5])


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
                    if RSI == r and Esto == e and MACD == m:

                        a = tablaC1.iat[K, 1]
                        b = float(a)
                        c = b + 1
                        tablaC1.iat[K, 1] = c

                        Acierto=2
                        Porsentaje=3
                        Dato=9
                        while Acierto < 11:

                            Dato5 = float(tabla.iat[Largo, Dato])
                            if Dato5 == 1:
                                a1 = tablaC1.iat[K, Acierto]
                                b1 = float(a1)
                                c1 = b1 + 1
                                tablaC1.iat[K, Acierto] = c1
                            p=tablaC1.iat[K, Acierto]
                            p1=float(p)
                            d=p1*100/c
                            tablaC1.iat[K, Porsentaje] = d
                            Acierto += 2
                            Porsentaje += 2
                            Dato += 1




    tablaC1.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinaciones1.csv', index=False, header=True)


def Analisiscombinado1W():

    f=0
    tablaleida5M = pandas.read_csv("TablaLeida5m.csv")
    tabla = tablaleida5M
    Largo = tabla.shape[0]
    tablaC1= pandas.read_csv("convinaciones1.csv")

    while (Largo > 2 and f<120):
        f+=1
        Largo -= 1
        RSI = float(tabla.iat[Largo, 1])
        Esto = float(tabla.iat[Largo, 3])
        MACD = float(tabla.iat[Largo, 5])


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
                    if RSI == r and Esto == e and MACD == m:
                        a = tablaC1.iat[K, 1]
                        b = float(a)
                        c = b + 1
                        tablaC1.iat[K, 1] = c

                        Acierto = 2
                        Porsentaje = 3
                        Dato = 9
                        while Acierto < 11:

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



    tablaC1.to_csv(r'C:\Users\Nacho\Desktop\Desarrollos\VamosQueSale\convinaciones1.csv', index=False, header=True)
