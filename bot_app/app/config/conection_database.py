from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('postgresql://root:example@localhost/dbcompass')

Session = sessionmaker(bind=engine)
session = Session()