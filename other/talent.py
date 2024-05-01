class Talent:
    def __init__(self,talent_name,talent_id,talent_cat):
        self.talent_name = talent_name
        self.talent_id = talent_id
        self.talent_cat = talent_cat
    def mut_name(self,new):
        self.talent_name = new
    def mut_id(self,new):
        self.talent_id = new
    def mut_cat(self,new):
        self.talent_cat = new
    def show_name(self):
        return self.talent_name
    def show_id(self):
        return self.talent_id
    def show_cat(self):
        return self.talent_cat
    def toString(self):
        print(f"Talent Name: {self.show_name()}")
        print(f"Talent ID: {self.show_id()}")
        print(f"Talent Category: {self.show_cat()}")
