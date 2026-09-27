from django.urls import path
from . import views

app_name = "reports"

urlpatterns = [
    # ex: /reports/
    path("", views.reports, name="reports")
]