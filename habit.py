from sqlalchemy import Boolean, Column, Integer, String
from db import Base


class Habit(Base):
    __tablename__ = "habits"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
