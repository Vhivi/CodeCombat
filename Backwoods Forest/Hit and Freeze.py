# Tu es piègé. Ne bouge pas, ca ferait mal 

def inAttackRange(character):
    '''Cette fonction vérifie si l'enemy est dans la distance d'attaque.'''
    distance = hero.distanceTo(character)
    # Presque toute les épées ont une distance d'attaque de 3
    if distance <= 3:
        return True
    return False

# Attaque les ogres seulement quand ils sont à portée
while True:
    # Trouve le plus proche enemy et sauvegarde le dans une variable
    enemy = hero.findNearestEnemy()
    # Appelle inAttackRange(enemy) avec enemy comme argument
    # et sauvegarde le résultat dans canAttack
    canAttack = inAttackRange(enemy)
    # si le resultat sauvegardé dans canAttack est vrai  True, alors attaque !
    if canAttack:
        hero.attack(enemy)
