from sqlalchemy import create_engine
from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy.orm import DeclarativeBase, Session
from typing import Annotated
import os

load_dotenv()


class Base(DeclarativeBase):
    pass



database_url = os.getenv("DATABASE_URL")
engine = create_engine(f"{database_url}", echo=True)




def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]