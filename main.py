import utilities
import welcome
import room_navigation


def print_player(current_room, player_inventory):
    print()
    print(f"You are in the {current_room}\n Inventory: {player_inventory}\n{'-' * 27}")

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

def game_initialize():
    utilities.clear()

    print('Game initializing...')

    spacecraft_rooms = {
    'Crew Quarters': {
        'description': "The Crew Quarters is where the ship's crew used to rest. It's quiet now, but something seems off.",
        'directions': {'South': 'Medical Bay'},
        'Item': None
    },
    'Medical Bay': {
        'description': "This is the Medical Bay, full of equipment to treat injuries.",
        'directions': {
            'North': 'Crew Quarters',
            'South': 'Control Room',
            'East': 'Observation Deck'
        },
        'Item': 'Nano Repair Kit'
    },
    'Control Room': {
        'description': "The Control Room is the heart of the ship. There are flashing lights and a strange hum.",
        'directions': {
            'North': 'Medical Bay',
            'South': 'Engine Room'
        },
        'Item': 'Power Cell'
    },
    'Engine Room': {
        'description': "You are in the Engine Room. The sound of machinery surrounds you.",
        'directions': {
            'North': 'Control Room',
            'East': 'Storage Bay'
        },
        'Item': 'Energy Converter'
    },
    'Observation Deck': {
        'description': "The Observation Deck provides a view of the stars.",
        'directions': {
            'West': 'Medical Bay',
            'South': 'Weaponry Room',
        },
        'Item': 'Command Key Card'
    },
    'Weaponry Room': {
        'description': "This is the Weaponry Room, filled with tools of defense.",
        'directions': {
            'North': 'Observation Deck',
            'South': 'Storage Bay',
        },
        'Item': 'Laser Cannon Blueprint'
    },
    'Storage Bay': {
        'description': "The Storage Bay is packed with supplies.",
        'directions': {
            'North': 'Weaponry Room',
            'South': 'Cargo Hold',
            'West': 'Engine Room',
        },
        'Item': 'Shield Generator'
    },
    'Cargo Hold': {
        'description': "The Cargo Hold is dark and eerie.",
        'directions': {
            'North': 'Storage Bay',
        },
        'Item': None
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
        display_room_info(spacecraft_rooms, current_room)

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
