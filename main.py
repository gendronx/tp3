# ­ 
"""
Xavier Gendron
404
Ce programme est un jeu dans lequel nous avancons dans un couloir rempli de monstre
"""

from random import randint

pv = 20
niveau = 0
victoire = 0
defaite = 0
victoire_consecutive = 0
puissance_monstre = 0
dee = 0


def parti():
    print(f"Vous êtes dans un couloir infini, des portes tout du long derriere lesqulles se cachent des monstres que vouz allez devoir affronter")
    print(f"Vouz ouvrez la premiere porte")


def status():
    print(f"Adversaire: {niveau}")
    print(f"Force de l'adversaire: {puissance_monstre}")
    print(f"Puissance du joueur: {dee}")
    print(f"Niveau de vie de l'usager: {pv}")
    print(f"Combat {niveau}: Victoire: {victoire} Défaite: {defaite}")


def menu():
    global pv, niveau

    print(f"Que voulez-vous faire: ")
    print(f"1- Combatre cet adversaire")
    print(f"2- Contourner cet adversaire et aller ouvrir une autre porte")
    print(f"3- Afficher les règles du jeu")
    print(f"4- Quitter la partie")
    print(f"5- status")
    action = int(input(": "))

    if action == 1:
        combatre()
        status()

    elif action == 2:
        print(f"Vous avez fui le combat, vous perdez 1 point de vie et ouvrez une autre porte")
        niveau += 1
        pv -= 1
        print(f"Il vous reste {pv} point de vie")
        if pv < 1:
            print("Vos points de vie on atteint 0 "
                  "vous êtes mort")
            exit()
        menu()

    elif action == 3:
        print(f"Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\n"
              "Dans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\n"
              "Une défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.\n"
              "Dans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\n"
              "La partie se termine lorsque les points de vie de l’usager tombent sous 0.\n"
              "L’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\n\n")
        menu()

    elif action == 4:
        print(f"Merci et au revoir...")
        exit()

    elif action == 5:
        status()
        menu()


def combatre():
    global niveau, pv, victoire, defaite, puissance_monstre, dee, victoire_consecutive
    puissance_monstre = randint(1, 1)
    dee = randint(1, 6)
    niveau += 1
    print(f"Vous tombez face à face avec un adversaire de difficulté : {puissance_monstre}")

    if dee > puissance_monstre:
        pv += puissance_monstre
        victoire += 1
        print(f"Vous avez gagner le combat")
        victoire_consecutive += 1
        print(f"Nombre de victoire consécutives: {victoire_consecutive}")
        status()
        menu()

    elif dee < puissance_monstre:
        pv -= puissance_monstre
        defaite += 1
        print(f"Vous avez perdu le combat")
        victoire_consecutive = 0
        print(f"Nombre de victoire consécutives: {victoire_consecutive}")
        status()
        if pv < 1:
            print("Vos points de vie on atteint 0 "
                  "vous êtes mort")
            exit()
        menu()

    elif dee == puissance_monstre:
        pv -= puissance_monstre
        defaite += 1
        print(f"Vous avez perdu le combat")
        victoire_consecutive = 0
        print(f"Nombre de victoire consécutives: {victoire_consecutive}")
        status()
        if pv < 1:
            print("Vos points de vie on atteint 0 "
                  "vous êtes mort")
            exit()
        menu()

    if pv < 1:
        print("Vos points de vie on atteint 0 "
              "vous êtes mort")
        exit()


parti()
menu()
