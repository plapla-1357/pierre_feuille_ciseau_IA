from random import*
from ast import*



def save(data):
    DATA = str(f"{data}")
    Save = open("data.txt","w")
    Save.write(DATA)
    Save.close()

def lire_data():
    donner= open("data.txt", "r")
    data = donner.read()
    print(data)
    print(type(data))
    data = literal_eval(data)
    print(data)
    print(type(data))



data = [["p","f","p","c"], ["p","f","p","c"]]
list_en_cours = []


save(data)
lire_data()