import random
from enum import Enum

Armour = Enum('Armour',[("Helmet",1),("Gloves",2),("Chest",3),("Shoes",4)])

class Unarmed:
    def __init__(self):
        self.attack_damage = 3
        self.effects = []
    def get_damage(self):
        return self.attack_damage

class Player:
    def __init__(self):
        self.armour = {Armour.Helmet:0,Armour.Gloves:0,Armour.Chest:0,Armour.Shoes:0}
        self.weapon = Unarmed()
        self.health_max = 30
        self.health = int(self.health_max)
    def damage(self,attack_recived):
        damage = attack_recived.get_damage()
        self.health -= damage
    def attack(self,target):
        target.damage(self.weapon)

