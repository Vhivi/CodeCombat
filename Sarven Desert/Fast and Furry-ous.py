# Use an event handler so pet and hero will both run!

def petMove():
    '''Définit la position que le pet doit atteindre.'''
    pet.moveXY(50, 21)

# Use pet.on("spawn", petMove) instead of petMove().
# This way your hero and pet will run at the same time.
pet.on("spawn", petMove) # ∆ Replace this with pet.on("spawn", petMove)

hero.moveXY(50, 12)
