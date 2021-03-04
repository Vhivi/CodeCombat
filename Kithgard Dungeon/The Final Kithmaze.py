# Utilisez une boucle pour bouger et attaquer.
while True:
    hero.moveRight()
    hero.moveUp()
    enemy = hero.findNearestEnemy()
    hero.attack(enemy)
    hero.attack(enemy)
    hero.moveRight()
    hero.moveDown(2)
    hero.moveUp()
