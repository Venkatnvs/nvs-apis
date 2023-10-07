from django.apps import AppConfig
from .utils import load_json_data

class Api1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'api1'

    def ready(self):
        load_json_data()
