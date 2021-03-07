# Paysans et péons se réunissent dans la forêt.
# Dirige les paysans vers la bataille et les péons à s'en aller!

while True:
    friend = hero.findNearestFriend()
    if friend:
        hero.say("Vers la bataille, " + friend.id + "!")
    # Maintenant trouve l'ennemi le plus proche et dis-lui de s'en aller.
    ennemy = hero.findNearestEnemy()
    if ennemy:
        hero.say("Fuck off, " + ennemy.id + "!")
