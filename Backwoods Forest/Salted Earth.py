# Les ogres attaquent à proximité de la colonie !
# Fais attention, car les ogres ont semé du poison dans la terre.
# Ramasse des pièces et vaincs les ogres, mais fait attention aux pièges et au poison !

while True:
    enemy = hero.findNearestEnemy()
    if enemy.type in ('munchkin', 'thrower'):
        hero.attack(enemy)
    item = hero.findNearestItem()
    # Vérifie quel est le type de l'objet pour être sûre que le héro ne ramasse pas du poison !
    # Si le type d'objet est une "gem" ou une "coin":
    if item.type == "gem" or item.type == "coin":
        # Ensuite déplace toi et ramasse le:
        pos = item.pos
        x = pos.x
        y = pos.y
        hero.moveXY(x, y)
