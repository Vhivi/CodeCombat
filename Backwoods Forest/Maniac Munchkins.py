# Un autre coffre dans le champ à ouvrir!
# Attaque le coffre pour forcer son ouverture.
# Certains munchkins ne resteront pas tranquilles pendant que tu les attaques!
# Défends-toi quand un munchkin se rapproche trop.

while True:
    enemy = hero.findNearestEnemy()
    distance = hero.distanceTo(enemy)
    if hero.isReady("cleave"):
        # La première priorité est d'utilise Cleave quand il est prêt.
        hero.cleave()
        pass
    elif distance < 5:
        # Attaque le munchkin le plus proche qui est dans ton rayon de portée.
        hero.attack(enemy)
        pass
    else:
        # sinon, essaie de forcer l'ouverture du coffre:
        # Utilise le nom du coffre pour l'attaquer: "Chest".
        hero.attack("Chest")
        pass
