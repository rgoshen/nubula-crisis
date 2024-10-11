import game_setup
import welcome
import room_navigation
import game_display
import item_management
import game_logic

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
    """
    current_room, spacecraft_rooms, alien_room, placed_items = game_setup.game_initialize()
    player_inventory = []

    # Total number of items in the game
    total_items = len(placed_items)

    while True:
        # Check if the player encounters the Alien Overlord
        if game_logic.check_alien_encounter(current_room, alien_room):
            if game_logic.check_all_items_collected(player_inventory, placed_items):
                print(
                    "\nYou have collected all the required items and activated the ship's defense system!")
                print("Congratulations! You have defeated the Alien Overlord and saved the ship!")
            else:
                missing_items = set(placed_items) - set(player_inventory)  # Calculate the missing items
                print("\nOh no! ZAP! ZAP! The Alien Overlord has won and taken over the ship.")
                print(f"You failed to collect the following items: {', '.join(missing_items)}. Game Over!")
            break  # Exit the game loop


        # Print player's location and inventory
        game_display.print_player(current_room)
        game_display.display_room_info(spacecraft_rooms, current_room)

        # Check if alien is in an adjacent room and give clue (only if the player has not encountered the alien)
        game_logic.check_adjacent_rooms_for_alien(current_room, spacecraft_rooms, alien_room)

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
            item_management.display_inventory(player_inventory, total_items)

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
