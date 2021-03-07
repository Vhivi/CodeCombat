# Restez au mileu et protégez !

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        # Soit attaquez l'ennemi...
        hero.attack(enemy)
    else:
        # ...soit reculez jusqu'à votre position de défense.
        hero.moveXY(40, 34)
