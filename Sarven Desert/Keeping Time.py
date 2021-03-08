# Utilise ton nouveau pouvoir pour choisir ce que tu dois faire :  hero.time

while True:
    enemy = hero.findNearestEnemy()
    coin = hero.findNearestItem()
    friend = hero.findNearestFriend()
    # Durant les 10 premières secondes : se battre.
    if hero.time < 10:
        if hero.isReady("cleave"):
            hero.cleave(enemy)
        hero.attack(enemy)
        pass
    # Sinon, si on est toujours dans les 35 premières secondes, ramasser des Pièces.
    elif hero.time < 35:
        hero.moveXY(coin.pos.x, coin.pos.y)
        pass
    # Après 35 secondes, rejoindre le raid !
    else:
        hero.moveXY(friend.pos.x, friend.pos.y)
        if enemy:
            if hero.isReady("cleave"):
                hero.cleave(enemy)
            hero.attack(enemy)
        pass
