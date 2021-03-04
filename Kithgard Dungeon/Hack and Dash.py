# Tu peux écrire du code avant une boucle (loop).
hero.moveRight()

# Fracasse le coffre ("Chest") avant d'utiliser une boucle pour t'enfuir de ce labyrinthe !
hero.attack("Chest")

# Retourne dans le couloir principal.
hero.moveDown()

while True:
    # Bouge trois fois.
    hero.moveRight(3)
    # Bouge trois fois de plus.
    hero.moveDown(3)
