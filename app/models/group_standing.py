from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from app.db import Base




class Group(Base):
    __tablename__ = "group_standing"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    group_name: Mapped[str] = mapped_column(String(45))
    position: Mapped[int]
    team_id: Mapped[int]
    team_name:Mapped[str] = mapped_column(String(45))
    played:Mapped[int]
    won:Mapped[int]
    drawn:Mapped[int]
    lost:Mapped[int]
    goals_for:Mapped[int]
    goals_against:Mapped[int]
    goal_difference:Mapped[int]
    points:Mapped[int]
