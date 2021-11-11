from django.apps import AppConfig


class QuickSearchConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quicksearch'

    def ready(self):
        import quicksearch.singals  # noqa

