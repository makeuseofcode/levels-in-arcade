import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "My Game")
        arcade.set_background_color(arcade.color.WHITE)
        self.player_x = SCREEN_WIDTH // 2

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.player_x, 50, 50, 50, arcade.color.BLUE)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= 10
        elif key == arcade.key.RIGHT:
            self.player_x += 10

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            pass

def main():
    game = MyGame()
    arcade.run()

if __name__ == "__main__":
    main()
