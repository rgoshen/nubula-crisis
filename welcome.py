def display_game_logo():
    """
    Displays the ASCII art logo for the game and an alien figure.

    The function prints out the game's title, "Nebula Crisis: Overlord Showdown,"
    in stylized ASCII art using text generated from an ASCII text generator.
    Additionally, it displays an alien figure in ASCII art to set the theme for the game.

    After displaying the logo and the alien figure, the function calls the
    welcome_prompt() function to show the game's welcome message and instructions.
    """
    print()
    # Ascii Text Generator https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
    print(r'''
     _   _        _             _          _____        _       _                                              
    | \ | |      | |           | |        /  __ \      (_)     (_)      _                                      
    |  \| |  ___ | |__   _   _ | |  __ _  | /  \/ _ __  _  ___  _  ___ (_)                                     
    | . ` | / _ \| '_ \ | | | || | / _` | | |    | '__|| |/ __|| |/ __|                                        
    | |\  ||  __/| |_) || |_| || || (_| | | \__/\| |   | |\__ \| |\__ \ _                                      
    \_| \_/ \___||_.__/  \__,_||_| \__,_|  \____/|_|   |_||___/|_||___/(_)                                     


     _____                    _                  _   _____  _                         _                        
    |  _  |                  | |                | | /  ___|| |                       | |                       
    | | | |__   __ ___  _ __ | |  ___   _ __  __| | \ `--. | |__    ___ __      __ __| |  ___ __      __ _ __  
    | | | |\ \ / // _ \| '__|| | / _ \ | '__|/ _` |  `--. \| '_ \  / _ \\ \ /\ / // _` | / _ \\ \ /\ / /| '_ \ 
    \ \_/ / \ V /|  __/| |   | || (_) || |  | (_| | /\__/ /| | | || (_) |\ V  V /| (_| || (_) |\ V  V / | | | |
     \___/   \_/  \___||_|   |_| \___/ |_|   \__,_| \____/ |_| |_| \___/  \_/\_/  \__,_| \___/  \_/\_/  |_| |_|
    ''')
    print()
    # Artist: Krogg https://www.asciiart.eu/space/aliens
    print(r'''
           \.   \.      __,-"-.__      ./   ./
       \.   \`.  \`.-'"" _,="=._ ""`-.'/  .'/   ./
        \`.  \_`-''      _,="=._      ``-'_/  .'/
         \ `-',-._   _.  _,="=._  ,_   _.-,`-' /
      \. /`,-',-._"""  \ _,="=._ /  """_.-,`-,'\ ./
       \`-'  /    `-._  "       "  _.-'    \  `-'/
       /)   (         \    ,-.    /         )   (\
    ,-'"     `-.       \  /   \  /       .-'     "`-,
  ,'_._         `-.____/ /  _  \ \____.-'         _._`,
 /,'   `.                \_/ \_/                .'   `,\
/'       )                  _                  (       `\
        /   _,-'"`-.  ,++|T|||T|++.  .-'"`-,_   \
       / ,-'        \/|`|`|`|'|'|'|\/        `-, \
      /,'             | | | | | | |             `,\
     /'               ` | | | | | '               `\
                        ` | | | '
                          ` | '
    ''')
    welcome_prompt()

def welcome_prompt():
    """
    Displays the welcome message and game instructions to the player.

    This function prints out a brief introduction to the game "Nebula Crisis: Overlord Showdown,"
    explaining the player's mission and the basic game mechanics. It outlines how the player can
    move between rooms, collect items, view their inventory, and exit the game.

    After displaying the instructions, it waits for the player to press any key to continue the game.
    """
    print()
    print('''\t\tWelcome to Nebula Crisis: Overlord Showdown!
    
        Your mission is to navigate through the spaceship and
        collect six critical items needed to activate the ship’s
        defense system. These items are scattered across various rooms,
        but beware—the deadly Alien Overlord is somewhere aboard the ship,
        and if you encounter it before gathering all the items, 
        it will be game over!
                            -------------------------
        Moves:\t'go {direction}' (travel north, south, east, or west)
              \t'get {item}' (add nearby item to inventory)
              \t'inventory' (shows a list of all your items)
              \t'exit (quits the game)'
          ''')
    input('Press any key to continue...')