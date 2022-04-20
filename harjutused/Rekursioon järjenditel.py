def loenda(järjend, element):

    # tühjas järjendis ei saa seda elementi esineda
    # see on rekursiooni baas
    if len(järjend) == 0:
        return 0
    else:
        # rekursiooni samm
        # järjendi päiseks nimetame tema esimest elementi
        päis = järjend[0]
        # sabaks nimetame kõike seda, mis tuleb peale esimest elementi
        saba = järjend[1:]

        # kasutame sama funktsiooni rekursiivselt järjendi sabal ...
        elementide_arv_sabas = loenda(saba, element)

        # ... ja kombineerime saadud tulemuse päisest saadud infoga
        if päis == element:
            return elementide_arv_sabas + 1
        else:
            return elementide_arv_sabas


print(loenda("kukesupp", "u"))
#print(loenda("kukesupp", "p"))
#print(loenda("kukesupp", "r"))
#print(loenda([1,2,3,2,2], 2))
#print(loenda([1,2,3,2,2], 8))