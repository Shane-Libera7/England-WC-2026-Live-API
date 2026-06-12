from pydantic import BaseModel, ConfigDict

class Player(BaseModel):
    id: int
    name: str
    position: str
    model_config = ConfigDict(from_attributes=True)