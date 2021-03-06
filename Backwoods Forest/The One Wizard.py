# Defeat as many ogres as you can.
# Use 'cast' and 'canCast' for spells.

while True:
    enemy = hero.findNearestEnemy()
    if enemy:
        if hero.isReady("chain-lightning"):
            hero.cast("chain-lightning", enemy)
        elif hero.isReady("lightning-bolt"):
            hero.cast("lightning-bolt", enemy)
        else:
            hero.attack(enemy)
    if hero.health < (83 / 2):
        if hero.isReady("regen"):
            hero.cast("regen", hero)
			
