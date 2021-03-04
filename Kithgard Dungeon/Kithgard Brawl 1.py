# Survis aux vagues d'Ogres
# Si tu gagnes, ce niveau sera plus dur mais rapportera plus de récompenses.
# Si tu perds, il faudra attendre un jour pour pouvoir Renvoyer une nouvelle solution.
# Chaque nouvel Envoi génère un nouveau niveau aléatoire de même difficulté.

while True:
    enemy = hero.findNearestEnemy()
    item = hero.findNearestItem()
    if enemy:
        distance = hero.distanceTo(enemy)
        if (distance < 10) and hero.isReady("cleave"):
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    if item:
        hero.moveXY(item.pos.x, item.pos.y)
