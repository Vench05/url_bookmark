from datetime import datetime


import datetime
from sqlalchemy import Column, String, DateTime, Integer, Text

from app.database import Base


class BookMark(Base):
    __tablename__ = 'bookmarks'

    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String, nullable=False, unique=True)
    title = Column(String)
    some_info = Column(Text)
    screenshot = Column(String)
    created_date = Column(DateTime, default=datetime.datetime.now())
