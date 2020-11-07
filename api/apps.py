from django.apps import AppConfig

# make sure to add this app reference into the settings.py INSTALLED_APPS
# format: <app_name>.<file.py>.<class_name>
# e.g <api.apps.ApiConfig>
class ApiConfig(AppConfig):
    name = "api"
