import random
from enum import Enum
import time

Armour = Enum('Armour',[("Helmet",1),("Gloves",2),("Chest",3),("Shoes",4)])
Body = Enum('Body',[("Head",1),("Arms",2),("Torso",3),("Legs",4)])

hitChance_default = {Body.Head: 70, Body.Arms: 20, Body.Torso: 20, Body.Legs: 40}

class Unarmed:
    def __init__(self):
        self.attack_damage = 3
        self.effects = []
        self.speed = 0
        self.accuracy = 10
    def get_damage(self):
        return self.attack_damage


class character_base:
    def __init__(self, name="none", health=10):
        self.name = name
        self.health = health
        self.health_max = health

        self.speed = 10
        self.weapon = Unarmed()
        self.update_speed()

        self.accuracy = 10

        self.armour = {Armour.Helmet:0, Armour.Gloves:0, Armour.Chest:0, Armour.Shoes:0}
        self.hit_chance = hitChance_default.copy()

        self.body_max_health = {Body.Head: health, Body.Arms: health, Body.Torso: health, Body.Legs: health}
        self.body_max_current_health = {Body.Head: health, Body.Arms: health, Body.Torso: health, Body.Legs: health}   
        self.body_health = {Body.Head: health, Body.Arms: health, Body.Torso: health, Body.Legs: health}

    def damage(self, attack_received, attacker, targeting):
        hit = random.randint(attack_received.accuracy + attacker.accuracy, 100)
        if self.get_hit_chance(targeting) < hit:
            damage = attack_received.get_damage()
            critical_body_damage = self.body_health[targeting] / self.body_max_current_health[targeting]
            if critical_body_damage < 0.5:
                chance_fatal = critical_body_damage/0.5*100
                outome_fatal = random.randint(1, 100)

            self.body_health[targeting] -= damage
            self.update_health(damage)
            return damage, chance_fatal if critical_body_damage < 0.5 else 1, outome_fatal if critical_body_damage < 0.5 else 0
        return 0, 100, 0  # No damage, always fatal chance is 100% and outcome is 0 (no fatal outcome)
    
    def attack(self, target, aim):
        return target.damage(self.weapon,self, aim)    

    def get_hit_chance(self, targeting):
        if targeting in self.hit_chance:
            return self.hit_chance[targeting]
        else:
            return 0
    def get_health(self):
        return self.health
    
    def update_speed(self):
        self.speed = self.speed + self.weapon.speed

    def update_health(self, damage):
        self.health -= damage

class Player(character_base):
    def __init__(self):
        super().__init__()
        self.armour = {Armour.Helmet:0,Armour.Gloves:0,Armour.Chest:0,Armour.Shoes:0}
        self.weapon = Unarmed()
        self.health_max = 0
        self.health = 0
        self.update_health(0)
        self.speed = 10
        self.accuracy = 10
        self.update_speed()
    def update_health(self,damage):
        self.health = 0
        for part in self.body_health:
            self.health += self.body_health[part]


class Test_enemy(character_base):
    def __init__(self, name, health):
        super().__init__(name, health)
    


running = True
while running:
    player = Player()
    adventure = True
    while adventure:
        Enemy = Test_enemy("Goblin", 10)
        battle = True
        while battle:
            print(f"Enemy {Enemy.name} has {Enemy.health} health.")
            print(f"head: {Enemy.body_health[Body.Head]} | arms: {Enemy.body_health[Body.Arms]} | torso: {Enemy.body_health[Body.Torso]} | legs: {Enemy.body_health[Body.Legs]}")
            print()
            print(f"You have {player.health} health.")
            print(f"head: {player.body_health[Body.Head]} | arms: {player.body_health[Body.Arms]} | torso: {player.body_health[Body.Torso]} | legs: {player.body_health[Body.Legs]}")
            print()
            print("Aim at")
            print("(h)ead, (a)rms, (t)orso, (l)egs")
            print(f"{100-Enemy.get_hit_chance(Body.Head)}% | {100-Enemy.get_hit_chance(Body.Arms)}% | {100-Enemy.get_hit_chance(Body.Torso)}% | {100-Enemy.get_hit_chance(Body.Legs)}%")
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
            aim = random.choice(list(Body))
            damage, fatal_chance, fatal_outcome = Enemy.attack(player,aim)
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