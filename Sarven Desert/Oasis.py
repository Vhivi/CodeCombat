# Avancez pour atteindre l'oasis
# mais reculez pour éviter les Yaks a proximité
while True:
    x = hero.pos.x
    y = hero.pos.y
    enemy = hero.findNearestEnemy()
    if enemy and hero.distanceTo(enemy) < 10:
        # Déplacez-vous à gauche en soustrayant 10 de vos coordonnées X
        left = x - 10
        # Use moveXY to move to the new x, y position.
        hero.moveXY(left, y)
    else:
        # Déplacez-vous à droite en additionnant 10 à vos coordonnées X
        right = x + 10
        # Use moveXY to move to the new x, y position.
        hero.moveXY(right, y)
