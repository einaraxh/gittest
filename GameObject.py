import pyglet

def preload_image(image):
    img = pyglet.image.load('res/sprites/'+image)
    return img

class GameObject:
    def __init__(self, posx, posy, sprite=None):
        self.posx = posx
        self.posy = posy
        self.velx = 0
        self.vely = 0
        if sprite is not None:
            self.sprite = sprite
            self.sprite.x = self.posx
            self.sprite.y = self.posy
            self.width = self.sprite.width
            self.height = self.sprite.height

    def draw(self):
        self.sprite.x = self.posx-self.sprite.width/2
        self.sprite.y = self.posy-self.sprite.height/2
        self.sprite.draw()

    def update(self):
        return