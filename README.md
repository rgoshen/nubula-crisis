# Nebula Crisis: Overlord Showdown

## Overview

**Nebula Crisis: Overlord Showdown** is a text-based adventure game set aboard an intergalactic spaceship overrun by a
deadly Alien Overlord. As the player, your mission is to explore the ship, gather critical items, and activate the
ship's defense system before the Alien Overlord catches you. Each playthrough is unique due to randomized starting
positions, item locations, and the alien's whereabouts, ensuring unpredictability and replayability.

## Gameplay

- You begin the game in a random room on the spaceship.
- Your mission is to explore the spaceship, collect six essential items, and activate the ship's defense system before
  encountering the Alien Overlord.
- The six essential items are:
    - **Power Cell**
    - **Shield Generator**
    - **Command Keycard**
    - **Energy Converter**
    - **Nano Repair Kit**
    - **Laser Cannon Blueprint**

- The location of these items, as well as the Alien Overlord, will be different in every playthrough.
- If you enter the room where the Alien Overlord is hiding before collecting all the necessary items, you will be
  defeated, and the game will end.

## Features

- **Randomized Start and Item Locations**: Both your starting point and the location of the essential items and the
  Alien Overlord are randomized with each new game, ensuring replayability and unpredictability.
- **Text-based Interface**: Navigate between rooms and collect items via simple text commands.
- **Item Collection**: Explore different rooms on the spaceship to collect the essential items.
- **Replayability**: Each playthrough is different, adding a layer of challenge and excitement as you explore the ship.

## Installation

1. Clone this repository to your local machine using:
   ```bash
   git clone https://github.com/yourusername/nebula-crisis.git
   ```

2. Navigate to the project directory:
    ```bash
    cd nebula_crisis
    ```

3. Run the game:
    ```bash
    python main.py
    ```

## How to Play

1. Move between rooms: Use simple commands like go north, go south, go east, and go west to navigate through the ship.
2. Collect items: When you enter a room containing one of the essential items, use the take item command to collect
   it.
3. Check inventory: Type inventory at any time to see which items you’ve collected.
4. Avoid the Alien Overlord: If you enter the Alien Overlord’s location before collecting all six items, you will be
   defeated, and the game will end.
5. Win condition: Once all six items have been collected, the ship’s defense system will activate, and you’ll
   successfully defeat the Alien Overlord.

## Game Commands

- Movement:
    - go [direction] – Moves the player to a new room. (e.g., go north)
- Item Management:
    - take item – Collects the item in the current room.
    - inventory – Shows a list of all collected items.
- Quit:
    - quit – Ends the game.

## Rooms in the Game

- Crew Quarters
- Control Room
- Storage Bay
- Observation
- Engine Room
- Medical Bay
- Weaponry Room
- Cargo Hold

These rooms will be explored as you attempt to find the six critical items while avoiding the Alien Overlord.

## Future Enhancements

- Adding more rooms and challenges.
- Implementing a combat system for direct confrontation with the Alien Overlord.
- Adding different types of aliens for increased difficulty.

## License

This project is licensed under the MIT License. See the [LICENSE](./LICENSE.md) file for details.

## Contact

For questions, suggestions, or bug reports, please contact:

Rick Goshen
Email: rick.goshen@gmail.com
GitHub: https://github.com/rickgoshen
