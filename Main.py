import arcade
import green
from cotsants import *
import base
import bullet
import red


class OurGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("background.png")
        self.green_tank = green.Green(self)
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.projectiles = arcade.SpriteList()
        self.green_base = base.Base('green_base.png', 350, 165, self)
        self.red_base = base.Base('red_base.png', 350, 1035, self)
        self.game = True

        self.red_tanks = []
        self.setup()

    def setup(self):
        for i in range(1, 4):
            tank = red.Red_tank(self)
            tank.center_x = 800
            tank.center_y = 200 * i - 50
            self.red_tanks.append(tank)

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.green_tank.draw()
        self.projectiles.draw()
        self.green_base.draw()
        self.red_base.draw()
        for tank in self.red_tanks:
            tank.draw()
        if self.red_base.shots >= 10:
            arcade.draw_text("Ты выиграл!", 400, SCREEN_HEIGHT / 2, (0, 255, 6), 50, font_name='Comic Sans MS')
        if self.green_base.shots >= 10 or self.green_tank.active == False:
            arcade.draw_text('Ты проиграл!', 400, SCREEN_HEIGHT / 2, arcade.color.RED, 50, font_name='Comic Sans MS')
            self.game = False

    def update(self, delta_time):
        if self.game:
            self.green_tank.update()
            self.projectiles.update()
            self.red_base.update()
            self.green_base.update()
            for tank in self.red_tanks:
                tank.update()

    def on_key_press(self, key, modifiers):
        if self.green_tank.active and self.game:
            if key == arcade.key.LEFT:
                self.left_pressed = True
                self.right_pressed = False
                self.green_tank.change_angle = 2.5
            if key == arcade.key.RIGHT:
                self.right_pressed = True
                self.left_pressed = False
                self.green_tank.change_angle = -2.5
            if key == arcade.key.UP:
                self.up_pressed = True
                self.down_pressed = False
                self.green_tank.change_x = 4
                self.green_tank.change_y = 4
            if key == arcade.key.DOWN:
                self.down_pressed = True
                self.up_pressed = False
                self.green_tank.change_x = -4
                self.green_tank.change_y = -4
            if key == arcade.key.SPACE:
                shell = bullet.Bullet('green_bullet.png', self.green_tank, 1)
                self.projectiles.append(shell)

    def on_key_release(self, key, modifiers):
        if self.green_tank.active and self.game:
            if key == arcade.key.LEFT and not self.right_pressed:
                self.green_tank.change_angle = 0
            if key == arcade.key.RIGHT and not self.left_pressed:
                self.green_tank.change_angle = 0
            if key == arcade.key.UP and not self.down_pressed:
                self.green_tank.change_x = 0
                self.green_tank.change_y = 0
            if key == arcade.key.DOWN and not self.up_pressed:
                self.green_tank.change_x = 0
                self.green_tank.change_y = 0


window = OurGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
arcade.run()
