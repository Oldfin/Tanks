import arcade


class Base(arcade.Sprite):
    def __init__(self, image, center_y, center_x, window):
        super().__init__(image, 1.5, )
        self.center_x = center_x
        self.center_y = center_y
        self.shots = 0
        self.window = window

    def draw(self):
        super().draw()
        arcade.draw_rectangle_outline(self.center_x, self.center_y + 320, 250, 15, (255, 0, 0), 3)
        indent = self.shots * 25
        arcade.draw_rectangle_filled(self.center_x - indent / 2, self.center_y + 320, 250 - indent, 9, (50, 205, 50))

    def update(self):
        hits = arcade.check_for_collision_with_list(self, self.window.projectiles)
        for bullete in hits:
            bullete.kill()
            self.shots += 1
        if self.shots >= 10:
            self.window.game = False
            self.shots = 10
