import os
from dotenv import load_dotenv

load_dotenv()

SIMULATOR_URL = os.getenv(
    "SIMULATOR_URL",
    "http://localhost:8000"
)
