import random
from enum import Enum
import time

Armour = Enum('Armour',[("Helmet",1),("Gloves",2),("Chest",3),("Shoes",4)])
Body = Enum('Body',[("Head",1),("Arms",2),("Torso",3),("Legs",4)])

hitChance_default = {Body.Head: 70, Body.Arms: 20, Body.Torso: 20, Body.Legs: 40}

class test_chest:
    def __init__(self):
        self.name = "Test Chest"
        self.description = "A chest chest for chesting purposes."
        self.armour_type = Armour.Chest
        self.armour_value = 1
        self.health = 10
        self.health_max = 10
        self.speed = 0
        self.accuracy = 0
        self.effects = []


class Weapon_base:
    def __init__(self):
        self.attack_damage = 0
        self.effects = []
        self.speed = 0
        self.accuracy = 0
    def get_damage(self):
        return self.attack_damage
    def get_effects(self):
        return self.effects

class Unarmed(Weapon_base):
    def __init__(self):
        super().__init__()
        self.attack_damage = 3
    

class character_base:
    def __init__(self, name="none", health=10):
        self.name = name
        self.health = health
        self.health_max = health

        self.speed = 10
        self.dodge = 0
        self.speed_current = 0
        self.weapon = Unarmed()
        self.selected_weapon = self.weapon
        self.update_speed()

        self.accuracy = 10

        self.armour = {Armour.Helmet:0, Armour.Gloves:0, Armour.Chest:0, Armour.Shoes:0}
        self.hit_chance = hitChance_default.copy()

        self.body_max_health = {Body.Head: health, Body.Arms: health, Body.Torso: health, Body.Legs: health}
        self.body_max_current_health = {Body.Head: health, Body.Arms: health, Body.Torso: health, Body.Legs: health}   
        self.body_health = {Body.Head: health, Body.Arms: health, Body.Torso: health, Body.Legs: health}

    def damage(self, attack_received, attacker, targeting):
        hit = attacker.get_attack_accuracy()
        print(self.get_hit_chance(targeting) < hit)
        if self.get_hit_chance(targeting) < hit:
            critical_body_damage = self.body_health[targeting] / self.body_max_current_health[targeting]
            if critical_body_damage < 0.5:
                chance_fatal = critical_body_damage/0.5*100
                outome_fatal = random.randint(1, 100)
            damage = attack_received.get_damage()
            self.body_part_damage(targeting, damage, attack_received)
            self.update_health(damage, attack_received)
            return damage, chance_fatal if critical_body_damage < 0.5 else 1, outome_fatal if critical_body_damage < 0.5 else 0
        return "miss", 100, 0  # No damage, always fatal chance is 100% and outcome is 0 (no fatal outcome)
    
    def body_part_damage(self, body_part, damage, attack_received):
        body_damage = int(damage)
        match body_part:
            case Body.Head if self.armour[Armour.Helmet] != 0:
                armour_targeted = self.armour[Armour.Helmet]
                body_damage -= armour_targeted.armour_value
            case Body.Arms if self.armour[Armour.Gloves] != 0:
                armour_targeted = self.armour[Armour.Gloves]
                body_damage -= armour_targeted.armour_value
            case Body.Torso if self.armour[Armour.Chest] != 0:
                print("Torso hit")
                armour_targeted = self.armour[Armour.Chest]
                body_damage -= armour_targeted.armour_value
            case Body.Legs if self.armour[Armour.Shoes] != 0:
                armour_targeted = self.armour[Armour.Shoes]
                body_damage -= armour_targeted.armour_value

        self.body_health[body_part] -= body_damage
        if self.body_health[body_part] < 0:
            self.body_health[body_part] = 0
        
    def attack(self, target, aim):
        return target.damage(self.weapon,self, aim)    

    def get_hit_chance(self, targeting):
        if targeting in self.hit_chance:
            return self.hit_chance[targeting] + self.dodge
        else:
            return 0
    def get_health(self):
        return self.health
    
    def get_attack_accuracy(self):
        acc = self.get_accuracy()
        return random.randint(acc, 100+ acc)
    
    def get_accuracy(self):
        return self.accuracy + self.selected_weapon.accuracy

    def update_speed(self):
        self.speed = self.speed + self.weapon.speed

    def update_health(self, damage, attack_received):
        self.health -= damage

class Player(character_base):
    def __init__(self):
        super().__init__()
        self.armour = {Armour.Helmet:0,Armour.Gloves:0,Armour.Chest:0,Armour.Shoes:0}
        self.weapon = Unarmed()
        self.selected_weapon = self.weapon
        self.health_max = 0
        self.health = 0
        self.update_health(0)
        self.speed = 10
        self.accuracy = 10
        self.update_speed()
    def update_health(self,damage, attack_received=None):
        self.health = 0
        for part in self.body_health:
            self.health += self.body_health[part]


class Test_enemy(character_base):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.armour[Armour.Chest] = test_chest()
        self.dodge = 10
    
if __name__ == "__main__":
    buffer = 18

    running = True
    while running:
        player = Player()
        adventure = True
        while adventure:
            Enemy = Test_enemy("Goblin", 10)
            battle = True
            while battle:

                

                player.speed_current += player.speed
                Enemy.speed_current += Enemy.speed
                if player.speed_current > 100:
                    player.speed_current = 0

                    print(f"Enemy {Enemy.name} has {Enemy.health} health.")
                    string_head_hp = "head: " + str(Enemy.body_health[Body.Head])
                    string_arms_hp = "arms: " + str(Enemy.body_health[Body.Arms])
                    string_torso_hp = "torso: " + str(Enemy.body_health[Body.Torso])
                    string_legs_hp = "legs: " + str(Enemy.body_health[Body.Legs])

                    string_head = "head: " + str(Enemy.armour[Armour.Helmet].name if Enemy.armour[Armour.Helmet] else 0)
                    string_arms = "arms: " + str(Enemy.armour[Armour.Gloves].name if Enemy.armour[Armour.Gloves] else 0)
                    string_torso = "torso: " + str(Enemy.armour[Armour.Chest].name if Enemy.armour[Armour.Chest] else 0)
                    string_legs = "legs: " + str(Enemy.armour[Armour.Shoes].name if Enemy.armour[Armour.Shoes] else 0)
                    

                    print(f"{string_head_hp:<{buffer}} | {string_arms_hp:<{buffer}} | {string_torso_hp:<{buffer}} | {string_legs_hp:<{buffer}}")
                    print(f"{string_head:<{buffer}} | {string_arms:<{buffer}} | {string_torso:<{buffer}} | {string_legs:<{buffer}}")
                    print()
                    print(f"You have {player.health} health.")
                    print(f"head: {player.body_health[Body.Head]} | arms: {player.body_health[Body.Arms]} | torso: {player.body_health[Body.Torso]} | legs: {player.body_health[Body.Legs]}")
                    print()
                    print("Aim at")
                    print("(h)ead, (a)rms, (t)orso, (l)egs")
                    acc = player.get_accuracy()
                    print(f"Accuracy: {acc}")
                    for x in Body:
                        print(f"{((100+acc)-Enemy.get_hit_chance(x))/((100+acc)-(0+acc))}%", end=" |")
                    print()
                    turn = input("Your turn: ").lower()
                    if turn == 'a':
                        aim = Body.Arms
                    elif turn == 't':
                        aim = Body.Torso
                    elif turn == 'l':
                        aim = Body.Legs
                    else:
                        aim = Body.Head
                    damage = player.attack(Enemy,aim)[0]
                    print(f"You attacked {Enemy.name} for {damage} damage." if damage else "You missed!")
                    if Enemy.health <= 0:
                        print(f"You defeated {Enemy.name}!")
                        battle = False
                        continue
                
                if Enemy.speed_current > 100:
                    Enemy.speed_current = 0
                    print(f"{Enemy.name} is attacking!")
                    aim = random.choice(list(Body))
                    damage, fatal_chance, fatal_outcome = Enemy.attack(player,aim)
                    time.sleep(1)
                    if damage:
                        print(f"{Enemy.name} attacked your {aim.name} for {damage} damage.")
                        print(f"TEST: {fatal_chance} | {fatal_outcome}")
                        if fatal_outcome:
                            time.sleep(1)
                            print(f"You are taking a fatal blow to your {aim.name}!")
                            time.sleep(1)
                            if fatal_chance < 100 and fatal_outcome >= fatal_chance:
                                print(f"{Enemy.name} has dealt a fatal blow to your {aim.name}!")
                                battle = False
                                adventure = False
                            else:
                                print(f"You SURVIVED the fatal blow to your {aim.name}!")
                    else:
                        print(f"{Enemy.name} missed!")