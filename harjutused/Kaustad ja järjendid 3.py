import os

listdir = []
for root, dirs, files in os.walk('C:\php'):
    for filename in files:
        listdir.append(filename)

print(listdir)

