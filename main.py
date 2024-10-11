import utilities
import welcome


def player_prompt(current_room, player_inventory):
    print(f"You are in the {current_room}\n Inventory: {player_inventory}\n{'-' * 27}")


def game_initialize():
    utilities.clear()
    print('Game initializing...')
    spacecraft_rooms = {
        'Crew Quarters': {
            'South': 'Medical Bay',
            'Item': None
        },
        'Medical bay': {
            'North': 'Crew Quarters',
            'South': 'Control Room',
            'East': 'Observation Deck',
            'Item': 'Nano Repair Kit'
        },
        'Control Room': {
            'North': 'Medical Bay',
            'South': 'Engine Room',
            'Item': 'Power Cell'
        },
        'Engine Room': {
            'North': 'Control Room',
            'East': 'Storage Bay',
            'Item': 'Energy Converter'
        },
        'Observation Deck': {
            'West': 'Medical Bay',
            'South': 'Weaponry Room',
            'Item': 'Command Key Card'
        },
        'Weaponry Room': {
            'North': 'Observation Deck',
            'South': 'Storage Bay',
            'Item': 'Laser Cannon Blueprint'
        },
        'Storage Bay': {
            'North': 'Weaponry Room',
            'South': 'Cargo Hold',
            'West': 'Engine Room',
            'Item': 'Shield Generator'
        },
        'Cargo Hold': {
            'North': 'Storage Bay',
            'item': None
        }
    }

    current_room = 'Crew Quarters'
    alien_room = 'Cargo Hold'
    player_inventory = []
    player_prompt(current_room, player_inventory)


if __name__ == '__main__':
    welcome.display_game_logo()
    game_initialize()
