# Amenez le héros et le paysan au sud.

def moveDownCenter():
    '''La fonction déplace votre héros le long de la ligne centrale.'''
    x = 40
    y = hero.pos.y - 12
    hero.moveXY(x, y)

# La fonction construire une clôture sur la droite de quelque chose :something.
def buildRightOf(something):
    '''buildXY une "fence" à 20 mètres de quelque chose(something) qui est à droite.'''
    x = something.pos.x + 20
    y = something.pos.y
    hero.buildXY("fence", x, y)

# La fonction construire une clôture sur la gauche de quelque chose :something.
def buildLeftOf(something):
    '''buildXY une "fence" à 20 mètres de quelque chose(something) qui est à gauche.'''
    x = something.pos.x - 20
    y = something.pos.y
    hero.buildXY("fence", x, y)

while True:
    ogre = hero.findNearestEnemy()
    coin = hero.findNearestItem()
    if ogre:
        buildLeftOf(ogre)
    if coin:
        buildRightOf(coin)
    moveDownCenter()
