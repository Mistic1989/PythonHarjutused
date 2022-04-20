def pikkus(jarjend):
    if not jarjend:
        return 0
    else:
        #print(jarjend)
        return 1 +  pikkus(jarjend[1:])
nimekiri = ["tere", "hommik", "kummik", "saabas"]
print(pikkus(nimekiri))