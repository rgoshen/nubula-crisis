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


def check_adjacent_rooms_for_alien(current_room, rooms, alien_room):
    """
    Checks if the Alien Overlord is in one of the rooms adjacent to the player's current room.

    Parameters:
        current_room (str): The current room of the player.
        rooms (dict): A dictionary of rooms with their details.
        alien_room (str): The room where the Alien Overlord is located.

    Returns:
        bool: True if the Alien Overlord is in an adjacent room, False otherwise.
    """
    adjacent_rooms = rooms[current_room]['directions'].values()  # Get adjacent rooms based on available directions

    if alien_room in adjacent_rooms:
        print("You hear strange noises coming from a nearby room.")  # Print clue
        return True

    return False