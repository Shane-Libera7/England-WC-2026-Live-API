from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from app.models.fixture import Fixture
from app.schemas.fixtures import Fixture as FixtureSchema
from datetime import datetime, timezone
from app.db import SessionDep

router = APIRouter(
    prefix="/fixtures",
    responses={404: {"description": "Not found"}}
)


@router.get("/")
async def read_fixtures(session: SessionDep, status: str | None = None) -> list[FixtureSchema]:
    if status:
        fixtures = session.scalars(select(Fixture).where(Fixture.status == status)).all()
       
    else:
        fixtures = session.scalars(select(Fixture)).all()
    
    return fixtures 

@router.get("/next")
async def next_fixture(session: SessionDep) -> FixtureSchema:
    today = datetime.now(timezone.utc)
    fixture = session.scalars(select(Fixture).where(Fixture.kickoff_utc > today).order_by(Fixture.kickoff_utc)).first()
    if fixture is None:
        raise HTTPException(status_code=404, detail="No Upcoming fixtures found")
    return fixture



@router.get("/form")
async def get_form(session: SessionDep, limit = 5) -> list[FixtureSchema]:
    form = session.scalars(select(Fixture).where(Fixture.status == "FINISHED").order_by(Fixture.kickoff_utc.desc()).limit(limit)).all()
    if not form:
        raise HTTPException(status_code=404, detail="Last 5 Games Not Found")
    return form



@router.get("/{fixture_id}")
async def get_fixture(fixture_id: int, session: SessionDep) -> FixtureSchema:
    fixture = session.scalars(select(Fixture).where(Fixture.id == fixture_id)).first()
    if fixture is None:
        raise HTTPException(status_code=404, detail="Fixture Not Found")
    return fixture





