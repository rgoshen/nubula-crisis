def print_player(current_room):
    """
    Displays the player's current room.

    Parameters:
        current_room (str): The name of the room the player is currently in.
    """
    print()
    print(f"You are in the {current_room}\n {'-' * 27}")

def display_room_info(rooms, current_room):
    """
    Displays the description, directions, and available item in the current room.

    Parameters:
        rooms (dict): A dictionary mapping each room to its possible exits (directions).
        current_room (str): The name of the current room.
    """
    room_info = rooms[current_room]

    print()

    # Display the room description
    print(room_info['description'])

    # Display possible directions
    print("You can move in the following directions: ", ", ".join(room_info['directions'].keys()))

    # Display the item in the room (if any)
    if room_info['Item']:
        print(f"You see a {room_info['Item']} here.")
        print()
    else:
        print("There are no items in this room.")
        print()