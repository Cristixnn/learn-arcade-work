# Imports arcade
import arcade


def draw_section_outlines():
    # Draw squares on bottom
    arcade.draw_rectangle_outline(150, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 150, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 150, 300, 300, arcade.color.BLACK)

    # Draw squares on top
    arcade.draw_rectangle_outline(150, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(450, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(750, 450, 300, 300, arcade.color.BLACK)
    arcade.draw_rectangle_outline(1050, 450, 300, 300, arcade.color.BLACK)


def draw_section_1():
    # Draws section one
    for row in range(30):
        for column in range(30):
            x = column * 10 + 5
            y = row * 10 + 5
            (arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))


def draw_section_2():
    # Draws section two
    for row in range(30):
        for column in range(30):
            x = column * 10 + 305
            y = row * 10 + 5
            if column % 2 == 0:
                (arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))
            else:
                (arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK))


def draw_section_3():
    # Draws section three
    for row in range(30):
        for column in range(30):
            x = column * 10 + 605
            y = row * 10 + 5
            if row % 2 == 0:
                (arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))
            else:
                (arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK))


def draw_section_4():
    # Draws section four
    for row in range(30):
        for column in range(30):
            x = column * 10 + 905
            y = row * 10 + 5
            if row % 2 == 0 and column % 2 == 0:
                (arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))
            else:
                (arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.BLACK))


def draw_section_5():
    # Draws section five
    for column in range(30):
        for row in range(column + 1):
            x = column * 10 + 15
            y = row * 10 + 305
            (arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))


def draw_section_6():
    # Draws section six
    for row in range(30):
        for column in range(30 - row):
            x = column * 10 + 305
            y = row * 10 + 305
            (arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))


def draw_section_7():
    # Draws section seven
    for row in range(30):
        for column in range(1 + row):
            x = column * 10 + 605
            y = row * 10 + 305
            (arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE))


def draw_section_8():
    # Draws section eight
    for row in range(30):
        for column in range(row + 2):
            x = (30 - column) * 10 + 905
            y = row * 10 + 305
            arcade.draw_rectangle_filled(x, y, 5, 5, arcade.color.WHITE)


def main():
    # Create a window
    arcade.open_window(1200, 600, "Lab 05 - Loopy Lab")
    arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    arcade.start_render()

    # Draw the outlines for the sections
    draw_section_outlines()

    # Draw the sections
    draw_section_1()
    draw_section_2()
    draw_section_3()
    draw_section_4()
    draw_section_5()
    draw_section_6()
    draw_section_7()
    draw_section_8()

    arcade.finish_render()

    arcade.run()


main()
