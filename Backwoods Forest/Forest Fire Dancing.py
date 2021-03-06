# Dans ce niveau la pierre du mal est mauvaise! Évitez les, marchez dans l'autre direction.
while True:
    evilstone = hero.findNearestItem()
    if evilstone:
        pos = evilstone.pos
        if pos.x == 34:     # == means "is equal to"
            # Si la pierre du mal est sur la gauche, dirige-toi vers le bord droit.
            hero.moveXY(46, 22)
            pass
        else:
            # Si la pierre du mal est sur la droite, dirige-toi vers le bord gauche.
            hero.moveXY(34, 22)
            pass
    else:
        # Si il n'y à pas de pierre du mal, dirige-toi vers le centre.
        hero.moveXY(40, 22)
        pass
