from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app import settings


engine = create_engine(settings.Settings().DATABASE_URL)
Session = sessionmaker(
    bind=engine,
    autoflush=False)