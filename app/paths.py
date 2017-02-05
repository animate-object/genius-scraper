import os
import os.path

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

CONFIG_JSON = os.path.join(APP_ROOT, 'resources\\app-config.json')

DATA_DIR = os.path.join(APP_ROOT, 'data\\')

#  [print(x) for x in [APP_ROOT, CONFIG_JSON, DATA_DIR]]
