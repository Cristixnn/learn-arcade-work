<<<<<<< HEAD
import arcade

WIDTH = 50
HEIGHT = 50
MARGIN = 5
COLUMN_COUNT = 10
ROW_COUNT = 10

=======
"""
Array Backed Grid

Show how to use a two-dimensional list/array to back the display of a
grid on-screen.
"""
import arcade

# Set how many rows and columns we will have
ROW_COUNT = 10
COLUMN_COUNT = 10

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20

# This sets the margin between each cell
# and on the edges of the screen.
MARGIN = 5

# Do the math to figure out our screen dimensions
>>>>>>> 2afb41a689d6e9ac7ced182c81c651a747f748cd
SCREEN_WIDTH = (WIDTH + MARGIN) * COLUMN_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN


class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
<<<<<<< HEAD
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)

        # Create grid of numbers
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)



        print(self.grid)
=======
        """
        Set up the application.
        """
        super().__init__(width, height)
        # Create a 2 dimensional array. A two dimensional
        # array is simply a list of lists.
        self.grid = []
        for row in range(ROW_COUNT):
            # Add an empty array that will hold each cell
            # in this row
            self.grid.append([])
            for column in range(COLUMN_COUNT):
                self.grid[row].append(0)  # Append a cell

        arcade.set_background_color(arcade.color.BLACK)
>>>>>>> 2afb41a689d6e9ac7ced182c81c651a747f748cd

    def on_draw(self):
        """
        Render the screen.
        """

<<<<<<< HEAD
        # Variable

        arcade.start_render()
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                x = WIDTH / 2 + column * (WIDTH + MARGIN) + MARGIN
                y = HEIGHT / 2 + row * (HEIGHT + MARGIN) + MARGIN
                if self.grid[row][column] == 0:
                    color = arcade.color.WHITE
                else:
                    color = arcade.color.GREEN

                arcade.draw_rectangle_filled(x, y,
                                             WIDTH, HEIGHT,
                                             color)
=======
        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw the grid
        for row in range(ROW_COUNT):
            for column in range(COLUMN_COUNT):
                # Figure out what color to draw the box
                if self.grid[row][column] == 1:
                    color = arcade.color.GREEN
                else:
                    color = arcade.color.WHITE

                # Do the math to figure out where the box is
                x = (MARGIN + WIDTH) * column + MARGIN + WIDTH // 2
                y = (MARGIN + HEIGHT) * row + MARGIN + HEIGHT // 2

                # Draw the box
                arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, color)
>>>>>>> 2afb41a689d6e9ac7ced182c81c651a747f748cd

    def on_mouse_press(self, x, y, button, modifiers):
        """
        Called when the user presses a mouse button.
        """

<<<<<<< HEAD
        row = y // (HEIGHT + MARGIN)
        column = x // (WIDTH + MARGIN)

        if row + 1 < ROW_COUNT and column < COLUMN_COUNT:

            if self.grid[row - 1][column] == 0:
                self.grid[row - 1][column] = 1
            else:
                self.grid[row - 1][column] = 0

        if row < ROW_COUNT and column < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column] == 0:
                self.grid[row][column] = 1
            else:
                self.grid[row][column] = 0
=======
        # Change the x/y screen coordinates to grid coordinates
        column = x // (WIDTH + MARGIN)
        row = y // (HEIGHT + MARGIN)

        print(f"Click coordinates: ({x}, {y}). Grid coordinates: ({row}, {column})")

        # Make sure we are on-grid. It is possible to click in the upper right
        # corner in the margin and go to a grid location that doesn't exist

        # Middle grid
        if self.grid[row][column] == 0:
            self.grid[row][column] = 1
        else:
            self.grid[row][column] = 0

        # Top grid
        if row + 1 < ROW_COUNT:
>>>>>>> 2afb41a689d6e9ac7ced182c81c651a747f748cd

            if self.grid[row + 1][column] == 0:
                self.grid[row + 1][column] = 1
            else:
                self.grid[row + 1][column] = 0

<<<<<<< HEAD








        print("click", row, column)
=======
        # Bottom grid
        if row - 1 > 0:

            # Flip the location between 1 and 0.
            if self.grid[row - 1][column] == 0:
                self.grid[row - 1][column] = 1
            else:
                self.grid[row - 1][column] = 0

        # Right grid
        if column + 1 < COLUMN_COUNT:

            # Flip the location between 1 and 0.
            if self.grid[row][column + 1] == 0:
                self.grid[row][column + 1] = 1
            else:
                self.grid[row][column + 1] = 0

        # Left grid
        if column - 1 > 0:

            # Flip the location between 1 and 0.
            if self.grid[row][column - 1] == 0:
                self.grid[row][column - 1] = 1
            else:
                self.grid[row][column - 1] = 0



>>>>>>> 2afb41a689d6e9ac7ced182c81c651a747f748cd


def main():
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()
