# ­ 
"""
Xavier Gendron
404
Ce programme est un jeu dans lequel nous avancons dans un couloir rempli de monstre
"""


import random as r

pv = 20
niveau = 0
victoire = 0
defaite = 0


def parti():
    print(f"Vous êtes dans un couloir infini, des portes tout du long derriere lesqulles se cachent des monstres que vouz allez devoir affronter")
    print(f"Vouz ouvrez la premiere porte")
    print(f"Vous tombez face à face avec un adversaire de difficulté : {puissance_monstre}")
    menu()



def status():
    print(f"Adversaire: {niveau}")
    print(f"Force de l'adversaire: {puissance_monstre}")
    print(f"Niveau de vie de l'usager: {pv}")
    print(f"Combat {niveau}:Victoire: {victoire} Défaite: {defaite}")


def menu():
    print(f"Que voulez-vous faire: ")
    print(f"1- Combatre cet adversaire")
    print(f"2- Contourner cet adversaire et aller ouvrir une autre porte")
    print(f"3- Afficher les règles du jeu")
    print(f"4- Quitter la partie")
    action = int(input(": "))

    if action == 1:
        combatre()

    elif action == 2:
        pv -= 1
        print(f"Vous avez fui le combat, vous perdez 1 point de vie et ouvrez une autre porte")
        menu()

    elif action == 3:
        print(f"Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.\nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\n\n")
        menu()

    elif action == 4:
        print(f"Merci et au revoir...")
        exit()


parti()
status()


def combatre():
    puissance_monstre = r.randint(1, 5)
    dee = r.randint(1, 6)
    niveau += 1

    if dee > puissance_monstre:
        vie += puissance_monstre
        victoire += 1
        menu()

    elif dee < puissance_monstre:
        vie -= puissance_monstre
        defaite += 1
        status()
        menu()

    elif dee == puissance_monstre:
        vie -= puissance_monstre
        defaite += 1
        status()
        menu()

