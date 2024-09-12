from Location import Location

class Enemy:
    def __init__(self, name, health, loot=None):
        self.name = name
        self.health = health
        self.loot = loot

    def is_alive(self):
        return self.health > 0

    def attack(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0


class LocationWithEnemy(Location):
    def __init__(self, name, description, enemy=None):
        super().__init__(name, description)
        self.enemy = enemy

    def get_description(self):
        description = super().get_description()
        if self.enemy and self.enemy.is_alive():
            description += f"\nNa Twojej drodze stoi {self.enemy.name}!"
        return description


class NPC:
    def __init__(self, name, dialogue):
        self.name = name
        self.dialogue = dialogue

    def talk(self):
        print(f"{self.name}: {self.dialogue}")
