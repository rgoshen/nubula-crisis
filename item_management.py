def get_item(current_room, rooms, item_name, player_inventory):
    """
    Allows the player to collect an item from the current room if it exists.

    Parameters:
        current_room (str): The room where the player is currently located.
        rooms (dict): The dictionary containing all rooms and their contents.
        item_name (str): The name of the item the player wants to collect.
        player_inventory (list): The player's current inventory.

    Returns:
        bool: Returns True if the item was collected successfully, False otherwise.
    """
    # Check if the item exists in the current room and matches the item name
    if rooms[current_room]['Item'] and rooms[current_room]['Item'].lower() == item_name.lower():
        # Add the item to the player's inventory
        player_inventory.append(rooms[current_room]['Item'])
        # Remove the item from the room
        rooms[current_room]['Item'] = None
        print(f"You have collected the {item_name.capitalize()}.")
        return True
    else:
        print("There is no such item in this room or the command is invalid.")
        return False


def display_inventory(player_inventory):
    """
    Displays the player's inventory.

    Parameters:
        player_inventory (list): A list containing the player's current items.

    Returns:
        None
    """
    if player_inventory:
        print(f"Your inventory contains: {', '.join(player_inventory)}")
    else:
        print("Your inventory is empty.")