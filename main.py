import game_setup
import welcome
import room_navigation
import game_display
import item_management

def game_play():
    """
    The main game loop for 'Nebula Crisis: Overlord Showdown'.

    This function initializes the game by calling the setup functions to assign the player's starting room,
    the Alien Overlord's starting room, and randomize item placements. It continuously prompts the player
    for input to either move between rooms, collect items, or exit the game.

    The player's movement is handled by checking valid directions, and inventory is updated as items are collected.
    If the player chooses to exit, the game will end. The game loop continues until the player exits.

    This function relies on other modules for displaying game information, navigating between rooms,
    and managing game setup.

    Parameters:
        None

    Returns:
        None
    """
    current_room, spacecraft_rooms, alien_room = game_setup.game_initialize()
    player_inventory = []

    while True:
        # Print player's location and inventory
        game_display.print_player(current_room)
        game_display.display_room_info(spacecraft_rooms, current_room)

        # Prompt the player for action
        action = input('Enter your move (go North, South, East, West or get <item> or Exit): ').lower()

        # Handle the 'go' command for movement
        if action.startswith('go '):
            direction = action.split()[1].capitalize()
            current_room = room_navigation.move_player(spacecraft_rooms, current_room, direction)

        # Handle the 'get' command for collecting items
        elif action.startswith('get '):
            item_name = action.split('get ', 1)[1].strip()
            item_management.get_item(current_room, spacecraft_rooms, item_name, player_inventory)

        # Handle the 'inventory' command to view player's inventory
        elif action == 'inventory':
            item_management.display_inventory(player_inventory)

        # Handle the 'exit' command to quit the game
        elif action == 'exit':
            print("Exiting the game...")
            break

        # Invalid command
        else:
            print("Invalid command! Please try again.")

if __name__ == '__main__':
    welcome.display_game_logo()
    game_play()
