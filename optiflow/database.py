import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

# --- Création automatique du dossier data ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # répertoire optiflow/
DATA_DIR = os.path.join(BASE_DIR, "../data")
os.makedirs(DATA_DIR, exist_ok=True)

# --- Chemin complet vers la base SQLite ---
DB_PATH = os.path.join(DATA_DIR, "base.db")

# --- Configuration SQLAlchemy ---
engine = create_engine(f"sqlite:///{DB_PATH}", echo=False)

# scoped_session permet d’utiliser query_property() dans BaseModel
session_factory = sessionmaker(bind=engine)
session = scoped_session(session_factory)

print(f"[INFO] Base SQLite configurée : {DB_PATH}")

# --- Création des tables ---
from optiflow.common.base.basemodel import Base
from optiflow.modules.client.models.client import Client

Base.metadata.create_all(engine)
print("[INFO] Tables créées dans base.db")
