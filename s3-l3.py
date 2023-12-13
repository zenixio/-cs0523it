
# Traccia: Si scriva un programma in Python che in base alla scelta dell’utente permetta di calcolare il 
# perimetro di diverse figure geometriche (scegliete pure quelle che volete voi). 
# Per la risoluzione dell’esercizio abbiamo scelto: 
# ● Quadrato (perimetro = lato*4). 
# ● Cerchio (circonferenza = 2*pi greco*r). 
# ● Rettangolo (perimetro= base*2 + altezza*2).

import math
pi = math.pi


def strToFloat(str1, var, str2=-1):
    try: 
        val1 = float(str1)
        val2 = None
        if(str2 != -1):
            val2 = float(str2)
        if(val2 != None):
            var(val1,val2)
        else:
            var(val1)
    except Exception as _: 
        print(_, "\n")
        print("Il valore inserito deve essere un numero")


def perimetroQuadrato(lato):
    p = lato * 4
    print("Il perimetro del quadrato è : ", p)

def perimetroCerchio(r):
    p = 2 * pi * r
    print("Il perimetro del cerchio è : ", p)

def perimetroRettangolo(b,a):
    p = (b*2) + (a*2)
    print("Il perimetro del rettangolo è : ", p)

def main():
    print("Scegliere il tipo di figura geometrica per la quale\nsi desidera calcolare il perimetro : \n")
    print("A - QUADRATO | B - CERCHIO | C - RETTANGOLO \n")

    choiche = input("Digitare l\'opzione A , B o C : ")

    if(choiche.lower() == "a" or choiche == 'A'):
        print("Hai scelto l'opzione A che corrisponde al QUADRATO\n")
        lato = input("Inserire ora la lunghezza del lato (cm) per calcolare il perimetro : ")
        strToFloat(lato,perimetroQuadrato)
    elif(choiche.lower() == "b" or choiche == 'B'):
        print("Hai scelto l'opzione B che corrisponde al CERCHIO\n")
        r = input("Inserire ora la lunghezza del raggio (cm) per calcolare il perimetro : ")
        strToFloat(r,perimetroCerchio)
    elif(choiche.lower() == "c" or choiche == 'C'):
        print("Hai scelto l'opzione B che corrisponde al RETTANGOLO\n")
        b = input("Inserire ora la lunghezza della base (cm) per calcolare il perimetro : ")
        a = input("Inserire ora la lunghezza dell'altezza (cm) per calcolare il perimetro : ")
        strToFloat(a,perimetroRettangolo,b)
    else: 
        print("Si prega di digitare A o B o C\n")


    again = input("Digitare 1 per continuare oppure 0 per uscire : ")

    try:
        if(int(again) == 1):
            main()
        else:
            print("Grazie per aver utilizzato il nostro programma")
    except:
        print("Valore non valido")


main()



    
