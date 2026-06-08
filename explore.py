import httpx
import json
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "https://api.football-data.org/v4"
HEADERS = {"X-Auth-Token": API_KEY,
           "X-Unfold-Goals": "true",
            "X-Unfold-Bookings": "true",
            "X-Unfold-Lineups": "true"
           }

def explore(endpoint):
    r = httpx.get(f"{BASE_URL}{endpoint}", headers=HEADERS)
    print(json.dumps(r.json(), indent=2))



# Get a finished England match from Euro 2024
explore("/competitions/WC/standings")
