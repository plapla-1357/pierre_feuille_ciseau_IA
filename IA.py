from ast import*
from random import*

coup_pos = ["pierre","feuille","ciseaux"]
regle = {"pierre":"ciseaux", "ciseaux": "feuille", "feuille":"pierre"}
joueur = input("quelle est votre nom: ") 
#def qui_joue():
    #return joueur    # ca permet au deux code de connaitre le nom de joueur 
    # le nom de joueur permet de savoir dans quelle fichier sauvagarder ses donner :  ce sera un fivier comme  
    #   prenom.txt      mais on change le prenom par le vrai prenom du joueur
    # tout cela va permetre de save des data relative a chaque joueur qui y jouent
    

def gagnant_contre(qui):
    qqch = regle[qui]
    coup_a_jouer = regle[qqch]     # trouver le coup a jouer a partir du coup anticiper de l'adversaire
    return coup_a_jouer

def save(data):
    DATA = str(f"{data}")
    Save = open(f"{joueur}.txt","w")   # sauvgarder les data dans data.txt
    Save.write(DATA)
    Save.close()

def lire_data():
    donner= open(f"{joueur}.txt", "r")   # recuperer les donners save
    Data = donner.read()
    Data = literal_eval(Data)
    #print(data)
    return Data


first_game = False
try:
    data = lire_data()
except:
    save("[]")
    first_game = True
    data = lire_data()



def t1 ():  # le but est de trouver les premier coup qui reviennent souvent
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
                if x<8 and c_j[x] != c_j[x+1]:  # il change de coup 
                    change = change+1
                else:
                    change_pas = change_pas +1
            x = x+1
    tot = change + change_pas
    try:
        return int((change/tot) *100)
    except ZeroDivisionError:
        return None

def change_ap_vict():  # stat si le joueur change de coup s'il gagne
    change = 0 
    change_pas = 0
    for j in data:
        x = 0  
        for k in j[2]:                    
            if k == "v":   # si quand il pert
                c_j = j[0]
                if x<8 and c_j[x] != c_j[x+1]:  # il change de coup 
                    change = change+1
                else:
                    change_pas = change_pas +1
            x = x+1
    tot = change + change_pas
    try:
        return int((change/tot) *100)
    except ZeroDivisionError:
        return None

def change_ap_ega():  # stat si le joueur change de coup s'il est egalite
    change = 0 
    change_pas = 0
    for j in data:
        x = 0  
        for k in j[2]:                    
            if k == "e":   # si quand il pert
                c_j = j[0]
                if x<8 and c_j[x] != c_j[x+1]:  # il change de coup 
                    change = change+1
                else:
                    change_pas = change_pas +1
            x = x+1
    tot = change + change_pas
    try:
        return int((change/tot) *100)
    except ZeroDivisionError:
        return None



#####------------- apres cette separation il y a les fonction pour ----  anticiper le coup -----

def coup_prevu(result,coup_av): coup_av est la varaible 
    coup = [] ## permet de faire le lien entre toutes les stats et anticiper le coup prevu par le joueur 
    if first_game == True :                   
        rd = choice(coup_pos)  
        p = 0
        f = 0
        c = 0
        return rd
    else :
        if result == "v":       
            if change_ap_vict <= 66 :
                if coup_av == "p":
                    p = p+((change_ap_vict-66)/10)
                elif coup_av == "f":
                    f = f+((change_ap_vict-66)/10)
                else:
                    c = c+((change_ap_vict-66)/10)


        # il faut return pierre feille ou ciseaux
        return coup   # ils faudra return le coup a jouer : gagnant_contre(qui)
    
  


