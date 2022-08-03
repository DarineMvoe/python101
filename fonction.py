prenom = 'johanna'
nom = 'david'

def nom_complet(pre, nm):
    return f'{pre} {nm}'

complet = nom_complet(nm=nom, pre=prenom)
print(complet.upper())