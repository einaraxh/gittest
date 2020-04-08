import pyglet
from pyglet.window import key, FPSDisplay
from pyglet.sprite import Sprite
from GameObject import GameObject, preload_image

class GameWindow(pyglet.window.Window):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.set_location(360, 90)
        self.frame_rate = 1/60.0
        self.fps_display = FPSDisplay(self)
        self.fps_display.label.font_size = 24

        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.space = False

        self.player_speed = 300
        self.player_firerate = 0.1    

        player_spr = Sprite(preload_image('retard.png'))
        self.player = GameObject(self.width/2, 120, player_spr)
    
        self.player_bullet = preload_image('bullet.png')
        self.player_bullet_list = []


    def on_key_press(self, symbol, modifiers):
        if symbol == key.A:
            self.left = True
        if symbol == key.D:
            self.right = True
        if symbol == key.W:
            self.up = True
        
        if symbol == key.SPACE:
            self.space = True

        if symbol == key.ESCAPE:
            pyglet.app.exit()

    def on_key_release(self, symbol, modifiers):
        if symbol == key.A:
            self.left = False
        if symbol == key.D:
            self.right = False
        if symbol == key.W:
            self.up = False
        if symbol == key.SPACE:
            self.space = False
        
    def on_draw(self):
        self.clear()
        self.player.draw()
        for p in self.player_bullet_list:
            p.draw()

        self.fps_display.draw()

    def update_player(self, dt):
        self.player.update()
        if self.right and self.player.posx < self.width:
            self.player.posx += self.player_speed * dt
        if self.left and self.player.posx > 0:
            self.player.posx += -self.player_speed * dt
    
    def update_player_bullets(self, dt):
        for p in reversed(self.player_bullet_list):
            p.update()
            p.posy += 400 * dt
            if p.posy > self.height+60:
                self.player_bullet_list.remove(p)

    def player_fire(self, dt):
        self.player_firerate -= dt
        if self.player_firerate <= 0:
            self.player_bullet_list.append(GameObject(self.player.posx, self.player.posy, Sprite(self.player_bullet)))
            self.player_firerate += 0.1


    def update(self, dt):
        self.update_player(dt)
        if self.space:
            self.player_fire(dt)
        self.update_player_bullets(dt)

if __name__ == "__main__":
    window = GameWindow(1200, 900, "Space Invaders", resizable=False)
    pyglet.clock.schedule_interval(window.update, window.frame_rate)
    pyglet.app.run()