
def carre(nombre):
    return nombre * nombre
    # return nombre ** 2

def somme(nombre1, nombre2):
    return nombre1 + nombre2
    
def est_pair(nombre):
    return nombre % 2 == 0 


class NouvellePersonne():
    def __init__(self, nom, annee_naissance):
        self.nom = nom
        self.annee_naissance = annee_naissance

    def calcul_age(self, annee):
        return annee - self.annee_naissance


    