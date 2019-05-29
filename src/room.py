# Implement a class to hold room information. This should have name and
# description attributes.
import textwrap

WIDTH = 80


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return textwrap.fill(textwrap.dedent(self.name + ':' + self.description + '.') \
                             .strip(), width=WIDTH)
