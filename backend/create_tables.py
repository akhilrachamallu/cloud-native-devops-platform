from app.core.database import Base, engine
from app.models import Task, User


def create_tables() -> None:
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")


if __name__ == "__main__":
    create_tables()