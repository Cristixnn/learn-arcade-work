import arcade

""" Variables"""
MOVEMENT_SPEED = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Bird:
    def __init__(self, position_x, position_y):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = 0
        self.change_y = 0
        self.error_sound = arcade.load_sound("arcade_resources_sounds_error2.wav")

    def update(self):
        # Moves bird
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the bird hits the edge of the screen, change direction

        size = 10
        if self.position_x < size:
            arcade.play_sound(self.error_sound)
            self.position_x = size

        if self.position_x > SCREEN_WIDTH - size:
            arcade.play_sound(self.error_sound)
            self.position_x = SCREEN_WIDTH - size

        if self.position_y < size:
            arcade.play_sound(self.error_sound)
            self.position_y = size

        if self.position_y > SCREEN_HEIGHT - size:
            arcade.play_sound(self.error_sound)
            self.position_y = SCREEN_HEIGHT - size

    def draw(self):
        """ this function generates a bird """
        arcade.draw_circle_filled(self.position_x, self.position_y,
                                  6, arcade.csscolor.BLACK)

        arcade.draw_arc_outline(self.position_x + 5, self.position_y - 18,
                                30, 40, arcade.csscolor.BLACK, 45, 120, 5)

        arcade.draw_arc_outline(self.position_x - 7, self.position_y - 15,
                                30, 40, arcade.csscolor.BLACK, 45, 120, 5)


class Kite:
    def __init__(self, position_x, position_y):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y

        self.change_x = 0
        self.change_y = 0
        self.error_sound = arcade.load_sound("arcade_resources_sounds_error2.wav")

    def draw(self):
        """ Draw the kite with the instance variables we have. """
        arcade.draw_triangle_filled(self.position_x, self.position_y,
                                    self.position_x + 70, self.position_y,
                                    self.position_x + 40, self.position_y + 40, arcade.color.RED)

        arcade.draw_triangle_filled(self.position_x, self.position_y,
                                    self.position_x + 70, self.position_y,
                                    self.position_x + 40, self.position_y - 40, arcade.color.DARK_RED)

        arcade.draw_line(self.position_x + 40, self.position_y - 40,
                         self.position_x + 90, self.position_y - 80, arcade.color.BROWN, 4)

    def update(self):
        # Move the kite
        self.position_y += self.change_y
        self.position_x += self.change_x

        self.error_sound = arcade.load_sound("arcade_resources_sounds_error2.wav")

        # See if the kite hit the edge of the screen. If so, change direction


        if self.position_x < self.change_x:
            arcade.play_sound(self.error_sound)
            self.position_x = self.change_x + 5

        if self.position_x > SCREEN_WIDTH - self.change_x:
            arcade.play_sound(self.error_sound)
            self.position_x = SCREEN_WIDTH - self.change_x - 70

        if self.position_y < self.change_y:
            arcade.play_sound(self.error_sound)
            self.position_y = self.change_y + 70

        if self.position_y > SCREEN_HEIGHT - self.change_y:
            arcade.play_sound(self.error_sound)
            self.position_y = SCREEN_HEIGHT - self.change_y - 10


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Create our kite
        self.kite = Kite(40, 500)
        self.bird = Bird(100, 100)

        self.hit_sound = arcade.load_sound("arcade_resources_sounds_hit1.wav")
        self.error_sound = arcade.load_sound("arcade_resources_sounds_error2.wav")

    def on_draw(self):
        def draw_grass():
            """  this function generates ocean """
            arcade.draw_lrtb_rectangle_filled(0, 800, 600 / 3, 0, arcade.color.FERN_GREEN)

        def draw_cloud(x, y):
            """ this function creates a cloud """
            arcade.draw_circle_filled(550 + x - 550, 420 + y - 420, 50, arcade.csscolor.WHITE)
            arcade.draw_circle_filled(500 + x - 550, 460 + y - 420, 50, arcade.csscolor.WHITE_SMOKE)
            arcade.draw_circle_filled(460 + x - 550, 420 + y - 420, 50, arcade.csscolor.GHOST_WHITE)
            arcade.draw_circle_filled(510 + x - 550, 390 + y - 420, 50, arcade.csscolor.WHITE_SMOKE)

        def draw_sun():
            """ this function draws the sun """
            arcade.draw_circle_filled(40, 180, 90, arcade.csscolor.YELLOW)
            arcade.draw_triangle_filled(45, 350,
                                        30, 280,
                                        60, 280, arcade.csscolor.ORANGE)
            arcade.draw_triangle_filled(175, 320,
                                        100, 270,
                                        125, 245, arcade.csscolor.ORANGE)
            arcade.draw_triangle_filled(235, 210,
                                        140, 230,
                                        140, 200, arcade.csscolor.ORANGE)
            arcade.draw_line(80, 280, 100, 340, arcade.csscolor.YELLOW, 4)
            arcade.draw_line(135, 240, 220, 260, arcade.csscolor.YELLOW, 4)

        # Calls function
        arcade.start_render()
        draw_sun()
        draw_cloud(200, 400)
        draw_cloud(500, 500)
        draw_cloud(700, 300)
        draw_grass()
        self.bird.draw()
        self.kite.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.bird.position_x = x
        self.bird.position_y = y

    def on_mouse_press(self, x, y, button, modifiers):
        """ If player press mouse button, a sound plays."""
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.hit_sound)
        elif button == arcade.MOUSE_BUTTON_RIGHT:
            arcade.play_sound(self.hit_sound)

    def update(self, delta_time):
        self.kite.update()
        self.bird.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.kite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.kite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.kite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.kite.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.kite.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.kite.change_y = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
    arcade.run()


main()
