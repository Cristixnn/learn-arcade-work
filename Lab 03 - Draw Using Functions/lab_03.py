import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_sun():
    """ this function makes the sun """
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


def draw_ocean():
    """  this function generates ocean """
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.SKY_BLUE)


def draw_fin(x, y):
    """ this function makes a sharks fin """
    arcade.draw_circle_filled(x, y, 5, arcade.csscolor.RED)
    arcade.draw_ellipse_filled(140 + x - 140, 190 + y - 190, 80, 50, arcade.csscolor.DIM_GRAY)
    arcade.draw_triangle_filled(120 + x - 140, 180 + y - 190, 170 + x - 140, 180 + y - 190, 125 + x - 140,
                                240 + y - 190, arcade.csscolor.DARK_GRAY)


def draw_cloud(x, y):
    """ this function creates a cloud """
    arcade.draw_circle_filled(550 + x - 550, 420 + y - 420, 50, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(500 + x - 550, 460 + y - 420, 50, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_circle_filled(460 + x - 550, 420 + y - 420, 50, arcade.csscolor.GHOST_WHITE)
    arcade.draw_circle_filled(510 + x - 550, 390 + y - 420, 50, arcade.csscolor.WHITE_SMOKE)


def draw_bird(x, y):
    """ this function generates a bird """
    arcade.draw_arc_filled(275 + x - 275, 555 + y - 555, 9, 9, arcade.csscolor.BLACK, 0, 360)
    arcade.draw_arc_outline(280 + x - 275, 537 + y - 555, 30, 40, arcade.csscolor.BLACK, 45, 120, 5)
    arcade.draw_arc_outline(268 + x - 275, 540 + y - 555, 30, 40, arcade.csscolor.BLACK, 45, 120, 5)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

    draw_sun()
    draw_ocean()
    draw_fin(50, 40)
    draw_fin(200, 150)
    draw_cloud(150, 500)
    draw_cloud(550, 450)
    draw_cloud(350, 400)
    draw_fin(400, 100)
    draw_bird(400, 300)
    draw_bird(500, 320)
    draw_bird(570, 340)
    draw_bird(300, 280)

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()
