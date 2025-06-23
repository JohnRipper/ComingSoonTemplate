


# Requirements


```bash

```


# How To Run:

```bash
python manage.py runserver
```

## Use other settings:
```bash
python manage.py runserver --settings=ComingSoonTemplate.settings.production
```
## Production notes:
On a Production Server: Your web server (Gunicorn, uWSGI) will use the wsgi.py file, which points to production.py.
