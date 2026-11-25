from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql+psycopg2://students_management_qxqv_user:F7W3VMJxQ8b9pcLFn3LHyoDtn0QxmMGb@dpg-dc35cre7bikc73c54vt0-a.oregon-postgres.render.com/students_management_qxqv"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()


# def get_connection():
#     db = session_local()
#     try:
#         yield db
#     finally:
#         db.close