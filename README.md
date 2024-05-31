
## Installation Manual

Ensure you have the following items installed on your system:
- Python 3.x

### 1. Install Django

Install Django using pip:

```bash
python -m pip install Django
```

### 2. Install the relational DataBase

- [PostgreSQL Installation](https://www.postgresql.org/download/)

NOTE: For this project i use PostgreSQL, but you can use any relational database.

### 3. Install psycopg2

Psycopg2 is an adpater to connect Django to PostgreSQL. To install, just use:

```bash
pip install psycopg2-binary
```

### 4. Configure the database

When you have the database created, you should go to psql and execute these commands:

```bash
CREATE DATABASE francesinha;
CREATE USER 'your_user' WITH PASSWORD 'your_user_password';
GRANT ALL PRIVILEGES ON DATABASE francesinha TO 'your_user';
```

### 5. Configure the Django to use PostgreSQL

In your Django project's `settings.py` file, configure the connection to the PostgreSQL database:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'francesinha',
        'USER': 'your_user',
        'PASSWORD': 'your_user_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 6. Apply Database Migrations

Inside of a terminal, go to the directory where you have the project and apply the database migrations to create the necessary tables:

```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create a Superuser

Create a superuser to access the Django admin interface:

```bash
python manage.py createsuperuser
```

### 8. Run the Server

Start the Django server:

```bash
python manage.py runserver
```

### 9. Access the Application

Open your browser and access the application at [localhost:8000](http://localhost:8000).

---
