import arcade
import math
import time
import bullet as bul


class Red_tank(arcade.Sprite):
    def __init__(self, window):
        super().__init__('red.png', 0.12)
        self.active = True
        self.angle = 180
        self.shots = 0
        self.window = window
        self.bullet_time = time.time()

    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x, self.center_y + 50, 50, 15, (255, 255, 255), 1)
        indent = self.shots * 10
        arcade.draw_rectangle_filled(self.center_x - indent / 2, self.center_y + 50, 50 - indent, 13, (255, 164, 27))

    def fire(self):
        if time.time() - self.bullet_time >= 2:
            shell = bul.Bullet('red_bullet.png', self, 0)
            self.window.projectiles.append(shell)
            self.bullet_time = time.time()

    def update(self):
        if self.active:

            self.part_x = math.cos(math.radians(self.angle))
            self.part_y = math.sin(math.radians(self.angle))
            hits = arcade.check_for_collision_with_list(self, self.window.projectiles)
            for bullete in hits:
                if bullete.side == 1:
                    bullete.kill()
                    self.shots += 1
            if self.shots >= 5:
                self.texture = arcade.load_texture('red_broken.png')
                self.active = False
                self.shots = 5
            delta_x = self.window.green_tank.center_x - self.center_x
            delta_y = self.window.green_tank.center_y - self.center_y
            self.radius = arcade.get_distance_between_sprites(self, self.window.green_tank)

            if self.radius <= 250:
                self.angle = math.degrees(math.atan2(delta_y, delta_x))
                self.fire()
            elif arcade.get_distance_between_sprites(self.window.green_base, self) <= 400:
                base_delta_x = self.window.green_base.center_x - self.center_x
                base_delta_y = self.window.green_base.center_y - self.center_y
                self.angle = math.degrees(math.atan2(base_delta_y, base_delta_x))
                self.fire()

            else:
                self.angle = 180
                self.center_x -= 1



