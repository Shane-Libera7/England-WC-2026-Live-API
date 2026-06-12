from fastapi import APIRouter
from sqlalchemy import select
from app.models.squad_players import Player
from app.schemas.squad import Player as PlayerSchema
from app.db import SessionDep


router = APIRouter(
    prefix="/squad",
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def get_squad(session: SessionDep) -> list[PlayerSchema]:
    squad = session.scalars(select(Player)).all()
    return squad



