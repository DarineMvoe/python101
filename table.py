nom = 'edwige'
prenom = 'simone'

for edwige in nom:
     print(edwige*2)

def nom_individu(nm, pre):
    return f'{nm} {pre}'
individu = nom_individu(nm=nom, pre=prenom)
print(individu)   
