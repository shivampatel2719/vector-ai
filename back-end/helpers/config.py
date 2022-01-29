import os
from dotenv import load_dotenv

from pathlib import Path
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_NAME:str = "Card Board"
    PROJECT_VERSION: str = "1.0.0"

    POSTGRES_USER : str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER : str = os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT : str = os.getenv("POSTGRES_PORT",5432) # default postgres port is 5432
    POSTGRES_DB : str = os.getenv("POSTGRES_DB","tdd")
    DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    # DATABASE_URL = str('postgresql://juqtjymdmoblia:846ff6f3067cccbc2cd05038a74c5684d57c96341003ed87e38251033b6671c3@postgres://juqtjymdmoblia:846ff6f3067cccbc2cd05038a74c5684d57c96341003ed87e38251033b6671c3@ec2-3-213-76-170.compute-1.amazonaws.com:5432/d53nkbkhm296ol:5432/d53nkbkhm296ol')
settings = Settings()