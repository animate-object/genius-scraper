import json
import os.path

from app.main.util.exceptions import NoSuchPropertyException


class ConfigUtil:
    def __init__(self):
        self.config_json = {}
        with open(self.config_file_name(), 'r') as configIn:
            self.config_json = json.load(configIn)

    def config_file_name(self):
        return os.path.join(
            os.path.dirname(__file__), '../../resources/app-config.json'
        )

    def get_property(self, property_name):
        if property_name in self.config_json.keys():
            return self.config_json[property_name]
        raise NoSuchPropertyException("Failed to find requested property", property_name)

