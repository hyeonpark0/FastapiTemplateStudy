from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotmap import DotMap
from config import Settings

settings = Settings()

db = {}
for key, value in vars(settings).items():
    _key = key.replace('db_', '')
    db[_key] = value
db = DotMap(db)

dialect = 'mysql+pymysql' if db.engine == 'mysql' else 'postgresql'

SQLALCHEMY_DATABASE_URL = f'{dialect}://{db.user}:{db.password}@{db.host}:{db.port}/{db.schema}'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
