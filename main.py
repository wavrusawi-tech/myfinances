from art import text2art
import hashlib
from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


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
session = SessionLocal()
print(text2art("MyFinances"))
print("Press Ctrl-C to quit any time.")

try:
    while True:
        print("\nPlease log in or create a new user")
        choice = input("[1: Login, 2: Register] ").strip()

        if choice == "1":
            login_username = input('Username: ')
            login_password = input('Password: ')
            matching_db_user = session.query(User).filter_by(username=login_username).first()

            if matching_db_user and matching_db_user.password == hash_text(login_password):
                print(f"Welcome back, {login_username}!")
            else:
                print("Invalid username or password.")

        elif choice == "2":
            register_username = input('Choose a username: ')
            existing_user = session.query(User).filter_by(username=register_username).first()

            if existing_user:
                print("That username is already taken. Please try again.")
            else:
                register_password = input('Choose a password: ')
                confirm_password = input('Confirm password: ')

                if register_password != confirm_password:
                    print("Passwords do not match.")
                else:
                    new_user = User(username=register_username, password=hash_text(register_password))
                    session.add(new_user)
                    session.commit()
                    print(f"User '{register_username}' registered successfully!")

        else:
            print("Invalid choice. Please choose 1 or 2.")

except KeyboardInterrupt:
    print("\nGoodbye!")
finally:
    session.close()

