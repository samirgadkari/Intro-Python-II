from item import Item


class LightSource(Item):
    def __init__(self, name, description, location, count):
        super().__init__(name, description, location, count)

    def on_drop(self):
        print('  It\'s not wise to drop your source of light')
        super().on_drop()
