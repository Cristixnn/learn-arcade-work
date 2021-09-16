import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600


def draw_grass():
    arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, SCREEN_HEIGHT / 3, 0, arcade.color.SKY_BLUE)


def draw_fin(x, y):
    arcade.draw_circle_filled(x, y, 5, arcade.csscolor.RED)
    arcade.draw_ellipse_filled(140 + x - 140, 190 + y - 190, 80, 50, arcade.csscolor.DIM_GRAY)
    arcade.draw_triangle_filled(120 + x - 140, 180 + y - 190, 170 + x - 140, 180 + y - 190, 125 + x - 140, 240 + y - 190, arcade.csscolor.DARK_GRAY)


def draw_cloud(x, y):
    arcade.draw_circle_filled(550 + x - 550, 420 + y - 420, 50, arcade.csscolor.WHITE)
    arcade.draw_circle_filled(500 + x - 550, 460 + y - 420, 50, arcade.csscolor.WHITE_SMOKE)
    arcade.draw_circle_filled(460 + x - 550, 420 + y - 420, 50, arcade.csscolor.GHOST_WHITE)
    arcade.draw_circle_filled(510 + x - 550, 390 + y - 420, 50, arcade.csscolor.WHITE_SMOKE)


def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

    draw_grass()
    draw_fin(50, 40)
    draw_fin(200, 150)
    draw_cloud(150, 500)
    draw_cloud(550, 450)
    draw_cloud(350, 400)
    draw_fin(400, 100)

 # Finish and run
    arcade.finish_render()
    arcade.run()

# Call the main function to get the program started.
main()