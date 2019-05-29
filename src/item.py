class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}'

    def on_drop(self):
        print('  You have dropped item:', self.name)

    def on_take(self):
        print('  You have picked up item:', self.name)
