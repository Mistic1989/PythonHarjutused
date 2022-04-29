import os.path

def kuva_failid(kaust):
    # os.listdir annab etteantud kaustas olevate failide ja kaustade nimed
    # (sõnede listina)
    nimekiri = list()
    for nimi in os.listdir(kaust):
        # os.path.join paneb kausta nime ja faili nime
        # kokku täisnimeks (vastavalt platvormi reeglitele kas / või \-ga)
        täisnimi = os.path.join(kaust, nimi)

        # os.path.isdir ütleb, kas tegemist on kaustaga
        if os.path.isdir(täisnimi):
            nimekiri = nimekiri + kuva_failid(täisnimi)
        else:
            nimekiri.append(täisnimi)

# Asenda Peeter enda kasutajanimega
print(kuva_failid("C:\\php")) # Mac'i ja Linuxi korral "~/Peeter"

