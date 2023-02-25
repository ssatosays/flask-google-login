# flask-google-login

Installation:
```bash
$ pip install -r requirements.txt
```

Create private.key & server.crt:
```bash
$ openssl genrsa -out private.key 2048
$ cat private.key |openssl rsa -pubout > public.key
$ openssl req -new -key private.key > server.csr
$ cat server.csr |openssl x509 -req -days 398 -signkey private.key > server.crt
```

Create config files & edit:
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
