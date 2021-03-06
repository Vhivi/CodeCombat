while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if distance < 10:
        # Attaquez s'ils se rapprochent trop du paysan.
        hero.attack(enemy)
        pass
    # Sinon, rester près du paysan ! Utilisez else.
    else:
        hero.moveXY(40, 37)
