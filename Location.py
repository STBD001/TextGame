class Item:
    def __init__(self, name, description, effect_type, effect_value):
        self.name = name
        self.description = description
        self.effect_type = effect_type
        self.effect_value = effect_value

    def __str__(self):
        return f"{self.name}: {self.description} ({self.effect_type} +{self.effect_value})"


class Location:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.connections = {}
        self.items = []

    def connect(self, direction, location):
        self.connections[direction] = location

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item_name):
        self.items = [item for item in self.items if item.name != item_name]

    def get_description(self):
        item_descriptions = "\n".join(str(item) for item in self.items)
        return f"{self.name}\n{self.description}\nPrzedmioty dostępne tutaj:\n{item_descriptions}"

    def move(self, direction):
        if direction in self.connections:
            return self.connections[direction]
        else:
            print("Nie można tam iść!")
            return self


# Tworzenie instancji lokacji
forest = Location("Las", "Znajdujesz się w gęstym lesie. Wokół słychać śpiew ptaków.")
cave = Location("Jaskinia", "Wchodzisz do mrocznej jaskini. Jest tu zimno i wilgotno.")
lake = Location("Jezioro", "Stoisz nad brzegiem spokojnego jeziora.")

# Połączenia między lokacjami
forest.connect("north", cave)
forest.connect("east", lake)
cave.connect("south", forest)
lake.connect("west", forest)
