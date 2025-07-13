import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)


class EventsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "events"

    def ready(self):
        import events.signals  # fmt: skip
        logger.info(type(events.signals))
