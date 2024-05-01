class Greetings:
    def __init__(self,firstname,lastname):
        self._firstname = firstname
        self._lastname = lastname
    
    @property
    def firstname(self):
        return self._firstname
    @property
    def lastname(self):
        return self._lastname
    
    def display(self):
        print(f"hi {self.firstname} {self.lastname}")

