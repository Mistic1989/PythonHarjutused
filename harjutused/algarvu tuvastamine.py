n = int(input("Sisesta number: "))

for d in range(2, n):
    print(d)
    if (n / d) % 1 == 0:
        print("Ei ole algarv")
        break
else:
    print("On algarv")