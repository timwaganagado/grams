from argparse import Action
from scene import *

A = Action

class gaming (Scene):
    def setup(self):
        pass
    def update(self):
        pass

if __name__ == '__main__':
    run(gaming(), PORTRAIT,show_fps=True)