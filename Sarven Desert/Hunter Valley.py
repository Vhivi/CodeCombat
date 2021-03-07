# Évadez-vous du côté droit de la vallée.

def moveDownRight(step):
    '''La fonction déplace le héros vers le bas et vers la droite.'''
    hero.moveXY(hero.pos.x + step, hero.pos.y - step)

def moveUpRight(step):
    '''La fonction déplace le héros vers le haut et vers la droite.'''
    # Complétez cette fonction:
    hero.moveXY(hero.pos.x + step, hero.pos.y + step)

#  Le chasseur est gentil et montrera la route.
hunter = hero.findFriends()[0]
route = hunter.route
routeIndex = 0

while routeIndex < len(route):
    direction = route[routeIndex]
    if direction > 0:
        moveUpRight(8)
    else:
        #  Utilisez une fonction moveDownRight avec le décalage 8:
        moveDownRight(8)
    routeIndex += 1
