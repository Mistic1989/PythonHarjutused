from turtle import *

def fraktal(tase, pikkus) :
    #print("Funktsioon hakkab otsast peale")
    if tase >= 1 :
        print("Funktsioon hakkab otsast peale")
        #print(tase)
        forward(pikkus)
        print("Liikumine edasi")
        left(90)
        fraktal(tase-1, pikkus * 0.7) #tase on nüüd 2, pikkus poole lühem, algab otsast peale
        print("Esimene rekursiooni funktsioon lõppenud")
        print(tase)
        right(180)
        print("Keeratud 180 kraadi")
        fraktal(tase-1, pikkus * 0.7)
        print("Teine rekursiooni funktsioon lõppenud")
        left(90)
        print("Pööre vasakule 90 kraadi lõpetatud")
        backward(pikkus)
        print("Suund tagasi")

left(90)
fraktal(5, 100)
exitonclick()



