# flask-google-login

Installation:
```bash
$ pip install -r requirements.txt
```

Create config files:
```bash
$ cp -p app_config/__init__.py.example app_config/__init__.py
$ cp -p config/__init__.py.example config/__init__.py
```

Migraton:
```bash
$ FLASK_APP=manage.py flask db init
$ FLASK_APP=manage.py flask db migrate
$ FLASK_APP=manage.py flask db upgrade
$ FLASK_APP=manage.py flask db downgrade
```

Run:
```bash
$ python3 run.py
```
