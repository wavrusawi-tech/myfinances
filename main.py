from art import text2art
import hashlib
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, session


def hash_text(text: str) -> str:
    return hashlib.sha256(text.encode()).hexdigest()


class Base(DeclarativeBase):
    pass


engine = create_engine("sqlite:///mydb.sqlite3", echo=True)


class User(Base):
    __tablename__ = 'user'

    username = Column(String, primary_key=True)
    password = Column(String)


Base.metadata.create_all(engine)

SessionLocal = sessionmaker(bind=engine)

print(text2art("MyFinances", font='block'))
print("Please log in or create a new user")
choice = int(input("[1: Login, 2: Register]"))
if choice == 1:
    all_users = session.query(User).all()
    login_username = input('Username:')
    login_password = input('Password:')
    login_hashed_password = hash_text(login_password)
    matching_db_user = session.query(User).filter_by(username=login_username1).first()

