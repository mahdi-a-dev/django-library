from django.urls import path
from . import views

app_name = "reminders"

urlpatterns = [
    # ex: reminders/my_reminders
    path("my_reminders/", views.my_reminders, name="my-reminders"),
    # ex: reminders/1
    path("<int:pk>/", views.reminder_detail, name="reminder-detail")
]

