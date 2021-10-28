import arcade

MOVEMENT_SPEED = 5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Player:
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        # Take the parameters of the init function above,
        # and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """

        def setup(self):
            """ Set up the game and initialize the variables. """

    def update(self):
        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < self.radius:
            self.position_x = self.radius

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.position_x = SCREEN_WIDTH - self.radius

        if self.position_y < self.radius:
            self.position_y = self.radius

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.position_y = SCREEN_HEIGHT - self.radius


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Make the mouse disappear when it is over the window.
        # So we just see our object, not the pointer.
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Create our ball
        self.ball = Player(50, 50, 0, 0, 15, arcade.color.AUBURN)

    def on_draw(self):
        """ Called whenever we need to draw the window. """

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

        def draw_grass():
            """  this function generates grass """
            arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.FERN_GREEN)

        def draw_cloud(x, y):
            """ this function creates a cloud """
            arcade.draw_circle_filled(550 + x - 550, 420 + y - 420, 50, arcade.csscolor.WHITE)
            arcade.draw_circle_filled(500 + x - 550, 460 + y - 420, 50, arcade.csscolor.WHITE_SMOKE)
            arcade.draw_circle_filled(460 + x - 550, 420 + y - 420, 50, arcade.csscolor.GHOST_WHITE)
            arcade.draw_circle_filled(510 + x - 550, 390 + y - 420, 50, arcade.csscolor.WHITE_SMOKE)


        arcade.start_render()
        draw_cloud(200, 400)
        draw_cloud(600, 500)
        draw_sun()
        draw_grass()
        self.ball.draw()

    def on_mouse_motion(self, x, y, dx, dy):
        """ Called to update our objects.
        Happens approximately 60 times per second."""
        self.ball.position_x = x
        self.ball.position_y = y

    def update(self, delta_time):
        self.ball.update()

    def on_key_press(self, key, modifiers):
        """ Called whenever the user presses a key. """
        if key == arcade.key.LEFT:
            self.ball.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.ball.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.ball.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.ball.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """ Called whenever a user releases a key. """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.ball.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.ball.change_y = 0


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
    arcade.run()



main()
