import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _


class Status(models.TextChoices):
    NEW = "pending"
    PROCESSING = "processing"
    SCHEDULED = "scheduled"
    CANCELLED = "cancelled"
    FAILED = "failed"


class ScheduleRequest(models.Model):
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    prompt = models.TextField(_("Prompt"))
    status = models.CharField(_("Status"), max_length=255, choices=Status.choices, default=Status.NEW)
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    def __str__(self):
        return f"ScheduleRequest {self.id}"


class Event(models.Model):
    uuid = models.UUIDField(_("UUID"), default=uuid.uuid4, editable=False, unique=True)
    title = models.CharField(_("Title"), max_length=255)
    description = models.TextField(_("Description"))
    start_date = models.DateTimeField(_("Start date"))
    end_date = models.DateTimeField(_("End date"))
    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    # Relations
    schedule_request = models.ForeignKey(ScheduleRequest, on_delete=models.CASCADE, related_name="events")

    def __str__(self):
        return self.title
