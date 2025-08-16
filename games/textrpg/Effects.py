from rpg import DamageType

class effect_base:
    def __init__(self):
        self.name = "Base Effect"
        self.description = "A base effect for testing purposes."
        self.damage = 0
        self.duration = 0
        self.effect = []


class Fire(effect_base):
    def __init__(self):
        super().__init__()
        self.name = "Fire"
        self.description = "A fire effect that burns the target."
        self.damage = 1
        self.duration = 1

        self.effect = [DamageType.Fire]

    def over_time(self, target,body_part):
        damage = target.damage(self, body_part)
        self.duration -= 1
        return damage, self.duration
    
    def apply_effect(self):
        return Fire()
        
    def get_damage(self):
        return self.damage,self.effect