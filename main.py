from random import*
from ast import*
import IA  # module IA.py permet de utiliser des stats sur les donner

regle = {"pierre":"ciseaux", "ciseaux": "feuille", "feuille":"pierre"}    # la pierrre bas le ciseaux qui bas la feuille qui bas la pierre
data = []
list_en_cours = []           #list qui servent a save les donner
list_coup_joueur = []
list_coup_bot = []
vict = []




def save(data):
    DATA = str(f"{data}")
    Save = open("data.txt","w")   # sauvgarder les data dans data.txt
    Save.write(DATA)
    Save.close()

def lire_data():
    donner= open("data.txt", "r")   # recuperer les donners save
    Data = donner.read()
    Data = literal_eval(Data)
    #print(data)
    return Data

def Round(coup_bot):  # deroulement d'un tour

    complete = False                   # mettre en forme le coup de joueur 
    while not complete :
        coup = input("quelle coup voulez vous jouer: ")
        if coup == "p":
            coup_ent ="pierre"
            complete =True
        elif coup == "f":                   #coup joueur
            coup_ent ="feuille"
            complete =True
        elif coup == "c":
            coup_ent = "ciseaux"
            complete = True
        else:
            print("vous vous n'avez pas donner une valeur attendu: pierre: p / feuille: f / ciseaux: c")
    list_coup_joueur.append(coup)
    
    



    if regle[coup_ent] == coup_bot:             # verifier qui a gagner
        print(f"{coup_ent} bas {coup_bot}")
        return "joueur"
    elif regle[coup_bot] == coup_ent :
        print(f"{coup_ent} pert contre {coup_bot}")
        return "bot"
    else:
        print(f"{coup_ent} et {coup_bot} sont egalité")
        return "egal"



#########
def f_coup_bot(i):
    if i == 1 :
        c_b = IA.t1()
        list_coup_bot.append(c_b[0])
        return c_b
    else:
        coup_pos = ["pierre","feuille","ciseaux"]   # cette fonction a pour but de choisir le coup du bot 
        rd = choice(coup_pos)                       # pour l'intant c'est aleatoir mais il faudras changer ca
        
        #print(rd)
        return rd
###################################################################################

            



# save(data)     # cette commande permet de sauvdarder les donners  (la variable data)


continu = True
while continu:
    data = lire_data()
    IA.test()
    points_j =0
    points_b = 0
    for i in range(1,11): 
        
        c_bot = f_coup_bot(i)
        gagnant = Round(c_bot)
        if gagnant == "joueur":
            points_j = points_j +1  # add 1 pts a celui qui a gagner
            vict.append("v")
        elif gagnant == "bot":
            points_b = points_b +1
            vict.append("d")
        else:
            vict.append("e")
        print(f"vous: {points_j} pts ---- bot: {points_b} pts ")
    list_en_cours.append(list_coup_joueur)
    list_en_cours.append(list_coup_bot)
    list_en_cours.append(vict)
    data.append(list_en_cours)

    if points_j < points_b:
        print("vous avez perdu")
    elif points_b < points_j:        # savoir qui a gagner
        print("vous avez gagner")
    else:
        print("vous etes egalité")


    if input(">>>>>> voulez vous recommencer : ").lower() != "oui" : # recommencer? 
        continu = False
    save(data)
    list_en_cours = []
    list_coup_bot = []          # reset des list pour save data
    list_coup_joueur = []
    vict = []
