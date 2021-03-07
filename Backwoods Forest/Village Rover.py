# Ceci définit une fonction nommée findAndAttackEnemy
def findAndAttackEnemy():
    '''Trouve et attaque un ennemi.'''
    enemy = hero.findNearestEnemy()
    if enemy:
        hero.attack(enemy)

# Ce code ne fait pas partie de la fonction.
while True:
    # Maintenante tu peux patrouiller le village en utilisant findAndAttackEnemy
    hero.moveXY(35, 34)
    findAndAttackEnemy()
    
    # Maintenant déplace-toi vers l'entrée de droite.
    hero.moveXY(60, 31)
    # Utilise findAndAttackEnemy
    findAndAttackEnemy()
