#­ 
import random as r

pv = 20
dee = r.randint(1, 6)
niveau = 0
victoire = 0
defaite = 0

def parti():
    print("Vous êtes dans un couloir infini, des portes tout du long derriere lesqulles se cachent des monstres que vouz allez devoir affronter")
    print("Vouz ouvrez la premiere porte")
    menu()


def monstre(puissance_monstre):
    puissance_monstre = r.randint(1, 5)
    niveau += 1


def status():
    print("Adversaire: ",niveau)
    print("Force de l'adversaire: ", puissance_monstre)
    print("Niveau de vie de l'usager: ", pv)
    print("Combat", niveau,": ", ":Victoire: ",victoire,"Défaite: ", defaite)

def menu():
    print("Que voulez-vous faire: ")
    print("1- Combatre cet adversaire")
    print("2- Contourner cet adversaire et aller ouvrir une autre porte")
    print("3- Afficher les règles du jeu")
    print("4- Quitter la partie")
    action = int(input(": "))

    if action == 1:
        combatre()

    elif action == 2:
        vie -= 1
        print("Vous avez fui le combat, vous perdez 1 point de vie et ouvrez une autre porte")
        menu()

    elif action == 3:
        print("Pour réussir un combat, il faut que la valeur du dé lancé soit supérieure à la force de l’adversaire.\nDans ce cas, le niveau de vie de l’usager est augmenté de la force de l’adversaire.\nUne défaite a lieu lorsque la valeur du dé lancé par l’usager est inférieure ou égale à la force de l’adversaire.\nDans ce cas, le niveau de vie de l’usager est diminué de la force de l’adversaire.\nLa partie se termine lorsque les points de vie de l’usager tombent sous 0.\nL’usager peut combattre ou éviter chaque adversaire, dans le cas de l’évitement, il y a une pénalité de 1 point de vie.\n\n")
        menu()

    elif action == 4:
        print("Merci et au revoir...")
        exit()

parti()

#def combatre():
