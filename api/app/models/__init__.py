import os
from dotenv import load_dotenv
from sqlmodel import create_engine, SQLModel, Session

from app.models.authors import Authors
from app.models.posts import Posts

# Load environment variables
load_dotenv()

DATABASE_URL = 'postgresql://' +  str(os.environ.get('DB_USER')) + ':' + str(os.environ.get('DB_PW')) + '@' + str(os.environ.get('DB_HOST')) + '/' + str(os.environ.get('DB_NAME'))

engine = create_engine(DATABASE_URL, echo=False if os.getenv("DEV_MODE", 'False') == 'False' else True)

session = Session(engine)