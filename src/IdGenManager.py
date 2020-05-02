import yaml, os

import urllib.request

from modules.pytg.Manager import Manager
from modules.pytg.ModulesLoader import ModulesLoader

class IdGenManager(Manager):
    @staticmethod
    def initialize():
        IdGenManager.__instance = IdGenManager()

        return

    @staticmethod
    def load():
        return IdGenManager.__instance

    def generate_id(self, id_class):
        file_path = "{}/ids.yaml".format(ModulesLoader.get_module_content_folder("idgen"))

        ids = yaml.safe_load(open(file_path, 'r'))

        if id_class not in ids:
            ids[id_class] = 0
        else:
            ids[id_class] += 1

        generated_id = ids[id_class] 

        yaml.safe_dump(ids, open(file_path, "w"))

        return generated_id