from ast import*
from random import*

regle = {"pierre":"ciseaux", "ciseaux": "feuille", "feuille":"pierre"}
def gagnant_contre(qui):
    qqch = regle[qui]
    coup_a_jouer = regle[qqch]     # trouver le coup a jouer a partir du coup anticiper de l'adversaire
    return coup_a_jouer

def lire_data():
    donner= open("data.txt", "r")   # recuperer les donners save
    Data = donner.read()
    Data = literal_eval(Data)
    #print(data)
    return Data


data = lire_data()
 



def t1 ():
    p = 0
    f = 0
    c = 0                   #tour 1 le bot anticipe le coup le plus jouer au premier tour
    for i in data:
        c_j = i[0]
        if c_j[0] == "p":
            p = p +1
        elif c_j[0] == "f":
            f = f +1
        else:
            c = c+1 
    if p > f  and p > c:
        return gagnant_contre("pierre")
    elif f>p and f>c :
        return gagnant_contre("feuille")                     
    elif c>p and c>f :
        return gagnant_contre("ciseaux")
    else: 
        return choice(["pierre","feuille","ciseaux"])

def change_ap_defaite():  # stat si le joueur change de coup s'il perd
    change = 0 
    change_pas = 0
    for j in data:
        x = 0  
        for k in j[2]:                    
            if k == "d":   # si quand il pert
                c_j = j[0]
                if c_j[x] != c_j[x+1]:  # il change de coup 
                    change = change+1
                else:
                    change_pas = change_pas +1
            x = x+1
        tot = change + change_pas
        if change > tot*2/3 :
            return "change"
        else:
            return "change_pas"



    # le but est de trouver les premier coup qui reviennent souvent


