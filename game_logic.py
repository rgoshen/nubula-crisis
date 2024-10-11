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

def check_all_items_collected(player_inventory, required_items):
    """
    Checks if the player has collected all the required items.

    Parameters:
        player_inventory (list): The player's current inventory.
        required_items (list): The list of required items to complete the game.

    Returns:
        bool: Returns True if the player has all the required items, otherwise False.
    """
    return set(required_items).issubset(set(player_inventory))