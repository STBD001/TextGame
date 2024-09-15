from Game import Game
from Location import forest, lake, Item
from Enemy import Enemy, LocationWithEnemy

def main():
    # Tworzenie przedmiotów
    sword = Item("Miecz", "Miecz, który zwiększa twoją siłę ataku.", "damage", 5)
    potion = Item("Mikstura", "Mikstura, która zwiększa twoje zdrowie.", "health", 20)

    # Tworzenie przeciwników z lootem
    forest_enemy = Enemy("Wilk", 20, loot=sword)
    cave_enemy = Enemy("Niedźwiedź", 35, loot=potion)
    lake_enemy = Enemy("Rekin", 30)

    # Ustawianie przeciwników do ich lokalizacji
    forest_with_forest_enemy = LocationWithEnemy("Las", "Znajdujesz się w gęstym lesie. Jest tu cicho i niepokojąco...", forest_enemy)
    cave_with_cave_enemy = LocationWithEnemy("Jaskinia", "Wchodzisz do mrocznej jaskini. Jest tu zimno i wilgotno.", cave_enemy)
    lake_with_lake_enemy = LocationWithEnemy("Jezioro", "Stoisz nad brzegiem spokojnego jeziora. Coś jednak przyciąga twoją uwagę...", lake_enemy)

    # Lokalizacje i połączenia
    forest.connect("north", cave_with_cave_enemy)
    forest.connect("west", forest_with_forest_enemy)
    forest.connect("east", lake_with_lake_enemy)

    game = Game()
    game.set_start_location(forest)
    game.play()

if __name__ == "__main__":
    main()
