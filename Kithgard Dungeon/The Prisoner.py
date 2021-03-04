# Libère le prisonnier, bats le garde et prend la gemme.

# Délivre Patrick derrière la porte "Weak Door".
hero.moveRight()
hero.attack("Weak Door")
hero.moveRight(2)

# Tue le garde nommé "Two"
enemy = hero.findNearestEnemy()
while enemy:
    hero.attack(enemy)

# Récupère la gemme.
hero.moveRight()
hero.moveDown(3)
