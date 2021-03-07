# Atteignez l'oasis. Attention aux nouveaux ennemis : les ogres éclaireurs !
# Allez vers le haut et la droite en ajoutant votre position en x et en y.

while True:
    # Attaque tout les ennemis que tu croise.
    enemy = hero.findNearestEnemy()
    if enemy:
        distance = hero.distanceTo(enemy)
        if hero.isReady("cleave") and distance < 10:
            hero.cleave(enemy)
        else:
            hero.attack(enemy)
    # Ou si il n'y à aucun ennemis en vue, continue d'avancer vers en haut à droite.
    else:
        hero.moveXY(hero.pos.x + 1, hero.pos.y + 1)
    
