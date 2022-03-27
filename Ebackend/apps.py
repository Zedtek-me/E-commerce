from django.apps import AppConfig



class EbackendConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Ebackend'
    
    def ready(self) -> None:
        import Ebackend.signals