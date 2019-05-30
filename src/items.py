from item import Item


class Items:
    def __init__(self, room):

        self.items = [
            Item('torch', 'midieval torch used to light your way', room, 1),
            Item('gold', 'barter for anything your heart desires', room, 1),
            Item('medicine', 'don\'t leave home without it', room, 1),
            Item('food', 'good for long journeys', room, 2)
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

    def update_loc(self, from_loc, to_loc, name):

        item_from_idx, item_from = self.find(name, from_loc)
        if item_from is None:
            print('  Error: No such item')
            return

        print('item_from.count:', item_from.count)

        _, item_to = self.find(name, to_loc)
        if item_to is None:
            item = Item(name, item_from.description, to_loc, 1)
            print('updated: item.count:', item.count)
            self.items.append(item)
        else:
            print('item_to.count:', item_to.count)
            item_to.count += 1
            print('updated: item_from.count:', item_from.count,
                  'item_to.count:', item_to.count)

        item_from.count -= 1
        if item_from.count == 0:
            self.items.pop(item_from_idx)
