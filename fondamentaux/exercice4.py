# Créer deux fonctions
# La première demande le nom de l'utilisateur
# Et lui souhaite la bienvenue ('Bienvenue, Alex' par exemple)
# La deuxième donne le nombre de lettres dans le nom de l'utilisateur
# ('Alex compte 4 lettres' par exemple)

# alex = "bienvenue alex"
# print(f"{alex}")
# def nom_utilisateur(alex):
#     for lettre in alex :
#         print(lettre)

# nom_utilisateur('alex')

def salutation():
    nom = input('Votre nom: ')
    print(f'Bienvenue, {nom}')
    return nom

def nombre_lettres(mot):
    print(f'{mot} compte {len(mot)} lettres.')

nombre_lettres(salutation())