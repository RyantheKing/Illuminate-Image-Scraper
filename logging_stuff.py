import logging

logger = logging.getLogger(__name__) 

logger.setLevel(logging.DEBUG) 

def add_file(file): 
    logger.addHandler(logging.StreamHandler(file)) 

def debug(msg, *args, **kwargs): 
    print(msg) 
    
    logger.debug(str(msg), *args, **kwargs) 