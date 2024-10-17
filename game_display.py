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

def get_dynamic_prompt(current_room, rooms):
    """
    Generates a dynamic prompt based on the current room.

    This function checks the available directions in the current room,
    whether there is an item in the room, and always includes the 'inventory' and 'exit' options.

    Parameters:
        current_room (str): The name of the room the player is currently in.
        rooms (dict): A dictionary of rooms with their details.

    Returns:
        str: The dynamically generated prompt.
    """
    room_directions = rooms[current_room]['directions']
    available_directions = ", ".join(room_directions.keys())

    # Start the prompt with available directions
    prompt = f"Enter your move (go {available_directions}"

    # Add specific item action if there is an item in the room
    if rooms[current_room]['Item']:
        item = rooms[current_room]['Item']
        prompt += f", get {item}"

    # Always include inventory and exit options
    prompt += ", inventory, exit): "

    return prompt