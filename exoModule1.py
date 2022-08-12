# I. Dans le fichier monModule.py créer trois fonctions
#    1. La première fonction prend en paramètre un nombre et retourne ce nombre au carré
#    2. La deuxième fonction prend en paramètres deux nombres et retourne leur somme
#    3. La troisième prend en paramètre un nombre et retourne True si le nombre est pair
#       et False si le nombre est impair

# II. Dans ce fichier (exoModule1.py), importer et tester les trois fonctions ci-dessus.



from monModule import carre, est_pair, somme


print(carre(4))
print(somme(10, 11))
print(est_pair(50))
print(est_pair(11))