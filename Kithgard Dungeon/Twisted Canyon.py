# Escape from the maze by moving to the X mark.
# Try to collect as many coins as you can.
hero.attack("Treasure Chest")
hero.moveUp()
hero.moveDown()
hero.attack("Gate")
hero.moveRight()
hero.moveUp(2)
hero.moveDown(2)
hero.moveLeft(3)
while True:
    hero.moveUp(2)
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)
    hero.moveLeft(2)
    hero.moveRight(2)
    hero.moveDown()
    hero.moveRight()
    hero.moveUp()
    hero.moveRight()
