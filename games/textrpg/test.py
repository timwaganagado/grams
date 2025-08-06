from rpg import Player, Test_enemy, Armour, Body, Unarmed
import random

P = Player()
E = Test_enemy("Goblin", 10)

acc = P.get_accuracy()
print(f"Player Accuracy: {acc}")
for x in Body:
    print(100+acc, E.get_hit_chance(x), (100+acc), (0+acc), end=" |")
    print(f"{((100+acc)-E.get_hit_chance(x))/((100+acc)-(0+acc))}%")