from django.core.management.base import BaseCommand
from reminders.services import create_upcoming_reminders, create_overdue_reminders, create_returned_reminders


class Command(BaseCommand):
 
    def handle(self, *args, **options):
        """
        Generate upcoming and overdue reminders.
        
        This command is intended to be executed periodically,
        for example cron.
        """
        create_upcoming_reminders()
        create_overdue_reminders()
        
        self.stdout.write(
                self.style.SUCCESS("Generate Reminders Command Worked Successfully.")
            )
        