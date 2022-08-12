class Personne():
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    espece = 'humaine'

    def presentation(self):
        print(f'Bonjour, je me nomme {self.nom} et j\'ai {self.age} ans. \n Je suis une {self.espece}')


# darine = Personne('Darine', 25)
# darine.presentation()

class Vehicule():
    nb_roues = 4
    couleur = 'violet'
    

    def demarrer(self):
        print('Vroum vroum!')


toyota = Vehicule()
toyota.demarrer()
print(toyota.nb_roues)