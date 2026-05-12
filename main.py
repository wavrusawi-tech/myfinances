from art import text2art
import hashlib
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///mydb.sqlite3", echo=False)


class User(Base):
    __tablename__ = 'user'

    username = Column(String, primary_key=True)
    password = Column(String)


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

print(text2art("MyFinances", font='block'))
