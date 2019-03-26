# Tutorial-testing-existing-project-live-81
Tutorial made from 'Live de Python #81 - Testando o que está pronto' (Eduardo Mendes) by Marcus Mariano 

---

## Introduction

Testing projects that already exist.

Packages

- flask
- flask-sqlalchemy
- flask-migrate
- flask-marshmallow
- marshmallow-sqlalchemy 

Dev-packages
- requests
- ipdb
- coverage

---

## Installation

```sh

pipenv install --dev

```

---

## How to Run

```sh
export FLASK_APP=app
export FLASK_ENV=Development
export FLASK_DEBUG=True

flask run
```

Creat DB
Make Magrations
```sh
flask db init 

flask db migrate

flask db upgrade
```

---

## Tests

Testing Flask API
```sh

python -m unittest -v tests/tests_flask_api.py

```

Run Coverage
```sh

coverage run --source=app -m unittest discover -s tests

```

Run Coverage Report
```sh

coverage report

```

Run Coverage generate HTML
```sh

coverage html

```

---

## Documentation

---

## License

Code and documentation are available according to the GNU GENERAL PUBLIC LICENSE Version 3 (see [LICENSE](https://www.gnu.org/licenses/gpl.html)).
