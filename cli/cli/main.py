import typer
from os import system as shell, popen as output

app = typer.Typer()

db_types = ['postgres', 'postgresql', 'mysql', None]

@app.command()
def run(env: str = 'dev', db: str | None = None):
    '''
    Run app in different envs & db engines
    '''
    if db not in db_types:
        typer.echo('Invalid db engine')
        raise typer.Exit()

    if db:
        current_content = output("sed '1,2 d' .env").read().strip()
        port = 3306 if db == 'mysql' else 5432
        content = f'DB_ENGINE={db}\nDB_PORT={port}\n' + current_content
        shell(f'echo "{content}" > .env')

    match env:
        case 'dev':
            shell('uvicorn app:app --reload')
        case 'prod':
            shell('uvicorn app:app --host 0.0.0.0 --port 80 --workers 5')
        case 'docker':
            shell('uvicorn app:app --reload --host 0.0.0.0 --port 80')
        case _:
            typer.echo('Invalid env')

@app.command()
def test(html: bool = False):
    '''
    Run pytest app tests
    & Generates html report
    '''
    if html:
        typer.echo('Running tests & generating html report...')
        shell('pytest --pdb -v --html=tests/report.html --self-contained-html tests/')
    else:
        typer.echo('Running tests...')
        shell('pytest --pdb -v tests/')

@app.command()
def coverage(html: bool = False):
    '''
    Shows test coverage
    & Generates html report
    '''
    if html:
        typer.echo('Generating coverage html report...')
        shell('pytest --cov-report html:tests/coverage --cov-report term-missing --cov=app tests/')
    else:
        typer.echo('Running test coverage...')
        shell('pytest --cov-report term-missing --cov=app tests/')
