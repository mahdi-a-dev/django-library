# Library Management System

A simple library management system built with Django.

The project allows users to browse books, borrow and return them,
and receive reminders related to their loans.

Administrators can manage the library through Django Admin and view system reports.

## Technologies
- Python
- Djago
- SQLite
- HTML / CSS
- Django Template Engine

## Reminders
The project uses a background reminder service to check loans and create reminders
for borrowed, upcoming, overdue, and returned book.

To run the reminder service manually:

`python manage.py generate_reminders`

For automatic execution, the command can be scheduled using cron on linux or Task Scheduler on Windows.
