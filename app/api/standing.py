from fastapi import APIRouter
from sqlalchemy import select
from app.models.group_standing import Group

from app.db import SessionDep


router = APIRouter(
    prefix="/standing",
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def get_standing(session: SessionDep) -> list[Group]:
    standing = session.scalars(select(Group)).all()
    return standing
