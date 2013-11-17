from sqlalchemy import create_engine
engine = create_engine('sqlite:///:memory:', echo = True)


from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)