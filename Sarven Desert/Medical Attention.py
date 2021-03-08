# Ask the healer for help when you're under one-half health.

while True:
    currentHealth = hero.health
    healingThreshold = hero.maxHealth / 2
    enemy = hero.findNearestEnemy()
    # Si tes points de vie actuels sont inférieurs au seuil (threshold),
    # move to the healing point and say, "heal me".
    # Sinon, attaquer. Tu dois te battre avec ardeur !
    if currentHealth < healingThreshold:
        hero.moveXY(65, 46)
        hero.say("heal me")
    if enemy:
        hero.attack(enemy)
    
