import random
import utilities

def randomize_game(rooms, items):
    """
    Randomly assigns the player's starting room, the Alien Overlord's starting room,
    and places the six items in random rooms, excluding the starting rooms of the player and alien.

    Returns:
        player_start_room (str): The player's starting room.
        alien_start_room (str): The Alien Overlord's starting room.
        placed_items (list): A list of items that were placed in the rooms.
    """
    room_names = list(rooms.keys())

    # Randomly assign player's starting room
    player_start_room = random.choice(room_names)

    # List of valid starting locations for the Alien Overlord (excluding Medical Bay and Storage Bay)
    valid_alien_rooms = [room for room in room_names if room not in ['Medical Bay', 'Storage Bay']]

    # Randomly assign Alien Overlord's starting room (must be different from player start)
    alien_start_room = random.choice(valid_alien_rooms)
    while alien_start_room == player_start_room:
        alien_start_room = random.choice(valid_alien_rooms)

    # List of rooms where items can be placed (excluding player and alien start rooms)
    available_rooms = [room for room in room_names if room not in [player_start_room, alien_start_room]]

    # Shuffle and assign items to available rooms
    placed_items = []  # Track items that are placed in rooms
    random.shuffle(items)
    for i, room in enumerate(available_rooms[:len(items)]):
        rooms[room]['Item'] = items[i]
        placed_items.append(items[i])  # Add placed item to the list

    return player_start_room, alien_start_room, placed_items

def game_initialize():
    """
    Initializes the game by setting up the rooms, items, and randomly assigning
    the player and alien starting locations, as well as randomizing item placements.

    Returns:
        current_room (str): The player's starting room.
        spacecraft_rooms (dict): The dictionary of rooms in the game.
        alien_room (str): The room where the Alien Overlord is located.
        placed_items (list): A list of items that were placed in the rooms.
    """
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
            'Item': None
        },
        'Control Room': {
            'description': "The Control Room is the heart of the ship. There are flashing lights and a strange hum.",
            'directions': {
                'North': 'Medical Bay',
                'South': 'Engine Room'
            },
            'Item': None
        },
        'Engine Room': {
            'description': "You are in the Engine Room. The sound of machinery surrounds you.",
            'directions': {
                'North': 'Control Room',
                'East': 'Storage Bay'
            },
            'Item': None
        },
        'Observation Deck': {
            'description': "The Observation Deck provides a view of the stars.",
            'directions': {
                'West': 'Medical Bay',
                'South': 'Weaponry Room',
            },
            'Item': None
        },
        'Weaponry Room': {
            'description': "This is the Weaponry Room, filled with tools of defense.",
            'directions': {
                'North': 'Observation Deck',
                'South': 'Storage Bay',
            },
            'Item': None
        },
        'Storage Bay': {
            'description': "The Storage Bay is packed with supplies.",
            'directions': {
                'North': 'Weaponry Room',
                'South': 'Cargo Hold',
                'West': 'Engine Room',
            },
            'Item': None
        },
        'Cargo Hold': {
            'description': "The Cargo Hold is dark and eerie.",
            'directions': {
                'North': 'Storage Bay',
            },
            'Item': None
        }
    }

    # List of items to be randomized
    items = ['Nano Repair Kit', 'Power Cell', 'Energy Converter', 'Command Key Card', 'Laser Cannon Blueprint',
             'Shield Generator']

    # Randomize player start, alien start, and item placement
    player_start_room, alien_start_room, placed_items = randomize_game(spacecraft_rooms, items)

    print("alien room:", alien_start_room) #TODO: remove this

    return player_start_room, spacecraft_rooms, alien_start_room, placed_items