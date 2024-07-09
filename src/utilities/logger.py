import logging
import os
import utilities.utils as utils

LOGGER_PATH = os.getenv('LOCALAPPDATA') + '\\' + os.path.basename(utils.ROOT_DIR) + '\\logs'

class Logger:
    def __init__(self, name, log_file=LOGGER_PATH + '\\debug.log', level=logging.DEBUG):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(level)
        
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        
        ch = logging.StreamHandler()
        ch.setLevel(level)
        
        fh = logging.FileHandler(log_file)
        fh.setLevel(level)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        ch.setFormatter(formatter)
        fh.setFormatter(formatter)
        
        self.logger.addHandler(ch)
        self.logger.addHandler(fh)
    
    def get_logger(self):
        return self.logger