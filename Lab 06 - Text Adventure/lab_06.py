class Room:

    def __init__(self, description, north, east, south, west):
        """Directions"""
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west


def main():
    current_room = 0
    # Room 0
    room_list = []
    my_room = Room("You are in the patio, go inside the house north."
                   "\nKeep exploring east.", 3, 1, None, None)
    room_list.append(my_room)
    # Room 1
    room_list = []
    my_room = Room("You are in the middle of the yard.", None, 2, None, 0)
    room_list.append(my_room)
    # Room 2
    room_list = []
    my_room = Room("You are near the near a shack, want to go in?", None, None, None, 2)
    room_list.append(my_room)
    # Room 3
    room_list = []
    my_room = Room("You are in the living room.", 6, 4, 0, None)
    room_list.append(my_room)
    # Room 4
    room_list = []
    my_room = Room("You are in the south hall.", 7, 5, None, 3)
    room_list.append(my_room)
    # Room 5
    room_list = []
    my_room = Room("You are in bedroom1.", None, None, None, 4)
    room_list.append(my_room)
    # Room 6
    room_list = []
    my_room = Room("You are in the kitchen.", None, 7, 3, None)
    room_list.append(my_room)
    # Room 7
    room_list = []
    my_room = Room("You are on the north hall.", None, 8, 4, 6)
    room_list.append(my_room)
    # Room 8
    room_list = []
    my_room = Room("You are on the bedroom2.", None, None, None, 7)
    room_list.append(my_room)

    print(room_list[0])
    print(current_room)


main()
