from sqlalchemy import String
from typing import Optional
from sqlalchemy import DateTime
from datetime import datetime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.db import Base


class Fixture(Base):
    __tablename__="fixtures"

    id: Mapped[int] = mapped_column(primary_key=True)
    kickoff_utc: Mapped[datetime]
    status: Mapped[str] = mapped_column(String(45))
    stage: Mapped[str] = mapped_column(String(45))
    group_name: Mapped[Optional[str]] = mapped_column(String(45))
    home_team: Mapped[Optional[str]] = mapped_column(String(45))
    away_team: Mapped[Optional[str]] = mapped_column(String(45))
    home_score: Mapped[Optional[int]]
    away_score: Mapped[Optional[int]]
   

