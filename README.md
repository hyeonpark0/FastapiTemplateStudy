<div align="center">
<img height="100" width="110" style="margin-bottom: -70px" alt="FastAPI Template" src="https://gitlab.com/uploads/-/system/project/avatar/33491624/fastapi.png">
<br>
<h1 align="center" style="text-decoration: none;"> FastAPI &nbsp;TEMPLATE </h1>
</div>

<br>
<br>

**Source Code**: <a href="https://gitlab.com/juanesquintero/fastapi-template" target="_blank"> https://gitlab.com/juanesquintero/fastapi-template </a>

---

## About
This project is a template or scaffolding for FastAPI framework with Python 3.10, to easily start your project without wasting time on basic  big project implementations like:
  - Development Guidelines
  - Clean folder tree
  - FastAPI advanced config & features
  - Application CLI
  - Docker containerization
  - SQL database connection
  - Unit Testing
  - Coverage report
  - Linting
  - Git hooks

<a href="https://nabajyotiborah.medium.com/fastapi-scalable-project-structure-with-docker-compose-45dc3a9fb4c6">
<img height="300" width="500" alt="FastAPI Template" src="https://miro.medium.com/max/1400/1*Thx7VapgMNGDOoLZ2kxBuQ.png">
</a>

<br>

<small>
  All commands in this project must be run on a <b>BASH</b> type terminal.
  (You can use git-bash in windows)
</small>

---

<br>

## Set up local environment
This template can be run it on your local machine or in a docker container,
so you can install just Docker or in place Pyenv and MySQL.

  <b>Pyenv</b> <br>
  https://help.dreamhost.com/hc/en-us/articles/216137637 <br>
  https://realpython.com/intro-to-pyenv/ <br>
  https://github.com/pyenv/pyenv#installation

  <b>venv</b> <br>
  https://docs.python.org/es/3/library/venv.html

  <b>Docker</b> <br>
  https://www.docker.com/resources/what-container <br>
  https://www.docker.com/get-started

  <small>
    If you are in Windows it's better to just install the python specific version,
    since the pyenv is not supporting windows currently.
  </small>

---

<br>

## TechStack

<i>Python</i> 3.10.2
https://www.python.org/downloads/release/python-3102/

<i>FastAPI</i> 0.73.0
https://fastapi.tiangolo.com/

<i>Typer</i>
https://typer.tiangolo.com/

<i>PostgreSQL</i> 14.2
https://www.postgresql.org/docs/14/release-14-2.html

<i>MySQL</i> 8.0
https://dev.mysql.com/doc/relnotes/mysql/8.0/en/

---

<br>

## SetUp

  Clone this repo

  ```console
  git clone https://gitlab.com/juanesquintero/fastapi-template.git
  ```

  Create <b><i>.env</i></b> file with the environment variables in the project root.

  ```dosini
  DB_ENGINE=postgres
  DB_PORT=5432

  DB_HOST=localhost
  DB_SCHEMA=academy
  DB_USER=root
  DB_PASSWORD=admin
  ```
  <small>Please leave DB_ENGINE, DB_PORT at the top 2 lines of the file</samll>

  ### Locally

  After install the local environment with pyenv use the certain python version.
  ```console
  $ pyenv shell 3.10.2
  ```

  Or just specify the python version if you are not using pyenv with the following prefix in each command.

  ```console
  $ python3.10 -m
  ```

  Upgrade your pip manager.
  ```console
  $ pip install --upgrade pip
  ```

  Create a <b><i>virtual environment</i></b> with python virtualenv
  https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/

  ```console
  $ pip install virtualenv
  $ python -m venv venv
  ```

  Activate the <b><i>virtual environment</i></b>

  ```console
  $ source venv/bin/activate
  ```

  Check the python version of the venv created above
  ```console
  (venv)$ which python
  ```

  ### Containerized

  After install [Docker Desktop](https://www.docker.com/get-started), create the images & instance the containers.

  ```console
  $ docker-compose up
  ```

The FastAPI app now is running on [http://localhost:8001](http://localhost:8001)
MySQL database on localhost:3306
PostgreSQL database on localhost:5432
Adminer GUI on [localhost:8081](http://localhost:8081) 
pgAdmin GUI on [localhost:5431](http://localhost:5431)

## Database
You can rather install MySQL and PostgreSQL engine locally or simply use the Docker containers created above.
Remember to change the .env connection variables if necessary.

In the <i>app/db/sql/</i> folder you will find the needed DDL & DML scripts for the proper database setup.
To enter to the Database through a UI, manage and execute the scripts you can use

### Changes
  If some DDL changes are included to the database is preferred to remove the db container & the data folder (postgres_data or mysql_data) 

#### GUI tools
Included in the docker containers are 2 GUI tools; "<b>Adminer</b>" for many sql engines including MySQL & "<b>pgAdmin</b>" for PostgreSQL.

If you prefer to install some on your machine we recommend one of the following... <br>
[MySQL Workbench](https://dev.mysql.com/downloads/workbench/) <br>
[phpMyAdmin](https://www.phpmyadmin.net/downloads/) <br>
[pgAdmin](https://www.pgadmin.org/) <br>
[Navicat](https://www.navicat.com/en) <br>

Use the same <b><i>.env</b></i> parameters to create the db connection.
If you are using a Docker container remember to not use localhost as server, instead use <b><i>host.docker.internal</i></b>.

---

<br>

## Folder Structure
    📦fastapi-template
     ┣ 📂app
     ┃ ┣ 📂db
     ┃ ┣ 📂models
     ┃ ┣ 📂routers
     ┃ ┣ 📂schemas
     ┃ ┣ 📂shared
     ┃ ┣ 📜__init__.py
     ┃ ┗ 📜main.py
     ┣ 📂cli
     ┣ 📂tests
     ┣ 📜.dockerignore
     ┣ 📜.env
     ┣ 📜.gitignore
     ┣ 📜.pre-commit-config.yaml
     ┣ 📜.python-version
     ┣ 📜DEVGUIDE.md
     ┣ 📜Dockerfile
     ┣ 📜README.md
     ┣ 📜config.py
     ┣ 📜docker-compose.yml
     ┣ 📜requirements-dev.txt
     ┣ 📜requirements.txt
     ┗ 📜run.py

<br>

## Installation
<div class="termy">

```console
(venv)$ pip install requirements.txt
```

</div>

If you are in dev mode use:

<div class="termy">

```console
(venv)$ pip install requirements-dev.txt
```

</div>


### Run
  The <b><i>run.py</i></b> file has dev environment parameters to run the application.
  ```console
  python run.py
  ```


### Check it

Open your browser at <a href="http://127.0.0.1:8000/" class="external-link" target="_blank"> http://localhost:8000/ </a>

You will see the JSON response as:

```JSON
{"api": "FastAPI Template"}
```

<br>

## CLI
This template counts with a custom CLI to execute clear and simple commands instead long and tedious native commands.
https://typer.tiangolo.com/tutorial/package/

<i><small>
Remember if you are running the app containerized to run these CLI commands inside the docker container console
<small></i>

  Set up the application CLI running the following commands in this location...

  <i>cli/</i>
  ```console
  (venv)$ poetry install

  (venv)$ poetry build

  (venv)$ pip install dist/cli-0.1.0-py3-none-any.whl
  ```


  Show available commands
  ```console
  (venv)$ app-cli --help
  ```

  Run or start api server <small>(dev env & postgres db by default)</small>
  ```console
  (venv)$ app-cli start

  (venv)$ app-cli start --help
  ```

  In prod mode
  ```
  (venv)$ app-cli start --env=prod
  ```

  With mysql engine db
  ```
  (venv)$ app-cli start --db=mysql
  ```

To change the application CLI command just modify the following line on the  <b><i>cli/cli/pyproject.toml</i></b> file.
And the Dockerfile entrypoint.
```TOML
[tool.poetry.scripts]
app-cli = "cli.main:app"
```

<br>

## Testing

  Run tests
  ```console
  (venv)$ app-cli test
  ```
  <small>pytest -v tests/</small>

  Run tests & generate html report
  ```console
  (venv)$ app-cli test --html
  ```
  <small>pytest -v --html=tests/report.html --self-contained-html tests/</small>

  Run coverage
  ```console
  (venv)$ app-cli coverage
  ```
  <small>pytest --cov-report term-missing --cov=app tests/</small>

  Run coverage & generate html Report
  ```console
  (venv)$ app-cli coverage --html
  ```
  <small>pytest --cov-report html:tests/coverage --cov-report term-missing --cov=app tests/</small>

<br>

<br>

## Pre-Commit Hooks
  The pre-commit git hooks consists on run some checks before confirm or commit your staged changes on the local repo, the <i>.pre-commit-config.yml</i> file contains the checks. <br>
  https://pre-commit.com/ <br>
  https://pypi.org/project/pre-commit/ <br>

  To set it up, you need to run this command on the root folder of the project
  ```console
  (venv)$ pre-commit
  (venv)$ pre-commit autoupdate
  ```

  It runs each time you try to commit your changes, or you can just run it manually
  ```console
  (venv)$ pre-commit run --all-files
  ```


  The following local checks are implemented:

  - Linting with PyLint
  ```console
  (venv)$ pylint *
  ```

  - Testing with PyTest
  ```console
  (venv)$ pytest -v tests/
  ```
<br>

## API Docs

### Swagger - OpenAPI

Now go to <a href="http://127.0.0.1:8000/docs" class="external-link" target="_blank"> http://localhost:8000/docs </a>

You will see the automatic interactive API documentation (provided by <a href="https://github.com/swagger-api/swagger-ui" class="external-link" target="_blank">Swagger UI</a>):

![Swagger UI](https://fastapi.tiangolo.com/img/index/index-01-swagger-ui-simple.png)

### ReDoc

And now, go to <a href="http://127.0.0.1:8000/redoc" class="external-link" target="_blank">http://localhost:8000/redoc </a>

You will see the alternative automatic documentation (provided by <a href="https://github.com/Rebilly/ReDoc" class="external-link" target="_blank">ReDoc</a>):

![ReDoc](https://fastapi.tiangolo.com/img/index/index-02-redoc-simple.png)


<br>

## Python Packages

**Core** <br>
[pydantic==1.9.0](https://pydantic-docs.helpmanual.io/) <br>
[fastapi==0.73.0](https://fastapi.tiangolo.com/) <br>
[uvicorn==0.17.0.post1](https://www.uvicorn.org/)

[python-dotenv==0.19.2](https://pypi.org/project/python-dotenv/) <br>
[cryptography==36.0.1](https://pypi.org/project/cryptography/)

**Database** <br>
[SQLAlchemy==1.4.31](https://www.sqlalchemy.org/) <br>
[PyMySQL==1.0.2](https://pymysql.readthedocs.io/en/latest/) <br>
[psycopg2-binary==2.9.3](https://www.psycopg.org/docs/)

**Utils** <br>
[pydash==5.1.0](https://pydash.readthedocs.io/en/latest/) <br>
[dotmap==1.3.23](https://pypi.org/project/dotmap/)

**CLI** <br>
[poetry==1.1.13](https://python-poetry.org/) <br>
[poetry-core==1.0.7](https://pypi.org/project/poetry-core/) <br>
[typer==0.4.0](https://typer.tiangolo.com/)

#### Development Packages
**Testing** <br>
[requests==2.27.1](https://docs.python-requests.org/en/latest/) <br>
[pytest==7.0.0](https://docs.pytest.org/en/7.1.x/) <br>
[pytest-html==3.1.1](https://pytest-html.readthedocs.io/en/latest/) <br>
[coverage==6.3.1](https://coverage.readthedocs.io/en/6.3.2/) <br>
[pytest-cov==3.0.0](https://pytest-cov.readthedocs.io/en/latest/) <br>

**Linting** <br>
[pylint==2.5.0](https://pypi.org/project/pylint/) <br>
[pylint-plugin-utils==0.6](https://pypi.org/project/pylint-plugin-utils/) <br>
[autopep8==1.5.6](https://pypi.org/project/autopep8/) <br>

**Git** <br>
[enforce-git-message==1.0.1](https://pypi.org/project/enforce-git-message/) <br>
[pre-commit==2.15.0](https://pre-commit.com/) <br>

<br>

## License

This project is licensed under the terms of the MIT license.
