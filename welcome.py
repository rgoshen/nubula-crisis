def display_game_logo():
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
              \t'exit (quits the game)'
          ''')
    input('Press any key to continue...')