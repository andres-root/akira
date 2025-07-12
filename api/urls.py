from django.urls import path

from .views import IndexViewset

app_name = "api"  # Optional: namespace for your app URLs

urlpatterns = [
    path("", IndexViewset.as_view(), name="index"),
]
