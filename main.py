import game_setup
import welcome
import room_navigation
import game_display

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
        game_display.print_player(current_room, player_inventory)
        game_display.display_room_info(spacecraft_rooms, current_room)

        action = input('Enter your move (go North, South, East, West or Exit): ').lower()

        # Check if the action is a move command
        if action.startswith('go '):
            direction = action.split()[1].capitalize()
            current_room = room_navigation.move_player(spacecraft_rooms, current_room, direction)
        elif action == 'exit':
            print("Exiting the game...")
            break
        else:
            print("Invalid command! Please try again.")

if __name__ == '__main__':
    welcome.display_game_logo()
    game_play()
