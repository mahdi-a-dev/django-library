from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("books.urls")),
    path("accounts/", include("accounts.urls")),
    path("loans/", include("loans.urls")),
    path("reminders/", include("reminders.urls")),
    path("reports/", include("reports.urls"))
]
