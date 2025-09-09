import random
from enum import Enum
import time
import Effects 

Armour = Enum('Armour',[("Helmet",1),("Gloves",2),("Chest",3),("Shoes",4)])
Body = Enum('Body',[("Head",1),("Arms",2),("Torso",3),("Legs",4)])
DamageType = Enum('DamageType',[("Physical",1),("Fire",2),("Ice",3),("Poison",4),("Slash",5),("Pierce",6),("Blunt",7),("Cleave",8)])



hitChance_default = {Body.Head: 70, Body.Arms: 20, Body.Torso: 20, Body.Legs: 40}



class Armour_base:
    def __init__(self):
        self.name = "Base Armour"
        self.description = "A base armour for testing purposes."
        self.armour_type = Armour.Chest
        self.armour_value = 0
        self.health = 0
        self.health_max = 0
        self.speed = 0
        self.accuracy = 0
        self.effects = []

class test_chest(Armour_base):
    def __init__(self):
        super().__init__()
        self.name = "Test Chest"
        self.description = "A chest chest for chesting purposes."
        self.armour_type = Armour.Chest
        self.armour_value = 1
        self.health = 10
        self.health_max = 10


class Weapon_base:
    def __init__(self):
        self.name = "Base Weapon"
        self.description = "A base weapon for testing purposes."
        self.attack_damage = 0
        self.limb_damage = 0
        self.effects = []
        self.speed = 0
        self.accuracy = 0
    def get_damage(self):
        return self.attack_damage, self.effects
    def get_effects(self):
        return self.effects

class Unarmed(Weapon_base):
    def __init__(self):
        super().__init__()
        self.name = "Unarmed"
        self.description = "A base weapon for testing purposes."
        self.attack_damage = 3
        self.limb_damage = 1
        self.effects = [DamageType.Physical, DamageType.Blunt]


class broken_sword(Weapon_base):
    def __init__(self):
        super().__init__()
        self.name = "Broken Sword"
        self.description = "A broken sword"
        self.attack_damage = 2
        self.limb_damage = 2
        self.effects = [DamageType.Physical, DamageType.Slash]
        self.speed = 0
        self.accuracy = 0


class broken_axe(Weapon_base):
    def __init__(self):
        super().__init__()
        self.name = "Broken Axe"
        self.description = "A broken axe"
        self.attack_damage = 3
        self.limb_damage = 3
        self.effects = [DamageType.Physical, DamageType.Cleave]
        self.speed = -1
        self.accuracy = -5


class broken_spear(Weapon_base):
    def __init__(self):
        super().__init__()
        self.name = "Broken Spear"
        self.description = "A broken spear"
        self.attack_damage = 3
        self.limb_damage = 2
        self.effects = [DamageType.Physical, DamageType.Pierce]
        self.speed = -1
        self.accuracy = 5
    

loot_table = {
    1: {
        "weapons": [(broken_sword, 0.5), (broken_axe, 0.3), (broken_spear, 0.2)],
        "armour": [(test_chest, 1.0)]
    },
    2: {
        "weapons": [("iron_sword", 0.4), ("iron_axe", 0.4), ("iron_spear", 0.2)],
        "armour": [("iron_chest", 1.0)]
    },
    # Add more levels as needed
}

class character_base:
    def __init__(self, name="none", health=10, difficulty=1):
        self.name = name
        self.health = health
        self.health_max = health

        self.stat_speed = 10
        self.stat_dodge = 0
        self.selected_weapon = Unarmed()
        self.speed = 0
        self.speed_current = 0
        self.update_speed()

        self.accuracy = 10

        self.armour = {Armour.Helmet:0, Armour.Gloves:0, Armour.Chest:0, Armour.Shoes:0}
        self.hit_chance = hitChance_default.copy()

        self.body_max_health = {Body.Head: health, Body.Arms: health, Body.Torso: health, Body.Legs: health}
        self.body_max_current_health = {Body.Head: health, Body.Arms: health, Body.Torso: health, Body.Legs: health}   
        self.body_health = {Body.Head: health, Body.Arms: health, Body.Torso: health, Body.Legs: health}

        self.effects = []
        self.body_part_effects = {Body.Head: [], Body.Arms: [], Body.Torso: [], Body.Legs: []}
        self.weakness = []

        self.difficulty = difficulty
        self.loot = []
        self.loot_chance = 0.1 * difficulty

    def hit(self, attack_received, attacker, targeting):
        hit = attacker.get_attack_accuracy()
        print(f"Hit chance: {self.get_hit_chance(targeting)}% vs {hit}%")
        if self.get_hit_chance(targeting) < hit:
            self.apply_effects(attack_received,targeting)
            damage = self.damage(attack_received, targeting)
            chance_fatal, outcome_fatal = self.fatal(targeting)
            return damage, chance_fatal, outcome_fatal
        return "miss", 100, 0  # No damage, always fatal chance is 100% and outcome is 0 (no fatal outcome)
    
    def apply_effects(self, attack_received,targeting):
        for effect in attack_received.get_effects():
            if isinstance(effect, Effects.effect_base):
                if effect not in self.body_part_effects[targeting]:
                    self.body_part_effects[targeting].append(effect.apply_effect())
                else:
                    self.body_part_effects[targeting].duration += effect.apply_effect().duration
                #self.effects.append(effect)
                print(f"{self.name} is affected by {effect.name}.")

    def fatal(self, targeting):
        critical_body_damage = self.body_health[targeting] / self.body_max_current_health[targeting]
        if critical_body_damage < 0.5:
            return critical_body_damage/0.5*100,random.randint(1, 100)
        return 100, 0  # Always fatal chance is 100% and outcome is 0 (no fatal outcome)    

    def damage(self, attack_received, targeting):
        attack = attack_received.get_damage()
        damage = int(attack[0])
        effects = attack[1]
        for effect in effects:
            if effect in self.weakness:
                print(f"{self.name} is weak to {effect.name} damage!")
                damage += 1
        #limb_damage = attack_received.get_limb_damage()
        self.body_part_damage(targeting, damage, attack_received)
        self.update_health(damage)
        return damage
    
    def body_part_damage(self, body_part, damage, attack_received):
        body_damage = damage
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
        return target.hit(self.selected_weapon,self, aim)    

    def get_hit_chance(self, targeting):
        if targeting in self.hit_chance:
            return self.hit_chance[targeting] + self.stat_dodge
        else:
            return 0
    def get_health(self):
        return self.health
    
    def get_attack_accuracy(self):
        acc = self.get_accuracy()
        return random.randint(acc, 100+ acc)
    
    def get_accuracy(self):
        return self.accuracy + self.selected_weapon.accuracy
    
    def getloot(self):
        return self.loot

    def update_speed(self):
        self.speed = self.stat_speed + self.selected_weapon.speed

    def update_health(self, damage):
        self.health -= damage
    

class Player(character_base):
    def __init__(self,):
        super().__init__()
        self.name = "Player"
        self.armour = {Armour.Helmet:0,Armour.Gloves:0,Armour.Chest:0,Armour.Shoes:0}
        self.selected_weapon = Unarmed()
        self.health_max = 0
        self.health = 0
        self.update_health(0)
        self.speed = 10
        self.accuracy = 10
        self.inventory = []
        self.update_speed()
    def update_health(self,damage, attack_received=None):
        self.health = 0
        for part in self.body_health:
            self.health += self.body_health[part]
    def show_inventory(self):
        print("Inventory:")
        for i, item in enumerate(self.inventory):
            print(f"{i}. {item.name} - {item.description}")
        print("Select an item to equip or 'x' to exit:")
        choice = input()
        if choice.lower() == 'x':
            return
        try:
            choice = int(choice)
            if choice >= 0 and choice < len(self.inventory):
                item = self.inventory[choice]
                print(f"Equipping {item.name}...")
                print(f"Item type: {type(item)}")
                print(f"Item description: {item.description}")
                confirm = input("Are you sure? (y/n): ")
                if confirm.lower() != 'y':
                    print("Equip cancelled.")
                    return
                if isinstance(item, Weapon_base):
                    self.selected_weapon = item
                    self.update_speed()
                    print(f"You have equipped {item.name}.")
                elif isinstance(item, Armour_base):
                    self.armour[item.armour_type] = item
                    print(f"You have equipped {item.name}.")
                else:
                    print("You can't equip that item.")
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid choice.")


class Test_enemy(character_base):
    def __init__(self, name, health):
        super().__init__(name, health)
        self.armour[Armour.Chest] = test_chest()
        self.loot = [test_chest()]
        self.dodge = 10
        self.weakness = [DamageType.Blunt]

#system that handles room selection and creation
#picks a random room from a list or randomly generates a room
#then selects whats in the room
#saves the room



class Room:
    def __init__(self, name="Default Room", description="A room for testing purposes.",items=[], enemy=None,loottype=0):
        self.name = name
        self.description = description
        self.items = items
        self.enemy = enemy
        self.doors = []
        self.completed = False
        self.loottype = loottype

        if self.enemy:
            print(self.enemy.loot_chance)
            if random.choices([True,False],[self.enemy.loot_chance,1-self.enemy.loot_chance])[0]:
                print('loot')
                loot = enemy.getloot()
                self.items.extend(loot)
    def content(self,player):
        #choose from three weapons
        print(f"You are in {self.name}. {self.description}")
        if self.loottype == 0:
            print("There is nothing in this room.")
        if self.loottype == 1:
            print("choose an item:")
            for i, item in enumerate(self.items):
                print(f"{i}. {item.name} - {item.description}")
    def interact(self,choice,player):
        if self.loottype == 0:
            self.completed = True
            return True
        if self.loottype == 1:
            if choice >= 0 and choice <= len(self.items):
                player.inventory.append(self.items[int(choice)])
                print(f"You have selected {player.selected_weapon.name}.")
                self.completed = True
                return True
            print("Invalid choice, try again.")
        return False
    
    def getdoors(self):
        pass

class room_manager:
    def __init__(self):
        self.rooms = []
        self.roomnumber = 0
        self.current_room = None
        self.add_room(Room("Room 0", "The place you Began",[broken_axe(), broken_sword(), broken_spear()], None,1))
        self.create_room()
    def add_room(self, room):
        self.rooms.append(room)
    def create_room(self):
        #loottype = random.choices([0,1], weights=[0.5,0.5])[0]
        self.roomnumber += 1
        room = Room(f"Room {self.roomnumber}", "A randomly generated room.",[], Test_enemy("Goblin", 10))
        self.add_room(room)

if __name__ == "__main__":
    buffer = 18
    for x in range(10):
        r = Room(f"Room {x}", "A randomly generated room.",[], Test_enemy("Goblin", 10))
    running = True
    while running:
        player = Player()
        R = room_manager()
        R.current_room = R.rooms[0]
        adventure = True
        R.current_room.content(player)
        roomcomplete = False
        while not roomcomplete:
            choice = input()
            if choice == 'i':
                Player.show_inventory()
            else:
                roomcomplete = R.current_room.interact(int(choice),player)
                explore = True

        while adventure:

            if R.current_room.completed == False:
                R.current_room.content(player)
                roomcomplete = False
            while not roomcomplete:
                choice = input()
                if choice == 'i':
                    Player.show_inventory()
                else:
                    roomcomplete = R.current_room.interact(choice,player)
                    explore = True

            while explore:
                print("Do you want to Move (f)orward/(b)ack/(meditate) or (i)nventory?")
                choice = input().lower()
                if choice == 'i':
                    Player.show_inventory()
                else:
                    if choice == 'f':
                        if R.current_room == R.rooms[-1]:
                            R.create_room()
                            R.current_room = R.rooms[-1]
                        else:
                            R.current_room = R.rooms[R.rooms.index(R.current_room)+1]
                        explore = False

            if R.current_room.enemy:
                Enemy = R.current_room.enemy
                battle = True
            
            while battle:

                player.speed_current += player.speed
                Enemy.speed_current += Enemy.speed

                for body_part in Enemy.body_part_effects:
                    for effect in Enemy.body_part_effects[body_part]:
                        if hasattr(effect, 'over_time'):
                            outcome = effect.over_time(Enemy,body_part)
                            print(f"{Enemy.name} is affected by {effect.name} on {body_part.name}. Damage: {outcome[0]}, Duration: {outcome[1]}")
                            if outcome[1] <= 0:
                                Enemy.body_part_effects[body_part].remove(effect)
                                print(f"{Enemy.name} is no longer affected by {effect.name} on {body_part.name}.")
                if Enemy.health <= 0:
                    print(f"You defeated {Enemy.name}!")
                    battle = False
                    continue
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
                                break
                            else:
                                print(f"You SURVIVED the fatal blow to your {aim.name}!")
                    else:
                        print(f"{Enemy.name} missed!")
            player.speed_current = 0
            #player.inventory.append(loot_table["weapons"][random.choices(range(len(loot_table["weapons"])), weights=[item[1] for item in loot_table["weapons"]])[0]][0])
            
