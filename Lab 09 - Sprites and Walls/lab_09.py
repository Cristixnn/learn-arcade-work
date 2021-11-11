import random
import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_GEM = 0.5
GEM_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 10


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 9: Sprites and Walls")

        # Sprite lists
        self.score = 0
        self.player_list = None
        self.wall_list = None
        self.gem_list = None

        # Set up the player
        self.player_sprite = None

        # This variable holds our simple "physics engine"
        self.physics_engine = None

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.gem_sound = arcade.load_sound("arcade_resources_sounds_coin4.wav")

    def setup(self):

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()

        # Reset the score

        # Create the player
        self.player_sprite = arcade.Sprite("slimeBlock.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 200
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 450
        self.wall_list.append(wall)


        wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 450
        self.wall_list.append(wall)

        # --- Place boxes inside a loop

        for x in range(300, 1800, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 800
            self.wall_list.append(wall)

        for x in range(0, 500, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 600
            self.wall_list.append(wall)
        for x in range(300, 600, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)
        for y in range(200, 700, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 1700
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(200, 700, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 1000
            wall.center_y = y
            self.wall_list.append(wall)
        for x in range(1200, 1500, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 400
            self.wall_list.append(wall)
        for x in range(1200, 1500, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 600
            self.wall_list.append(wall)
        for x in range(1200, 1500, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 200
            self.wall_list.append(wall)
        for y in range(200, 700, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 1330
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(0, 324, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 705
            wall.center_y = y
            self.wall_list.append(wall)

        # Edge of the map.

        for x in range(0, 2000, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 0
            self.wall_list.append(wall)
        for x in range(0, 2000, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 1025
            self.wall_list.append(wall)
        for y in range(0, 1025, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 1985
            wall.center_y = y
            self.wall_list.append(wall)
        for y in range(0, 1025, 64):
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = 0
            wall.center_y = y
            self.wall_list.append(wall)

        # --- Place walls with a list
        coordinate_list = [[709, 509],
                           [770, 509],
                           [709, 570],
                           [770, 570]]

        # Loop through coordinates
        for coordinate in coordinate_list:
            wall = arcade.Sprite("stoneCenter.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        for i in range(GEM_COUNT):

            gem = arcade.Sprite("gemBlue.png", SPRITE_SCALING_GEM)


            gem_placed_successfully = False

            # Keep trying until success
            while not gem_placed_successfully:
                # Position the gem
                gem.center_x = random.randrange(2000)
                gem.center_y = random.randrange(1000)

                # See if the gem is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)

                # See if the gem is hitting another gem
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:
                    # It is!
                    gem_placed_successfully = True

            # Add the gem to the lists
            self.gem_list.append(gem)

        # Creates physics engine
        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)

    def on_draw(self):
        arcade.start_render()

        # Select the scrolled camera for our sprites
        self.camera_for_sprites.use()

        # Draw the sprites
        self.wall_list.draw()
        self.player_list.draw()
        self.gem_list.draw()

        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()
        self.gem_list.update()

        hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.gem_list)
        for gem in hit_list:
            gem.remove_from_sprite_lists()
            self.score += 1
            arcade.play_sound(self.gem_sound)

        CAMERA_SPEED = 1
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
