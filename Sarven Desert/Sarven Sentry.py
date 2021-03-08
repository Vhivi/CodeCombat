# Utilisez des drapeaux de différentes couleurs pour exécuter de différentes tâches.

while True:
    flagGreen = hero.findFlag("green")
    flagBlack = hero.findFlag("black")
    
    # S'il y a un drapeau vert, construisez une barrière.
    if flagGreen:
        # Build a "fence" at flagGreen's position.
        hero.buildXY("fence", flagGreen.pos.x, flagGreen.pos.y)
        # Garder en esprit de ramasser les drapeaux après de les avoir utiliser!
        hero.pickUpFlag(flagGreen)
    # S'il y a un drapeau noir, construisez un piège à feu.
    if flagBlack:
        # Build a "fire-trap" at flagBlack's position.
        hero.buildXY("fire-trap", flagBlack.pos.x, flagBlack.pos.y)
        # Garder en esprit de ramasser les drapeaux après de les avoir utiliser!
        hero.pickUpFlag(flagBlack)
    # Move back to the center.
    hero.moveXY(43, 31)
    
