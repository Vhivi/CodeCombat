# Ceci montre comment définir une fonction appelée cleaveWhenClose
# Cette fonction définit un paramètre appelé `target`
def cleaveWhenClose(target):
    '''Lance cleave quand la cible (target) est trop proche.'''
    if hero.distanceTo(target) < 5:
        # Mets ton code d'attaque ici
        # Si fendre (cleave) est prêt (isReady), alors cleave target
        if hero.isReady("cleave"):
            hero.cleave(target)
        # sinon, juste attaque `target`!
        else:
            hero.attack(target)

# Ce code ne fait pas partie de la fonction.
while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Note qu'à l'intérieur de la fonction cleaveWhenClose, nous faison référence à `enemy` sous l'appellation `target`.
        cleaveWhenClose(enemy)
