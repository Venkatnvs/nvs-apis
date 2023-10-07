import os
import json
from django.conf import settings
from django.core.cache import cache

def load_json_data():
    path = os.path.join(settings.BASE_DIR, 'data_set/states_dist.json')
    with open(path, 'r') as file:
        data = json.load(file)
        cache.set('state_data', data)

    file_path = os.path.join(settings.BASE_DIR,'data_set/pincode.json')
    with open(file_path, 'r') as json_file:
        data2 = json.load(json_file)
        cache.set('zip_data', data2)