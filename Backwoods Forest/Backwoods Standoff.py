# Ces Munchkins ont peur du héros!
# Par contre, quand ils seront assez nombreux, les Munchkins se regrouperont et t'embusqueront! Fais attention!
# À chaque fois que tu le peux, `cleave` afin de détruire le groupe d'ennemis.

while True:
    enemy = hero.findNearestEnemy()
    # Utilises un 'if-statement' avec 'isReady' pour contrôler "cleave":
    if hero.isReady("cleave"):
        # Fends!
        hero.cleave()
    # Autrement, si 'cleave' n'est pas prêt:
    else:
        # Attaque l'ogre le plus proche
        hero.attack(enemy)
