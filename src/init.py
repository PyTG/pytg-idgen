import logging

from modules.idgen.IdGenManager import IdGenManager

def initialize():
    logging.info("Initializing idgen module...")

    IdGenManager.initialize()

def connect():
    pass

def load_manager():
    return IdGenManager.load()

def depends_on():
    return []