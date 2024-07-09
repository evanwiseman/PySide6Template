import json
import os
import utilities.utils as utils

SETTINGS_FILE = os.getenv('LOCALAPPDATA') + '\\' + os.path.basename(utils.ROOT_DIR) + '\\settings.json'

class Settings:
    def __init__(self):
        self.theme:str = 'dark_teal.xml'
    
    def to_json(self): 
        return self.__dict__
    
    @staticmethod
    def from_json(data):
        settings = Settings()
        settings.__dict__.update(data)
        return settings
    
    def save(self):
        directory = os.path.dirname(SETTINGS_FILE)
        if not os.path.exists(directory):
            os.makedirs(directory)
        
        with open(SETTINGS_FILE, 'w') as file:
            json.dump(self.to_json(), file)
    
    def load(self):
        if not os.path.exists(SETTINGS_FILE):
            self.__init__()
            self.save()
            return
        
        with open(SETTINGS_FILE, 'r') as file:
            data = json.load(file)
            self.__dict__.update(data)