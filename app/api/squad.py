from fastapi import APIRouter
from sqlalchemy import select
from app.models.squad_players import Player
from app.db import SessionDep


router = APIRouter(
    prefix="/squad",
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def get_squad(session: SessionDep) -> list[Player]:
    squad = session.scalars(select(Player)).all()
    return squad



