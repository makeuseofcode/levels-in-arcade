import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class LevelOne:
    def __init__(self):
        self.player_x = SCREEN_WIDTH // 2

    def update(self):
        pass

    def draw(self):
        arcade.draw_rectangle_filled(self.player_x, 50, 50, 50, arcade.color.BLUE)

class LevelTwo:
    def __init__(self):
        self.player_x = SCREEN_WIDTH // 2

    def update(self):
        pass

    def draw(self):
        arcade.draw_rectangle_filled(self.player_x, 50, 50, 50, arcade.color.RED)

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")
        arcade.set_background_color(arcade.color.WHITE)
        self.levels = [LevelOne(), LevelTwo()]
        self.current_level = 0

    def on_draw(self):
        arcade.start_render()
        self.levels[self.current_level].draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.levels[self.current_level].player_x -= 10
        elif key == arcade.key.RIGHT:
            self.levels[self.current_level].player_x += 10

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            pass

    def update(self, delta_time):
        self.levels[self.current_level].update()

        # Check if the player crossed the boundary
        if self.levels[self.current_level].player_x < 0:
            self.current_level += 1
            self.current_level %= len(self.levels)
            self.levels[self.current_level].player_x = SCREEN_WIDTH
        elif self.levels[self.current_level].player_x > SCREEN_WIDTH:
            self.current_level += 1
            self.current_level %= len(self.levels)
            self.levels[self.current_level].player_x = 0

def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
