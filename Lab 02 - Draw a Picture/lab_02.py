"""
 Beach
"""

# Imports arcade library
import arcade

# Opens up window
arcade.open_window(600, 600, "Drawing Example")

# Background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Ready to draw
arcade.start_render()

# Sun
arcade.draw_circle_filled(40, 380, 90, arcade.csscolor.YELLOW)
arcade.draw_triangle_filled(45, 550,
                            30, 480,
                            60, 480, arcade.csscolor.ORANGE)
arcade.draw_triangle_filled(175, 520,
                            100, 470,
                            125, 445, arcade.csscolor.ORANGE)
arcade.draw_triangle_filled(235, 410,
                            140, 430,
                            140, 400, arcade.csscolor.ORANGE)
arcade.draw_line(80, 480, 100, 540, arcade.csscolor.YELLOW, 4)
arcade.draw_line(135, 440, 220, 460, arcade.csscolor.YELLOW, 4)

# Cloud
arcade.draw_circle_filled(550, 420, 70, arcade.csscolor.WHITE)
arcade.draw_circle_filled(500, 480, 70, arcade.csscolor.WHITE_SMOKE)
arcade.draw_circle_filled(450, 440, 80, arcade.csscolor.GHOST_WHITE)
arcade.draw_circle_filled(400, 420, 70, arcade.csscolor.WHITE)
arcade.draw_circle_filled(350, 380, 70, arcade.csscolor.GHOST_WHITE)
arcade.draw_circle_filled(310, 390, 60, arcade.csscolor.WHITE_SMOKE)

# Ocean
arcade.draw_lrtb_rectangle_filled(0, 600, 401, 0, arcade.csscolor.DEEP_SKY_BLUE)
arcade.draw_triangle_filled(250, 400,
                            0, 400,
                            0, 100, arcade.csscolor.DODGER_BLUE)
arcade.draw_ellipse_filled(190, 392, 200, 18, arcade.csscolor.DODGER_BLUE)
arcade.draw_ellipse_filled(220, 385, 200, 30, arcade.csscolor.DODGER_BLUE)
arcade.draw_ellipse_filled(200, 365, 200, 50, arcade.csscolor.DODGER_BLUE)
arcade.draw_ellipse_filled(190, 330, 200, 50, arcade.csscolor.DODGER_BLUE)
arcade.draw_ellipse_filled(190, 290, 200, 80, arcade.csscolor.DODGER_BLUE)
arcade.draw_ellipse_filled(150, 250, 200, 80, arcade.csscolor.DODGER_BLUE)
arcade.draw_ellipse_filled(130, 210, 200, 80, arcade.csscolor.DODGER_BLUE)
arcade.draw_ellipse_filled(95, 170, 200, 80, arcade.csscolor.DODGER_BLUE)
arcade.draw_ellipse_filled(0, 120, 200, 80, arcade.csscolor.DODGER_BLUE)

# Shark fins
arcade.draw_ellipse_filled(140, 190, 80, 50, arcade.csscolor.DIM_GRAY)
arcade.draw_triangle_filled(120, 180, 170, 180, 125, 240, arcade.csscolor.DARK_GRAY)

arcade.draw_ellipse_filled(140, 60, 80, 50, arcade.csscolor.DIM_GRAY)
arcade.draw_triangle_filled(120, 50, 160, 50, 160, 100, arcade.csscolor.DARK_GRAY)

# Beach sand
arcade.draw_lrtb_rectangle_filled(400, 600, 400, 0, arcade.csscolor.BEIGE)
arcade.draw_ellipse_filled(400, 200, 90, 400, arcade.csscolor.BEIGE)
arcade.draw_arc_filled(460, 100, 5, 5, arcade.csscolor.SIENNA, 0, 360)
arcade.draw_arc_filled(480, 100, 5, 5, arcade.csscolor.SIENNA, 0, 360)
arcade.draw_arc_filled(430, 100, 5, 5, arcade.csscolor.SIENNA, 0, 360)
arcade.draw_arc_filled(460, 130, 5, 5, arcade.csscolor.SIENNA, 0, 360)
arcade.draw_arc_filled(420, 70, 5, 5, arcade.csscolor.SIENNA, 0, 360)
arcade.draw_arc_filled(490, 60, 5, 5, arcade.csscolor.SIENNA, 0, 360)
arcade.draw_arc_filled(450, 40, 5, 5, arcade.csscolor.SIENNA, 0, 360)
arcade.draw_arc_filled(460, 60, 5, 5, arcade.csscolor.SIENNA, 0, 360)


# Patch of grass
arcade.draw_circle_filled(630, 50, 100, arcade.csscolor.DARK_GREEN)
arcade.draw_circle_filled(580, -20, 100, arcade.csscolor.GREEN)

# Shark sign
arcade.draw_line(410, 200, 410, 250, arcade.csscolor.SIENNA, 7)
arcade.draw_polygon_filled([[360, 290],
                            [380, 250],
                            [440, 250],
                            [460, 290],
                           [410, 330]], arcade.color.BROWN)
arcade.draw_polygon_outline([[360, 290],
                            [380, 250],
                            [440, 250],
                            [460, 290],
                            [410, 330]], arcade.color.WHITE_SMOKE, 5)
arcade.draw_text("SHARKS", 375, 280, arcade.color.WHITE, 13)

# Edge
arcade.draw_lrtb_rectangle_outline(0, 600, 401, 0, arcade.csscolor.BLACK, 1)

# Beach hut
arcade.draw_lrtb_rectangle_filled(480, 580, 420, 350, arcade.csscolor.SIENNA)
arcade.draw_triangle_filled(470, 420, 590, 420, 530, 460, arcade.csscolor.SADDLE_BROWN)
arcade.draw_arc_filled(530, 350, 40, 70, arcade.csscolor.BLACK, 0, 180)

# finish drawing
arcade.finish_render()

# keep window up until someone closes it.
arcade.run()
