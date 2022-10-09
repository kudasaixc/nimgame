"""
Date : Octobre 2022
But du projet : Jouer au jeu des allumettes, dit "Jeu de Nim"
"""

# Importation des modules
from time import sleep
from random import randint

# Déclaration du nombre d'allumettes par défaut
allumettes = 21

# Variable booléenne qui sera mise en False lorsque le jeu sera terminé
jeu = True

def ReplayGame(): # Fonction qui permet de rejouer
    print("Voulez vous rejouer?")
    var = input("oui/non")
    if var == "oui":
        jeu = True
    elif var == "non":
        jeu = False
    else:
        print("Paramètre non documenté")

while jeu == True & allumettes > 0: # Boucle principale du jeu
    print(f"Il y a {allumettes} allumettes\n")
    print("Combien d'allumettes voulez vous prendre? 1, 2 ou 3")
    rem = int(input()) # interaction avec l'utilisateur
    while rem > 3 or rem < 1: # Si l'utilisateur prend plus de 3 ou moins de 1 allumettes
        print("Vous ne pouvez pas prendre plus de 3 ou moins de 1 allumettes")
        rem = int(input())
    else: 
        print("L'ordinateur réfléchit...\n")
        sleep(randint(1,2)) # pause d'une seconde pour réalisme
        print(f"Vous avez pris {rem} allumettes.")
        allumettes = allumettes - rem
        if allumettes > 3:
            ordi = int(randint(1,3))
            print(f"L'ordinateur prend {ordi} allumettes")
            allumettes = allumettes - ordi
        elif allumettes == 3:
            ordi = 2
            print(f"L'ordinateur prend {ordi} allumettes")
            allumettes = allumettes - ordi
            print(f"Vous avez perdu car il reste {allumettes} allumettes")
            ReplayGame()
        elif allumettes == 2:
            ordi = 1
            print(f"L'ordinateur prend {ordi} allumettes")
            allumettes = allumettes - ordi
            print(f"Vous avez perdu car il reste {allumettes} allumettes")
            ReplayGame()
        elif allumettes == 1:
            print("L'ordinateur a perdu")
            print("Vous avez gagné!")
            ReplayGame()
        else:
            print("Vous avez gagné")       
        rem = 0
        ordi = 0
    
