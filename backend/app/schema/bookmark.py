from typing import Optional
from pydantic import BaseModel
from pydantic.networks import AnyHttpUrl


class BookMarkRequest(BaseModel):
    url: AnyHttpUrl


class BookMarkCreate(BookMarkRequest):
    title: Optional[str] = None
    some_info: Optional[str] = None
    screenshot: Optional[str] = None

    class Config:
        orm_mode = True


class BookMarkResponse(BookMarkCreate):
    id: int


class BookMarkRequestUpdate(BaseModel):
    title: Optional[str] = None
    some_info: Optional[str] = None

    class Config:
        orm_mode = True
