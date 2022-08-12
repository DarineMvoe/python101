# Créer une fonction qui prend en paramètre deux nombres
# et retourne le plus grand de ces nombres.

def plus_grand(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2


print(plus_grand(123, 75))