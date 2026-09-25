from django.core.management.base import BaseCommand
from reminders.services import create_upcoming_reminders, create_overdue_reminders, create_returned_reminders


class Command(BaseCommand):
 
 
    def handle(self, *args, **options):
        create_upcoming_reminders()
        create_overdue_reminders()
        