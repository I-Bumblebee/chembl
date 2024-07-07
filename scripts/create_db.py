from sqlalchemy import create_engine
from sqlalchemy_utils import create_database, database_exists

from config.settings import (
    DATABASE_HOST,
    DATABASE_NAME,
    DATABASE_PASSWORD,
    DATABASE_PORT,
    DATABASE_USERNAME,
)
from models.dwh_models import Base

DATABASE_URL = f"postgresql+psycopg2://{DATABASE_USERNAME}:{DATABASE_PASSWORD}@{DATABASE_HOST}:{DATABASE_PORT}/{DATABASE_NAME}"

engine = create_engine(DATABASE_URL)

if not database_exists(engine.url):
    create_database(engine.url)

engine = create_engine(DATABASE_URL)

Base.metadata.create_all(engine)
