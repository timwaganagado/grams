
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