import os
from pydantic import BaseSettings
from logging import DEBUG, getLogger, basicConfig, FileHandler, Formatter, Logger

base_dir = os.path.dirname(os.path.abspath(__file__))

'''LOGGING CONFIG'''
log_format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s'
log_dir = base_dir + '/logs'

def create_logger(level: str):
    level_upper = level.upper()
    file_handler = FileHandler(f'{log_dir}/{level_upper}.log')
    file_handler.setFormatter(Formatter(log_format))
    logger = getLogger(f'{level}_logger')
    logger.setLevel(level_upper)
    logger.addHandler(file_handler)

# GENERAL LOGS (ALL)
getLogger().setLevel(DEBUG)
basicConfig(filename=log_dir+'/GENERAL.log', level=DEBUG, format=log_format)
# ERROR LOGS
create_logger('error')
# INFO LOGS
create_logger('info')

'''END LOGGING CONFIG'''


class Settings(BaseSettings):
    db_engine: str = 'postgres'
    db_port: str = '5432'

    db_host: str = 'localhost'
    db_user: str = 'root'
    db_password: str = 'admin'
    db_schema: str = 'academy'

    error_logger: Logger = getLogger('error_logger')
    info_logger: Logger = getLogger('info_logger')

    class Config:
        env_file = '.env'


app_description = '''
FastAPI Template API helps you do awesome stuff. 🚀

### Courses

* You can **read courses**.
* You can **create courses**.
* You can **update courses**.
* You can **delete courses**.

### Users

You will be able to:
* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
'''

APP_CONFIG = dict(
    title='FastAPI Template',
    version='0.0.1',
    description=app_description,
    contact={
        'name': 'Juan Quintero',
        'url': 'https://www.linkedin.com/in/juanes-quintero/',
        'email': 'juanestquintero@gmail.com',
    },
    license_info={
        'name': 'Apache 2.0',
        'url': 'https://www.apache.org/licenses/LICENSE-2.0.html',
    },
    openapi_tags=[
        {
            'name': 'courses',
            'description': 'Operations with courses.',
            'externalDocs': {
                'description': 'Courses external docs',
                'url': 'https://fastapi.tiangolo.com/',
            },
        },
        {
            'name': 'users',
            'description': 'Operations with users. The **login** logic is also here.',
        },
        {
            'name': 'items',
            'description': 'Manage items. So _fancy_ they have their own docs.',
        },
    ]
)
