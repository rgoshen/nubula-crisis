def move_player(rooms, current_room, direction):
    """
    Moves the player between rooms based on the direction input.

    Parameters:
        rooms (dict): A dictionary mapping each room to its possible exits (directions).
        current_room (str): The room where the player currently is.
        direction (str): The direction in which the player wants to move (e.g., 'North', 'South', 'East', 'West').

    Returns:
        str: The new room the player has moved to, or the current room if the move is invalid.
    """
    # Check if the direction is valid from the current room
    if direction in rooms[current_room]['directions']:
        # Move to the new room
        new_room = rooms[current_room]['directions'][direction]
        return new_room
    else:
        # Invalid direction, stay in the current room
        print("You can't go that way!")
        return current_room
