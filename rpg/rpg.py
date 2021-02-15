aohe = 3
aohp = 5
cd_a = 0
cd_f = 0
cd_s = 0
from findenemy import find
from attind import attackindex
import random
levels = 1
enemies = [1,2]
while levels <= 4:
    tle = random.choice(enemies)
    fe,aohe,f_a,s_a,t_a = find(tle)
    print('Level',levels)
    while aohe > 0 and aohp > 0:
        print(f'{fe} Health bar')
        hp_be = (chr(9608)+'|')*(aohe-1)+chr(9608)
        print(hp_be)
        print()
        print()
        print('Player health')
        hp_bp = (chr(9608)+'|')*(aohp-1)+chr(9608)
        print(hp_bp)
        print('1.axe 2.fist 3.spell')
        w_p = int(input('Which weapon (1/2/3): '))
        while w_p != 0:
            if w_p == 1:
                if cd_a <= 0:
                    aohe = aohe - 2
                    cd_a = 1
                    cd_a = cd_a - 1
                    cd_s = cd_s - 1
                    w_p = 0
                else:
                    print('Weapon on cooldown')
                    w_p = int(input('Which weapon (2/3): '))
            elif w_p == 2:
                aohe = aohe - 1
                w_p = 0
                cd_a = cd_a - 1
                cd_s = cd_s - 1
            elif w_p == 3:
                if cd_a <= 0:
                    aohe = aohe - 3
                    cd_s = 2
                    cd_a = cd_a - 1
                    cd_s = cd_s - 1
                    w_p = 0
                else:
                    print('Weapon on cooldown')
                    w_p = int(input('Which weapon (1/2): '))
            else:
                w_p = int(input('Which weapon (1/2/3): '))
        
        
        if aohe > 0:
            e_a = 1
        else:
            e_a = 0
        while e_a == 1:
            e_p = random.randint(1,3)
            if e_p == 1:
                aohp,e_p,e_a = attackindex(f_a,aohp,e_p)
            elif e_p == 2:
                aohp,e_p,e_a = attackindex(s_a,aohp,e_p)
            elif e_p == 3:
                aohp,e_p,e_a = attackindex(t_a,aohp,e_p)
    
    
    if aohe <= 0:
        levels = levels + 1
    else:
        print('You lose')
        levels = 5
print('You destroyed all the monsters')