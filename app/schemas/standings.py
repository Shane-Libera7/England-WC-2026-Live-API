from pydantic import BaseModel, ConfigDict



class Group(BaseModel):
    id: int 
    group_name: str
    position: int
    team_name:str
    played:int
    won:int
    drawn:int
    lost:int
    goals_for:int
    goals_against:int
    goal_difference:int
    points:int
    model_config = ConfigDict(from_attributes=True)