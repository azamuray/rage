from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db_name = "base.db"
db_path = f"sqlite:///db/{db_name}"
debug_mode = False

engine = create_engine(db_path, echo=debug_mode)
Base = declarative_base()
Session = sessionmaker(bind=engine)
