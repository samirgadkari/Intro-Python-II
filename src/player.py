# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, room):
        self.current_room = room

    def move(self, direction):

        room_dir = {
            'n': self.current_room.n_to,
            's': self.current_room.s_to,
            'e': self.current_room.e_to,
            'w': self.current_room.w_to
        }
        explicit_dir = {
            'n': 'north',
            's': 'south',
            'e': 'east',
            'w': 'west'
        }[direction]

        next_room = room_dir[direction]
        if next_room is None:
            print(f'\n  ERROR: No room to the {explicit_dir}' +
                  f' of "{self.current_room.name}"\n')
        else:
            self.current_room = next_room
