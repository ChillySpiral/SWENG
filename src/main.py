import os

from dotenv import load_dotenv
from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.schema import CreateSchema
from entity.entities import Base


def main():
    load_dotenv()
    database_url_object = URL.create(
        "postgresql",
        username=os.getenv("DB_USERNAME"),
        password=os.getenv("DB_PASSWORD"),
        host="localhost",
        port=5432,
        database=os.getenv("DB_NAME"),
    )
    engine = create_engine(database_url_object, echo=True)
    Base.metadata.create_all(engine)  # Create all tables
    print(Base.metadata.tables)

if __name__ == '__main__':
    main()
