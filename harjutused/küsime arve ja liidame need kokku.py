s = 0
no = int(input("Kui palju numbreid sisestada?"))

for _ in range(no):
#while True:
    n = int(input("Sisesta arv: "))
    if n < 0:
        break
    s += n
    print(f"Summa on kokku: {s}")
    #if s >= 100:
    #    break
