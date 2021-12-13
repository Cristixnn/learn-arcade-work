<<<<<<< HEAD
import re


# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)
=======
import random
import arcade

# --- Constants ---
done = False
SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_GEMS = 0.3
GEM_COUNT = 50
ROCK_COUNT = 30
MOVEMENT_SPEED = 2

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Gem(arcade.Sprite):

    def reset_pos(self):
        self.center_y = random.randrange(SCREEN_HEIGHT + 50,
                                         SCREEN_HEIGHT + 100)
        self.change_x = random.randrange(SCREEN_WIDTH)

    def update(self):
        self.center_y -= 0.5

        if self.top < 0:
            self.reset_pos()


class Rock(arcade.Sprite):

    def reset_pos(self):
        self.center_x = random.randrange(SCREEN_WIDTH + 50,
                                         SCREEN_WIDTH + 100)
        self.change_x = random.randrange(SCREEN_HEIGHT)

    def update(self):
        self.center_x -= 1

        if self.left < -1:
            self.reset_pos()


class MyGame(arcade.Window):
    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 08 - Sprites")

        # Variables that will hold sprite lists
        self.player_list = None
        self.gem_list = None
        self.rock_list = None

        # Set up the player info
        self.player_sprite = None
        self.score = 0

        # Don't show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.BLACK)

        # Sound effect from Arcade resource's
        self.gem_sound = arcade.load_sound("arcade_resources_sounds_coin4.wav")
        self.rock_sound = arcade.load_sound("arcade_resources_sounds_error2.wav")

    def setup(self):

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.gem_list = arcade.SpriteList()
        self.rock_list = arcade.SpriteList()

        # Score
        self.score = 0

        # Set up the player
        # Character image from Arcade resource's
        self.player_sprite = arcade.Sprite("playerShip2_orange.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        # Create the gems
        for i in range(GEM_COUNT):
            # Create the gem instance
            # Gem image from arcade library
            gem = Gem("gemBlue.png", SPRITE_SCALING_GEMS / 3)

            # Position the gem
            gem.center_x = random.randrange(SCREEN_WIDTH)
            gem.center_y = random.randrange(SCREEN_HEIGHT)
            gem.change_x = random.randrange(-3, 4)
            gem.change_y = random.randrange(-3, 4)

            # Add the gem to the lists
            self.gem_list.append(gem)

        for i in range(ROCK_COUNT):
            rock = Rock("meteorGrey_big3.png", SPRITE_SCALING_GEMS)
            rock.center_x = random.randrange(SCREEN_WIDTH)
            rock.center_y = random.randrange(SCREEN_HEIGHT)
            rock.change_x = random.randrange(-3, 4)
            rock.change_y = random.randrange(-3, 4)
            self.rock_list.append(rock)

    def on_draw(self):
        """ Draw everything """
        arcade.start_render()
        self.gem_list.draw()
        self.rock_list.draw()
        self.player_list.draw()

        if len(self.gem_list) == 0:
            arcade.draw_text("GAME OVER", 40, 300, arcade.color.WHITE, 90)

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """ Handle Mouse Motion """
        if len(self.gem_list) > 0:



            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time):
        if len(self.gem_list) > 0:

            """ Movement and game logic """

            # Call update on all sprites (The sprites don't do much in this
            # example though.)
            self.player_sprite.update()
            self.gem_list.update()
            self.rock_list.update()

            # Generate a list of all sprites that collided with the player.
            hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.gem_list)
            # Loop through each colliding sprite, remove it, and add to the score.
            for gem in hit_list:
                gem.remove_from_sprite_lists()
                self.score += 1
                arcade.play_sound(self.gem_sound)

            hit_list = arcade.check_for_collision_with_list(self.player_sprite,
                                                            self.rock_list)
            for rock in hit_list:
                rock.remove_from_sprite_lists()
                self.score -= 1
                arcade.play_sound(self.rock_sound)




    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
>>>>>>> 2afb41a689d6e9ac7ced182c81c651a747f748cd
