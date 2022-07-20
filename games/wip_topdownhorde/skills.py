from multiprocessing.context import SpawnContext
import shelve
import os , sys


def test():
    print('working')

def new_skill(name,description,action=dict,specific_skill=str):
    #global skill,skill_dict
    skill_dict.update({name:{'description':description,'action':action}})
    if specific_skill == 'all':
        skill.append(name)
        return
    if specific_skill not in specific_skill_dict:
        specific_skill_dict.update({specific_skill:[name]})
        return

    specific_skill_dict[specific_skill].append(name)
    
def get_skills(highscores):
    return highscores['skill_dict'],highscores['skill'],highscores['specific_skill_dict']

#def speacialskill(target):
#    pass
#    #over.skills.remove(target)
#    target()
#
def Special_investment():
    pass
spec = [Special_investment]
    
if __name__ == '__main__':
    skill_dict = {} 
    skill = []
    specific_skill_dict = {}
    
    filename = os.path.dirname(sys.argv[0])
    highscores = shelve.open(filename+'/scorestopdown.txt',writeback=True)
    new_skill('Bullet Damage Increase','Increases Bullet Damage by 25%',{'damage':0.25},'all')
    new_skill('Range Collection Increase','Increases exp Range',{'range':20},'all')
    new_skill('Swift Feet','Increases Movement Speed by 0.75',{'speed':-0.75},'all')
    new_skill('Fire rate','Increases Fire Rate',{'fire_speed':-50},'all')
    new_skill('Bullets From Hell','Bullets do 1 extra damage',{'flat_damage':1},'Phoenix Gun')
    new_skill('Spraying and Praying','Lose some Damage for Movement and Fire Rate',{'damage':-0.25,'speed':-0.50,'fire_speed':-50},'Phoenix Gun')
    new_skill('Bouncing Bolts','Lightning bounces from enemies',{'lightning_bounce':1},'Lightning')
    new_skill('Bigger Bolts','Lightnings area grows',{'lightning_size':0.25},'Lightning')
    new_skill('Falling Through','Bullets Will Pierce Through 1 More Enemy',{'bullet_pierce':1},'Phoenix Gun')
    new_skill('Further Shock','Increase The Range of Lightning',{'lightning_range':1},'Lightning')
    new_skill('An Investment','invest some damage to get more later',{'empty':0},0)
    highscores['skill_dict'] = skill_dict
    highscores['skill'] = skill
    highscores['specific_skill_dict'] = specific_skill_dict
        