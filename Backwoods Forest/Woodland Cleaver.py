# Utilisez votre nouvelle capacité "cleave" (fendre) aussi souvent que possible.

hero.moveXY(23, 23)
while True:
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        # Fendez l'ennemi!
        hero.cleave(enemy)
    else:
        # Sinon (si fendre n'est pas prêt), faites une attaques normale.
        hero.attack(enemy)
