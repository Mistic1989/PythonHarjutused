import os.path

def kuva_failid(kaust):
    failid = list()
    nimekiri = list()
    for item in os.listdir(kaust):
        fullpath = os.path.join(kaust, item)
        #print(os.path.basename(fullpath))
        if os.path.isdir(fullpath):
                failid = failid + kuva_failid(fullpath)
                nimekiri.append(failid)
                #print(failid)
        else:
                nimekiri.append(item)

    return nimekiri

print(kuva_failid('c:\\python27'))