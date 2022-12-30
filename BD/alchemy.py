from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker, declarative_base


# если файл alchemy.py будет не в одной папке с базой, откорректировать путь ниже !
# engine = create_engine("sqlite:////BD/db_currency.db")
engine = create_engine("sqlite:///BD/db_currency.db")

db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))

Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    from BD import Model_db
    Base.metadata.create_all(bind=engine)