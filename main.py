from random import*
from ast import*
import IA

regle = {"pierre":"ciseaux", "ciseaux": "feuille", "feuille":"pierre"}    # la pierrre bas le ciseaux qui bas la feuille qui bas la pierre
joueur = IA.joueur
print(joueur)
def save(data):
    DATA = str(f"{data}")
    Save = open(f"{joueur}.txt","w")   # sauvgarder les data dans data.txt
    Save.write(DATA)
    Save.close()

def lire_data():
    donner= open(f"{joueur}.txt", "r")   # recuperer les donners save
    data = donner.read()
    data = literal_eval(data)
    #print(data)
    return data

def Round(coup_bot):  # deroulement d'un tour

    coup_ent = coup_joueur()

    if regle[coup_ent] == coup_bot:             # verifier qui a gagner
        print(f"{coup_ent} bas {coup_bot}")
        return "joueur"
    elif regle[coup_bot] == coup_ent :
        print(f"{coup_ent} pert contre {coup_bot}")
        return "bot"
    else:
        print(f"{coup_ent} et {coup_bot} sont egalité")
        return "egal"


##################################    coup du joueur et du bot   #################################################
def f_coup_bot(tour):
    if tour == 1: 
        rd = IA.t1()
        list_coup_bot.append(rd[0])   
    else:
        c = IA.coup_prevu(result)
        list_coup_bot.append(c[0])                  # pour l'intant c'est aleatoir mais il faudras changer ca
        #print(rd)
    return c

def coup_joueur ():
    complete = False                   # mettre en forme le coup de joueur 
    while not complete :
        coup = input("quelle coup voulez vous jouer: ")
        if coup == "p":
            coup_ent ="pierre"
            complete =True
        elif coup == "f":
            coup_ent ="feuille"
            complete =True
        elif coup == "c":
            coup_ent = "ciseaux"
            complete = True
        else:
            print("vous vous n'avez pas donner une valeur attendu: pierre: p / feuille: f / ciseaux: c")
    list_coup_joueur.append(coup)
    return coup_ent 
 ######################################################################           

data = []
list_en_cours = []
list_coup_joueur = []
list_coup_bot = []
vict=[]
result = ""

# save(data)     # cette commande permet de sauvdarder les donners  (la variable data)
if data != "[]":
    print(IA.change_ap_defaite())
continu = True
while continu:
    data = lire_data()
    points_j =0
    points_b = 0
    for i in range(1,11): 
        
        c_bot = f_coup_bot(i)
        gagnant = Round(c_bot)
        if gagnant == "joueur":
            points_j = points_j +1  # add 1 pts a celui qui a gagner
            vict.append("v")
            result = "v"
        elif gagnant == "bot":
            points_b = points_b +1
            vict.append("d")
            result = "d"
        else: 
            vict.append("e")
            result = "e"
        print(f"vous: {points_j} pts ---- bot: {points_b} pts ")


    if points_j < points_b:
        print("vous avez perdu")
    elif points_b < points_j:        # savoir qui a gagner
        print("vous avez gagner")
    else: 
        print ("egalité...")
    list_en_cours.append(list_coup_joueur)
    list_en_cours.append(list_coup_bot)
    list_en_cours.append(vict)
    data.append(list_en_cours)
    list_en_cours = []
    list_coup_joueur = []
    list_coup_bot = []            #reset des varialble pour construire data
    vict=[]


    if input(">>>>>> voulez vous recommencer : ").lower() != "oui" : # recommencer? 
        continu = False
    save(data)
