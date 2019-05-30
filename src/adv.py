from room import Room
from player import Player
from items import Items


class Adventure:
    def __init__(self, name):
        self.name = name
        self.player = None

        # Declare all the rooms

        room = {
            'outside':
            Room("Outside Cave Entrance",
                 "North of you, the cave mount beckons"),
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
                "Treasure Chamber",
                """You've found the long-lost treasure
                chamber! Sadly, it has already been completely emptied by
                earlier adventurers. The only exit is to the south.""",
                is_light=True),
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

        # Make a new player object that is currently in the 'outside' room.

        outside_room = room['outside']
        self.items = Items(outside_room)
        self.player = Player(outside_room)

    def update_items(self, player, action, items, item_name):

        if (action == 'get') or (action == 'take'):
            item = items.update_loc(player.current_room, player, item_name)
            if item is not None:
                item.on_take()
        elif action == 'drop':
            item = items.update_loc(player, player.current_room, item_name)
            if item is not None:
                item.on_drop()

    def loop(self):
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

        def room_is_lit():
            nonlocal self
            return self.player.current_room.is_light or \
                self.items.item_in_loc_has_light(self.player.current_room) or \
                self.items.item_in_loc_has_light(self.player)

        VALID_MOVES = ['n', 's', 'e', 'w']
        MOVE_PROMPT = f'Type in {",".join(VALID_MOVES)} to move'
        QUIT_PROMPT = ' or \'q\' to quit'
        VALID_ACTIONS = ['get', 'take', 'drop']
        DONE_MSG = 'Thank you for playing !!'

        while True:
            print('\nCurrent room>', self.player.current_room)
            if room_is_lit():
                print('  Items in room: ', [
                    (str(item.name) + ' (' + str(item.count) + ')')
                    for item in self.items.get_items(self.player.current_room)
                ])
            else:
                print('It\'s pitch black!')

            cmd = input(MOVE_PROMPT + QUIT_PROMPT + ': ')
            if ' ' in cmd:
                cmd_parts = cmd.split()

            if cmd == 'q':
                print(DONE_MSG)
                break
            elif (cmd == 'i') or (cmd == 'inventory'):
                print(
                    '  Items with player: ',
                    [str(item) for item in self.items.get_items(self.player)])
                print()
            elif cmd in VALID_MOVES:
                self.player.move(cmd)
            elif cmd_parts[0] in VALID_ACTIONS:
                self.update_items(self.player, cmd_parts[0], self.items,
                                  cmd_parts[1])
            else:
                print('  Error: Cannot understand command:', cmd)


if __name__ == '__main__':
    adv = Adventure('Treasure hunt')
    adv.loop()
