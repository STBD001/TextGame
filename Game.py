from Enemy import LocationWithEnemy
class Game:
    def __init__(self):
        self.current_location = None
        self.player_health = 100
        self.attack_power = 10

    def set_start_location(self, location):
        self.current_location = location

    def play(self):
        while True:
            print("\n" + self.current_location.get_description())

            if isinstance(self.current_location, LocationWithEnemy) and self.current_location.enemy.is_alive():
                self.fight(self.current_location.enemy)

            command = input("Co chcesz zrobić? ").strip().lower()
            if command in ["exit", "quit", "wyjscie", "wyjsc"]:
                print("Dziękujemy za grę!")
                break
            elif command in ["north", "south", "east", "west"]:
                self.current_location = self.current_location.move(command)
            else:
                print("Nie rozumiem polecenia")

    def fight(self, enemy):
        print(f"\nRozpoczyna się walka z {enemy.name}!")
        while enemy.is_alive() and self.player_health > 0:
            action = input("Co chcesz zrobić? (atak, ucieczka) ").strip().lower()
            if action == "atak":
                damage = self.attack_power
                enemy.attack(damage)
                print(f"Zadałeś {damage} obrażeń {enemy.name}.")

                if not enemy.is_alive():
                    print(f"Pokonałeś {enemy.name}!")

                    if enemy.loot:
                        print(f"Z przeciwnika {enemy.name} wypadł {enemy.loot.name}!")
                        if enemy.loot.effect_type == "damage":
                            self.attack_power += enemy.loot.effect_value
                            print(f"Twoja siła ataku wzrosła o {enemy.loot.effect_value}!")
                        elif enemy.loot.effect_type == "health":
                            self.player_health += enemy.loot.effect_value
                            print(f"Twoje zdrowie wzrosło o {enemy.loot.effect_value}!")

                else:
                    enemy_damage = enemy.health * 0.5
                    self.player_health -= enemy_damage
                    print(f"{enemy.name} zadaje Ci {enemy_damage} obrażeń!")
                    print(f"Twoje zdrowie: {self.player_health} punktów")

                    if self.player_health <= 0:
                        print("Zostałeś pokonany! Gra skończona.")
                        break
            elif action == "ucieczka":
                print("Uciekasz z walki!")
                break
            else:
                print("Nie rozumiem tej akcji.")

        if self.player_health <= 0:
            print("Zostałeś pokonany! Gra skończona.")
            return

        if not enemy.is_alive():
            print(f"Pokonałeś {enemy.name} i kontynuujesz podróż.")
