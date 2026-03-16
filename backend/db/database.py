import os
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from dotenv import load_dotenv


# Loading ENV
load_dotenv()


DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username="root",
    password=os.getenv('MYSQL_ROOT_PASSWORD', ''),
    host="db",
    port=3306,
    database=os.getenv('MYSQL_DATABASE', 'tododb'))


try:
    engine = create_engine(DATABASE_URL)

except SQLAlchemyError as e:
    print("Database connection failed:", e)
    exit(1)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
