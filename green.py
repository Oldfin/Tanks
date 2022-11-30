import arcade
import math
from cotsants import *


class Green(arcade.Sprite):
    def __init__(self, window):
        super().__init__('green.png', 0.12)
        self.part_y = None
        self.part_x = None
        self.window = window
        self.center_x = 500
        self.center_y = 500
        self.active = True
        self.shots = 0

    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x, self.center_y + 50, 50, 15, (255, 255, 255), 1)
        indent = self.shots * 10
        arcade.draw_rectangle_filled(self.center_x - indent / 2, self.center_y + 50, 50 - indent, 13, (50, 205, 50))

    def update(self):
        if self.active:
            self.angle += self.change_angle
            self.part_x = math.cos(math.radians(self.angle))
            self.part_y = math.sin(math.radians(self.angle))
            self.center_x += self.part_x * self.change_x
            self.center_y += self.part_y * self.change_y
            if self.left <= 0:
                self.left = 0
            if self.right >= SCREEN_WIDTH:
                self.right = SCREEN_WIDTH
            if self.bottom <= 0:
                self.bottom = 0
            if self.top >= SCREEN_HEIGHT:
                self.top = SCREEN_HEIGHT
            hits = arcade.check_for_collision_with_list(self, self.window.projectiles)
            for bullete in hits:
                if bullete.side != 1:
                    bullete.kill()
                    self.shots += 1
            if self.shots >= 5:
                self.texture = arcade.load_texture('green_broken.png')
                self.active = False
                self.shots = 5

