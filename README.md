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

```bash
python manage.py generate_reminders
```

For automatic execution, the command can be scheduled using cron on linux or Task Scheduler on Windows.

## Docker

### 1.Create `.env`

Copy `.env.example` to `.env`:

```bash
cp .env.example .env
```

Then set your own Django secret key in `.env`:

```env
DJANGO_SECRET_KEY=your-secret-key
DEBUG=1
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

### 2.Build and run

```bash
docker compose up --build
```

Open:
http://localhost:8000

### Django commands

```bash
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
```

### Stop
```bash
docker compose down
```
