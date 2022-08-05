
lieu = 'maison' 
jour = 'mardi'
mois = 'fevrier'
def nom_agenda(li, jr, ms):
    return f'{li} {jr} {ms}'

agenda = nom_agenda(li=lieu, jr=jour, ms=mois)
print(agenda.upper())
