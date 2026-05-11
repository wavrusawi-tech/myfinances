from art import text2art
import hashlib
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'user'

    def __init__(self):
        self.username = Column(String, primary_key=True)
        self.password = Column(String)

engine = create_engine("sqlite:///mydb.sqlite3", echo=True)



SessionLocal = sessionmaker(bind=engine)

Base.metadata.create_all(engine)

print(text2art("MyFinances", font='block'))