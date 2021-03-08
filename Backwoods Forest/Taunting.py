# Attack les munchkins, appelle les brawlers et ignore les burls.

def dealEnemy(character):
    '''Cette fonction définit le comportement des héros face aux ennemis.'''
    # Si enemy.type est "munchkin":
    if character.type == "munchkin":
        # Ensuite attaque-le:
        hero.attack(character)
    # Si le type d'ennemi est "brawler":
    elif character.type == "brawler":
        # Alors dis quelque chose au brawler.
        hero.say("Fuck You !")

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        dealEnemy(enemy)
    else:
        hero.moveXY(30, 34)
