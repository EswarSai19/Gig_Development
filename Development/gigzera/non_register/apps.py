from django.apps import AppConfig


class NonRegisterConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'non_register'
