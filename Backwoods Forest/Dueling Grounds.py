# Bat le héros ennemi dans un duel

while True:
    # Trouve et attaque l'ennemi dans une boucle.
    # When you're done, submit to the multiplayer ladder!
    enemy = hero.findNearestEnemy()
    if hero.isReady("cleave"):
        hero.shield()
        hero.cleave(enemy)
        pass
    else:
        hero.attack(enemy)
        pass
    
