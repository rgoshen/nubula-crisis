def check_alien_encounter(current_room, alien_room):
    """
    Checks if the player is in the same room as the Alien Overlord.

    Parameters:
        current_room (str): The room where the player is currently located.
        alien_room (str): The room where the Alien Overlord is located.

    Returns:
        bool: Returns True if the player encounters the Alien Overlord, otherwise False.
    """
    return current_room == alien_room