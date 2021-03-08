# Attack les munchkins, appelle les brawlers et ignore les burls.

# Cette fonction définit le comportement des héros face aux ennemis.
def dealEnemy(enemy):
    # Si enemy.type est "munchkin":
    if enemy.type == "munchkin":
        # Ensuite attaque-le:
        hero.attack(enemy)
    # Si le type d'ennemi est "brawler":
    elif enemy.type == "brawler":
        # Alors dis quelque chose au brawler.
        hero.say("Fuck You !")

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        dealEnemy(enemy)
    else:
        hero.moveXY(30, 34)
