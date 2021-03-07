# Explorez la forêt, mais restez sur le qui-vive!
# Il peut y avoir des ogres dans les recoins de forêt!

hero.moveXY(19, 33)
enemy = hero.findNearestEnemy()
# L'instruction `if` testera si la variable contient un ogre.
if enemy:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveXY(49, 51)
enemy = hero.findNearestEnemy()
if enemy:
    # Attaquez l'ennemi ici:
    hero.attack(enemy)
    hero.attack(enemy)

hero.moveXY(58, 14)
enemy = hero.findNearestEnemy()
# Utilisez une instruction `if` pour voir s'il y a un ennemi.
if enemy:
    # S'il y a un ennemi, attaquez-le!    
    hero.attack(enemy)
    hero.attack(enemy)
    
