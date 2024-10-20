import shelve
from param import *
from config import *

class Save:
    def __init__(self):
        self.file=shelve.open('data')

    def save(self):
        self.file['dancing_dude'] = dancing_dude
        self.file['FPS'] = FPS
        self.file['mouse_effect']=mouse_effect
        self.file['custom1']=custom1
        self.file['custom2'] = custom2
        self.file['custom3'] = custom4

    def add(self, name, value):
        self.file[name]=value

    def get(self, name):
        return self.file[name]

    def __del__(self):
        self.file.close()