from random import*
from ast import*

regle = {"pierre":"ciseaux", "ciseaux": "feuille", "feuille":"pierre"}    # la pierrre bas le ciseaux qui bas la feuille qui bas la pierre

def save(data):
    DATA = str(f"{data}")
    Save = open("data.txt","w")   # sauvgarder les data dans data.txt
    Save.write(DATA)
    Save.close()

def lire_data():
    donner= open("data.txt", "r")   # recuperer les donners save
    data = donner.read()
    data = literal_eval(data)
    #print(data)
    return data

def Round(coup_bot):  # deroulement d'un tour

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




    if regle[coup_ent] == coup_bot:             # verifier qui a gagner
        print(f"{coup_ent} bas {coup_bot}")
        return "joueur"
    elif regle[coup_bot] == coup_ent :
        print(f"{coup_ent} pert contre {coup_bot}")
        return "bot"
    else:
        print(f"{coup_ent} et {coup_bot} sont egalité")
        return "egal"


###################################################################################
def f_coup_bot():
    coup_pos = ["pierre","feuille","ciseaux"]   # cette fonction a pour but de choisir le coup du bot 
    rd = choice(coup_pos)                       # pour l'intant c'est aleatoir mais il faudras changer ca
    #print(rd)
    return rd
            

data = []
list_en_cours = []
list_coup_joueur = []
list_coup_bot = []


# save(data)     # cette commande permet de sauvdarder les donners  (la variable data)
lire_data()

continu = True
while continu:
    points_j =0
    points_b = 0
    for i in range(1,11): 
        
        c_bot = f_coup_bot()
        gagnant = Round(c_bot)
        if gagnant == "joueur":
            points_j = points_j +1  # add 1 pts a celui qui a gagner
        elif gagnant == "bot":
            points_b = points_b +1
        print(f"vous: {points_j} pts ---- bot: {points_b} pts ")


    if points_j <= points_b:
        print("vous avez perdu")
    elif points_b <= points_j:        # savoir qui a gagner
        print("vous avez gagner")


    if input(">>>>>> voulez vous recommencer : ").lower() != "oui" : # recommencer? 
        continu = False
    save(data)
