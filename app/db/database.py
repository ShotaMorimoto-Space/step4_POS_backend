from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()  # .envを読み込む

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "3306")
DB_NAME = os.getenv("DB_NAME")

ssl_ca_path = Path(__file__).resolve().parent / "DigiCertGlobalRootCA.crt.pem"
SSL_CA = str(ssl_ca_path)

DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# echo=True にするとSQLが表示される（デバッグ時便利）
engine = create_engine(
    DATABASE_URL,
    connect_args={"ssl": {"ca": SSL_CA}},
    echo=True,
    pool_pre_ping=True
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()