from fastapi import FastAPI
from .api import fixture, squad, standing


app = FastAPI(title="England WC 2026 Live API",
    description="Live England World Cup 2026 match data, squad and standings",
    version="1.0.0")


app.include_router(fixture.router)
app.include_router(squad.router)
app.include_router(standing.router)

