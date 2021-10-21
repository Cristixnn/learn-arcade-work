import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_bird(x, y):
    """ this function generates a bird """
    arcade.draw_arc_filled(275 + x - 275, 555 + y - 555, 9, 9, arcade.csscolor.BLACK, 0, 360)
    arcade.draw_arc_outline(280 + x - 275, 537 + y - 555, 40, 5-0, arcade.csscolor.BLACK, 45, 120, 5)
    arcade.draw_arc_outline(268 + x - 275, 540 + y - 555, 40, 50, arcade.csscolor.BLACK, 45, 120, 5)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

    draw_bird(400, 300)
    draw_bird(500, 320)
    draw_bird(570, 340)
    draw_bird(300, 280)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
