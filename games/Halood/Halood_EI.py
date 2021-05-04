import pygame as pg
vec = pg.math.Vector2
screen = pg.display.set_mode((1920, 1080),pg.FULLSCREEN,display = 1)
class enemy():
    def __init__(self):
        self.null = 0
    def boot():
        C = enemy.conrift()
        C.vec = vec(43,20)
        C.health = 50
        C.combat_animation = {1:conrift_combat_img,2:conrift_combat2_img,3:conrift_combat3_img}
    class conrift():
        def __init__(self):
            self.vec = 0
            self.health = 0
            self.combat_animation = 0
        

conrift_combat_img = pg.image.load('images/Layer 1_conrift_combat1.png').convert_alpha()
conrift_combat_img = pg.transform.scale(conrift_combat_img, (256, 256))
conrift_combat2_img = pg.image.load('images/Layer 1_conrift_combat2.png').convert_alpha()
conrift_combat2_img = pg.transform.scale(conrift_combat2_img, (256, 256))
conrift_combat3_img = pg.image.load('images/Layer 1_conrift_combat3.png').convert_alpha()
conrift_combat3_img = pg.transform.scale(conrift_combat3_img, (256, 256))
