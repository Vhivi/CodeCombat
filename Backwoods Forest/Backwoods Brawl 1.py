# Reste en vie pendant 1 minute. 
# Si tu gagne, ca devient plus difficile (mais la récompense est plus grande)
# Si tu perds, tu devra attendre une journée pour rejouer.
# Rappele-toi, chaque présentation obtient une nouvelle table aléatoire.

def checkAndAttack(target):
    '''Vérifie si l'ennemi existe, sa distance et si les abiletés sont disponibles.'''
    if target:
        if hero.isReady("cleave") and (hero.distanceTo(target) < 10):
            hero.cleave(target)
        elif hero.distanceTo(target) > 10:
            hero.shield()
            hero.attack(target)
        else:
            hero.attack(target)

while True:
    enemy = hero.findNearestEnemy()
    checkAndAttack(enemy)

