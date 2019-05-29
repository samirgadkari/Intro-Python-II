from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':
    Room("Outside Cave Entrance", "North of you, the cave mount beckons"),
    'foyer':
    Room(
        "Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),
    'overlook':
    Room(
        "Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),
    'narrow':
    Room(
        "Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),
    'treasure':
    Room(
        "Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

VALID_MOVES = ['n', 's', 'e', 'w']
MOVE_PROMPT = f'Type in {",".join(VALID_MOVES)} to move'
QUIT_PROMPT = ' or \'q\' to quit'
VALID_ACTIONS = ['get', 'take', 'drop']
DONE_MSG = 'Thank you for playing !!'

room = room['outside']
items = [
    Item('torch', 'midieval torch used to light your way'),
    Item('gold', 'barter for anything your heart desires'),
    Item('medicine', 'don\'t leave home without it'),
    Item('food', 'good for long journeys')
]
for item in items:
    room.add_item(item)

player = Player(room)


def move(player, direction):
    room = player.current_room
    room_dir = {'n': room.n_to, 's': room.s_to, 'e': room.e_to, 'w': room.w_to}
    explicit_dir = {
        'n': 'north',
        's': 'south',
        'e': 'east',
        'w': 'west'
    }[direction]

    next_room = room_dir[direction]
    if next_room is None:
        print(f'\n  ERROR: No room to the {explicit_dir} of "{room.name}"\n')
    else:
        player.current_room = next_room


def update_items(player, action, item_name):
    def move_item(from_loc, to_loc, item_name):

        nonlocal player
        item = None

        for from_item in from_loc.get_items():
            if from_item.name == item_name:
                item = from_item
                break
        if item is None:
            print('  Error: No such item')
            return

        from_loc.remove_item(item)
        to_loc.add_item(item)

        if player is from_loc:
            item.on_drop()
        elif player is to_loc:
            item.on_take()

        return

    if (action == 'get') or (action == 'take'):
        move_item(player.current_room, player, item_name)
    elif action == 'drop':
        move_item(player, player.current_room, item_name)


# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

while True:
    print('\nCurrent room>', player.current_room)
    print('  Items in room: ',
          [str(item) for item in player.current_room.get_items()])

    cmd = input(MOVE_PROMPT + QUIT_PROMPT + ': ')
    if ' ' in cmd:
        cmd_parts = cmd.split()

    if cmd == 'q':
        print(DONE_MSG)
        break
    elif (cmd == 'i') or (cmd == 'inventory'):
        print('  Items with player: ',
              [str(item) for item in player.get_items()])
        print()
    elif cmd in VALID_MOVES:
        move(player, cmd)
    elif cmd_parts[0] in VALID_ACTIONS:
        update_items(player, cmd_parts[0], cmd_parts[1])
    else:
        print('  Error: Cannot understand command:', cmd)
