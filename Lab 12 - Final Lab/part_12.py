import random
import arcade

done = False
SPRITE_SCALING = 0.5

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 6

# Gem
SPRITE_SCALING_GEM = 0.5
GEM_COUNT = 50


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        map_name = "Jumpy.json"

        # Sprite lists
        self.tile_map = arcade.load_tilemap(map_name, scaling=SPRITE_SCALING)
        self.player_list = None
        self.wall_list = None

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        # Gem list
        self.score = 0
        self.gem_list = None
        self.camera_for_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

        self.gem_sound = arcade.load_sound("arcade_resources_sounds_coin2.wav")
        self.jump_sound = arcade.load_sound("arcade_resources_sounds_jump4.wav")
        self.background_sound = arcade.load_sound("arcade_resources_music_1918.mp3")
        arcade.play_sound(self.background_sound)

    def setup(self):
        """ Set up the game and initialize the variables. """

        self.gem_list = arcade.SpriteList()

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("slimePurple.png",
                                           scale=0.4)
        self.player_sprite.center_x = 600
        self.player_sprite.center_y = 100
        self.player_list.append(self.player_sprite)

        self.wall_list = self.tile_map.sprite_lists["Tile Layer 1"]

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=0.9)

        # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        for i in range(GEM_COUNT):

            gem = arcade.Sprite("gemBlue.png", SPRITE_SCALING_GEM)

            gem_placed_successfully = False

            # Keep trying until success
            while not gem_placed_successfully:
                # Position the gem
                gem.center_x = random.randrange(2000)
                gem.center_y = random.randrange(3000)

                # See if the gem is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(gem, self.wall_list)

                # See if the gem is hitting another gem
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.gem_list)

                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:
                    # It is!
                    gem_placed_successfully = True

            # Add the gem to the lists
            self.gem_list.append(gem)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.gem_list.draw()

        self.camera_for_gui.use()
        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)

        # Select the (scrolled) camera for our GUI
        self.camera_gui.use()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = 20
                arcade.play_sound(self.jump_sound)
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED

        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

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

        # Scroll the screen to the player
        self.scroll_to_player()

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
                   self.player_sprite.center_y - self.height / 2

        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
