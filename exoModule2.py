# Dans le fichier monModule.py, créer une classe Personne avec un constructeur 
#  qui prend en paramètre le nom et l'année de naissance.
# Cette classe possède également une méthode calcul_age qui prend en
#  paramètre une année et retourne l'age de la personne cette année

# Dans le fichier exoModule2.py, importer la classe Persone, créer une 
#  instance de la classe et invoquer la méthode calcul_age pour les années 
#  1999 et 2022


from monModule import NouvellePersonne


darine = NouvellePersonne('Darine', 1990)
print(darine.calcul_age(1999))
print(darine.calcul_age(2022))