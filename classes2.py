class Etudiant():
    def __init__(self, nom, age):
        self.nom = nom
        self.age = age
    
    def enregistrer_note1(self, note):
        self.note1 = note

    def enregistrer_note2(self, note):
        self.note2 = note

    def enregistrer_note3(self, note):
        self.note3 = note
    
    def calculer_moyenne(self):
        return (self.note1 + self.note2 + self.note3) / 3

darine = Etudiant('Darine', 25)
darine.enregistrer_note1(15)
darine.enregistrer_note2(18)
darine.enregistrer_note3(14)
print(darine.calculer_moyenne())