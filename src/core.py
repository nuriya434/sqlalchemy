from models import metadata
from database import engine
def create_tables():
    metadata.create_all(engine)
