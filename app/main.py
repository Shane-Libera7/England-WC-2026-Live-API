from fastapi import Depends, FastAPI
from .db import get_session


app = FastAPI(title="England WC 2026 Live API",
    description="Live England World Cup 2026 match data, squad and standings",
    version="1.0.0")


