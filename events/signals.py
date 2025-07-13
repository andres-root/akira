import logging

from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver

from agents.services import CalendarService
from events.models import Event, ScheduleRequest, Status
from events.utils import parse_datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
calendar_service = CalendarService()


@receiver(post_save, sender=ScheduleRequest)
def create_event(sender, instance, created, **kwargs):
    if created:
        try:
            # Update the status to processing and save it
            instance.status = Status.PROCESSING
            instance.save()
            # Parse the event
            event = calendar_service.parse_event(instance.prompt)
            # Create the event
            with transaction.atomic():
                event = Event.objects.create(
                    title=event.title,
                    description=event.description,
                    start_date=parse_datetime(event.start_datetime),
                    end_date=parse_datetime(event.end_datetime),
                    schedule_request=instance,
                )
                event.save()

                # Update the status to completed and save it
                instance.status = Status.SCHEDULED
                instance.save()
                logger.info(f"Event created: {event.title}")
        except Exception as e:
            logger.error(f"Error creating event: {e}")
            print("error: ", str(e))
            instance.status = Status.FAILED
            instance.save()
