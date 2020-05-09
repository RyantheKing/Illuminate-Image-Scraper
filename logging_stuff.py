import logging
import sys

logger = logging.getLogger(__name__) 

logger.setLevel(logging.DEBUG) 

logger.addHandler(logging.StreamHandler(sys.stdout)) 

def add_file(file): 
    logger.addHandler(logging.StreamHandler(file)) 

def debug(msg, *args, **kwargs): 
    logger.debug(str(msg), *args, **kwargs) 