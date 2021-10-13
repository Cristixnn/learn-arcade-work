class Room:

    def __init__(self, description, north, east, south, west):
        """Directions"""
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


# Main function
def main():
    print("Hello there!")
    print("You have just purchased your new home!")
    print("Search all of the property and explore your new home, enjoy!\n")
    # Variable
    current_room = 0
    # Room 0
    room_list = []
    my_room = Room("You are in the patio outside."
                   "\nGo north to enter the house or go east to explore the backyard", 3, 1, None, None)
    room_list.append(my_room)

    # Room 1
    my_room = Room("You are in the middle of the yard, lots of space for your pets!"
                   "\nYou see a small shack to the east, return to patio by going west. ", None, 2, None, 0)
    room_list.append(my_room)

    # Room 2
    my_room = Room("You see a shack! Its locked, that's strange."
                   "\nGo back to the middle yard by going west.", None, None, None, 2)
    room_list.append(my_room)

    # Room 3
    my_room = Room("You are in the living room, where will you put the coffee table?"
                   "\nYou see the kitchen north and the south hall to the east.", 6, 4, 0, None)
    room_list.append(my_room)

    # Room 4
    my_room = Room("You are in the south hall."
                   "\nYou can go to the north hall by going north, you see a bedroom to your east."
                   "\nOr you can go back to the living room west.", 7, 5, None, 3)
    room_list.append(my_room)

    # Room 5
    my_room = Room("You are in the bedroom, its dark and empty in here."
                   "\nReturn back into the south hall west.", None, None, None, 4)
    room_list.append(my_room)

    # Room 6
    my_room = Room("You are in the kitchen. Empty fridge, might need to start stocking soon."
                   "\nGo east to the north hall, or go south to the living room.", None, 7, 3, None)
    room_list.append(my_room)

    # Room 7
    my_room = Room("You are on the north hall."
                   "\nYou can go to the kitchen east, you see a door to the east."
                   "\nAnd you can go to south hall going south", None, 8, 4, 6)
    room_list.append(my_room)

    # Room 8
    my_room = Room("You are in the master bedroom, spacious but empty."
                   "\nReturn back to the north hall by going west.", None, None, None, 7)
    room_list.append(my_room)

    done = False

    while not done:

        # User choice
        print(room_list[current_room].description)
        user_choice = input("\nWhat direction. ")

        # User options
        # If user quits
        if user_choice.upper() == "QUIT" or user_choice.upper() == "Q":
            print("you have quit the game.")
            done = True

        # If user wants to go north
        elif user_choice.upper() == "NORTH" or user_choice.upper() == "N":
            next_room = room_list[current_room].north
            if next_room is None:
                print()
                print("\nYou cant go there.")
            else:
                current_room = next_room

        # If user wants to go east
        elif user_choice.upper() == "EAST" or user_choice.upper() == "E":
            next_room = room_list[current_room].east
            if next_room is None:
                print()
                print("\nYou cant go there.")
            else:
                current_room = next_room

        # If user wants to go south
        elif user_choice.upper() == "SOUTH" or user_choice.upper() == "S":
            next_room = room_list[current_room].south
            if next_room is None:
                print()
                print("\nYou cant go there.")
            else:
                current_room = next_room

        # If user wants to go west
        elif user_choice.upper() == "WEST" or user_choice.upper() == "W":
            next_room = room_list[current_room].west
            if next_room is None:
                print()
                print("\nYou cant go there.")
            else:
                current_room = next_room


# Main function
main()