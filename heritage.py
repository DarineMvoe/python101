
# Classe mère (ou générale)
class Mammifere():
    environnement = 'planète terre'

    def presentation(self):
        print(f'Cet animal vit ici: {self.environnement}')

#Classe fille (ou sous-classe)
class Cetace(Mammifere):
    # On peut redéfinir des attributs ou des méthodes dans les sous-classes
    environnement ='océan'

    # On peut également ajouter de nouveaux attributs ou méthodes
    nez = 'au-dessus de la tête'

chat = Mammifere()

chat.presentation()
print('============================')
dauphin = Cetace()
print(dauphin.nez)

# Toutes les méthodes définies dans la classe mère sont accessibles aux sous-classes
dauphin.presentation()
