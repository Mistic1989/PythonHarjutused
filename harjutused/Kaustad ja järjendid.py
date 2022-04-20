import os.path

def kuva_failid(kaust):
    # os.listdir annab etteantud kaustas olevate failide ja kaustade nimed
    # (sõnede listina)
    for nimi in os.listdir(kaust):
        # os.path.join paneb kausta nime ja faili nime
        # kokku täisnimeks (vastavalt platvormi reeglitele kas / või \-ga)
        täisnimi = os.path.join(kaust, nimi)

        # os.path.isdir ütleb, kas tegemist on kaustaga
        if os.path.isdir(täisnimi):
            print("Kaust", täisnimi)
        else:
            print("Fail", täisnimi)

# Asenda Peeter enda kasutajanimega
kuva_failid("C:\\Users\\Peeter") # Mac'i ja Linuxi korral "~/Peeter"


def liida(järjend):
    summa = 0
    for element in järjend:
        if isinstance(element, list):
            summa += liida(element)
        else:
            summa += element
    return summa

print(liida([1, [2, 3], [[[[4, 5], 6]]], 7, 8]))
print(liida([1, 2, 3, 4, 5, 6, 7, 8]))