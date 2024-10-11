import utilities
import welcome
import room_navigation


def print_player(current_room, player_inventory):
    print()
    print(f"You are in the {current_room}\n Inventory: {player_inventory}\n{'-' * 27}")


def game_initialize():
    utilities.clear()

    print('Game initializing...')

    spacecraft_rooms = {
        'Crew Quarters': {
            'directions': {'South': 'Medical Bay'},
            'Item': None
        },
        'Medical bay': {
            'directions': {
                'North': 'Crew Quarters',
                'South': 'Control Room',
                'East': 'Observation Deck'
            },
            'Item': 'Nano Repair Kit'
        },
        'Control Room': {
            'directions': {
                'North': 'Medical Bay',
                'South': 'Engine Room'
            },
            'Item': 'Power Cell'
        },
        'Engine Room': {
            'directions': {
                'North': 'Control Room',
                'East': 'Storage Bay'
            },
            'Item': 'Energy Converter'
        },
        'Observation Deck': {
            'directions': {
                'West': 'Medical Bay',
                'South': 'Weaponry Room',
            },
            'Item': 'Command Key Card'
        },
        'Weaponry Room': {
            'directions': {
                'North': 'Observation Deck',
                'South': 'Storage Bay',
            },
            'Item': 'Laser Cannon Blueprint'
        },
        'Storage Bay': {
            'directions': {
                'North': 'Weaponry Room',
                'South': 'Cargo Hold',
                'West': 'Engine Room',
            },
            'Item': 'Shield Generator'
        },
        'Cargo Hold': {
            'directions': {
                'North': 'Storage Bay',
            },
            'item': None
        }
    }

    # set starting room
    current_room = 'Crew Quarters'

    # set alien overlord starting room
    alien_room = 'Cargo Hold'

    return current_room, spacecraft_rooms, alien_room

def game_play():
    current_room, spacecraft_rooms, alien_room = game_initialize()
    player_inventory = []

    while True:
        print_player(current_room, player_inventory)

        action = input('Enter your move (go North, South, East, West): ').lower()

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
