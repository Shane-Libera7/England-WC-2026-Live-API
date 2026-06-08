from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import DeclarativeBase, Session
import os

load_dotenv()


class Base(DeclarativeBase):
    pass



database_url = os.getenv("DATABASE_URL")
engine = create_engine(f"{database_url}", echo=True)




def get_session():
    with Session(engine) as session:
        yield session
