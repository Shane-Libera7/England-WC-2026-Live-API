from pydantic import BaseModel, ConfigDict
from typing import Optional 
from datetime import datetime

class Fixture(BaseModel):
    id: int
    kickoff_utc: datetime
    status: str
    stage: str
    group_name: Optional[str] = None
    home_team: Optional[str] = None
    away_team: Optional[str] = None
    home_score: Optional[int] = None
    away_score: Optional[int] = None
    model_config = ConfigDict(from_attributes=True)