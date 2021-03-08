# Votre tâche est de lui dire la distance par rapport aux ogres qui approchent.

def nearestEnemyDistance():
    '''Cette fonction trouve l'ennemi le plus proche et retourne sa distance par rapport a vous.
	Si il n'y a pas d'ennemi, la fonction retourne 0.'''
    enemy = hero.findNearestEnemy()
    result = 0
    if enemy:
        result = hero.distanceTo(enemy)
    return result

while True:
    # Appelle nearestEnemyDistance() et 
    # Sauve le résultat dans la variable enemyDistance.
    enemyDistance = nearestEnemyDistance()
    # Si enemyDistance est supérieur à 0:
    if enemyDistance > 0:
        # Dis la valeur de la variable enemyDistance.
        hero.say(enemyDistance)
