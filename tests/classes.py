
class almostfunny:
    def __init__(self):
        self.thing = 'weird'
    def howfunny(self):
        if self.thing == 'weird':
            return

class funny(almostfunny):
    def __init__(self):
        super().__init__()
    def howfunny(self):
        super().howfunny()
        print('still weird')

funny1 = funny()

funny1.howfunny()

class thesmacker:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return str(self.name)
    
ll = thesmacker('potato')
print(ll.name == 'potato')