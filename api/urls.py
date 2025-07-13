from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EventViewset, ScheduleRequestViewset

app_name = "api"  # Optional: namespace for your app URLs

router = DefaultRouter()
router.register(r"events", EventViewset, basename="events")
router.register(r"schedule", ScheduleRequestViewset, basename="schedule")

urlpatterns = [
    # path("", IndexViewset.as_view(), name="index"),
    path("calendar/", include(router.urls)),
]
