# Créer une classe Voiture qui respecte les règles suivantes:
# 1. La classe est initialisée grâce à un constructeur qui prend en paramètre la marque
# 2. Le constructeur initialise aussi la vitesse initiale à 0
# 3. La classe implémente une méthode demarrer qui met la voiture en marche
# 4. La classe implémente une méthode accelerer qui prend en paramètre une valeur et augmente la vitesse
#    de cette valeur
#    (si la voiture n'a pas démarré, la méthode accélérer affiche un message)
# 5. La classe implémente une méthode arreter qui remet la vitesse de la voiture à 0

# class voiture():

#    marque = 'toyota'
#    vitesse = 0
#    def demarrer(self):
#     print('vitesse')
#     def accelerer(self,):
#         vitesse = vitess +1
#      if voiture:
#       print(demarré)
#      else:
#          print(erreur)
#          toyota = voiture()
#          voiture.arreter()
#          print(vitesse)


class Voiture():
    def __init__(self, marque):
        self.marque = marque
        self.vitesse = 0
        self.est_en_marche = False
    
    def demarrer(self):
        self.est_en_marche = True
        print(f'{self.marque} a démarré...')
    
    def accelerer(self, increment):
        if self.est_en_marche:
            self.vitesse += increment
            print(f'{self.marque} accélère jusqu\'à {self.vitesse} km/h.')
        else:
            print('Il faut d\'abord démarrer la voiture!')
    
    def arreter(self):
        self.vitesse = 0
        self.est_en_marche = False
        print(f'{self.marque} s\'est arrêtée.')

ma_voiture = Voiture('Rav4')
ma_voiture.accelerer(10)
ma_voiture.demarrer()
ma_voiture.accelerer(15)
ma_voiture.accelerer(18)
ma_voiture.arreter()
print(ma_voiture.vitesse)




