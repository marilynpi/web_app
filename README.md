# Web App


## Requeriments

- PostgreSQL
- Python 3.8.10


## Environment Variables

To run this project, you will need to add the following environment variables to your `.env` file in directory root.

`HOST`
`DB_USER`
`DB_PASSWORD`
`DB_HOST`
`DB_PORT`
`DB_DATABASE`

## Installation

Create a new virtualenv:

```bash
  python3 -m venv venv

```

Activate the virtualenv:

```bash
  source venv/bin/activate

```

Install python requirements:

```bash
  pip install -r requirements.txt

```

Set up database:

```bash
  python3 manage.py migrate

```

Create the admin superuser:

```bash
  python manage.py createsuperuser

```

## Run Locally

Start web server:

```bash
  python3 manage.py runserver

```

## Admin theme based on:

- [Django Admin Volt](https://github.com/app-generator/django-admin-volt)
- [Volt Dashboard Django](https://github.com/app-generator/django-volt-dashboard)

