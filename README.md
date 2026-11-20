# BoxInventory

A small Django application for recording storage boxes and the items inside them. It includes searchable inventory, per-box pages, an all-boxes report, individual box reports, and browser printing.

## Requirements
- Python 3.10 or newer
- pip

## Install and run
Open a terminal in this directory and run:

```bash
python -m venv .venv
```

Activate the environment:

- macOS/Linux: `source .venv/bin/activate`
- Windows: `.venv\\Scripts\\activate`

Install Django and initialize the database:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

## Main features
- Create a box with a unique box number and optional notes.
- Add, edit, and delete item descriptions in each box.
- Search by box number or item description.
- View a report of all boxes and their contents.
- View and print an individual box contents report.
- Optional Django admin at `/admin/` (create an administrator with `python manage.py createsuperuser`).

## Notes
This starter project uses SQLite and Django's development server. Before putting it on a public server, set a private `SECRET_KEY`, set `DEBUG = False`, configure `ALLOWED_HOSTS`, use HTTPS, and add authentication/authorization appropriate for your use.
