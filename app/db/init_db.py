import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.db.database import engine, Base
from app.models import models  # 必須：Baseにモデルを登録

def init():
    print("Creating database tables...")
    print(f"Tables registered: {list(Base.metadata.tables.keys())}")
    Base.metadata.create_all(bind=engine)
    print("Done.")

if __name__ == "__main__":
    init()