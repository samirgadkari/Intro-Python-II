from item import Item
from lightsource import LightSource


class Items:
    def __init__(self, room):

        self.items = [
            Item('gold', 'barter for anything your heart desires', room, 1),
            Item('medicine', 'don\'t leave home without it', room, 1),
            Item('food', 'good for long journeys', room, 2),
            LightSource('lamp', 'oil lamp', room, 2)
        ]

    def find(self, name, location):
        for idx, item in enumerate(self.items):
            if (item.name == name) and (item.location == location):
                return idx, item
        return None, None

    def get_items(self, location):
        items_in_location = []
        for item in self.items:
            if item.location == location:
                items_in_location.append(item)
        return items_in_location

    def item_in_loc_has_light(self, location):
        for item in self.get_items(location):
            if isinstance(item, LightSource):
                return True
        return False

    def update_loc(self, from_loc, to_loc, name):

        item_from_idx, item_from = self.find(name, from_loc)
        if item_from is None:
            print('  Error: No such item')
            return

        _, item_to = self.find(name, to_loc)
        if item_to is None:
            if item_from.count == 1:
                item_from.location = to_loc
            else:
                item_from.count -= 1
                if isinstance(item_from, LightSource):
                    item = LightSource(item_from.name, item_from.description,
                                       to_loc, 1)
                    self.items.append(item)
                elif isinstance(item_from, Item):
                    item = Item(item_from.name, item_from.description, to_loc,
                                1)
                    self.items.append(item)
        else:
            item_to.count += 1

            item_from.count -= 1
            if item_from.count == 0:
                self.items.pop(item_from_idx)
