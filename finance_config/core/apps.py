from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'finance_config.core'
    
    # def ready(self) -> None:
    #     import finance_config.core.signals.handlers