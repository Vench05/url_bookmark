import os
from sqlalchemy.orm.session import Session

from app.process_url import ProcessUrl
from app.schema.bookmark import BookMarkRequest, BookMarkCreate, BookMarkRequestUpdate
from app.models.bookmark import BookMark


def create_bookmark(req: BookMarkRequest, db: Session):
    if get_bookmark_by_url(url=req.url, db=db):
        return False
    process_url = ProcessUrl(req.url)

    with ProcessUrl(req.url) as process_url:
        new_bookmark = BookMarkCreate(url=req.url)
        new_bookmark.title = process_url.get_title()
        new_bookmark.screenshot = process_url.get_screenshot(new_bookmark.title)
        new_bookmark.some_info = process_url.get_some_data()
    bookmark = BookMark(**new_bookmark.dict())
    db.add(bookmark)
    db.commit()
    db.refresh(bookmark)
    return bookmark


def get_all_bookmark(db: Session):
    return db.query(BookMark).all()


def get_bookmark_by_id(id: int, db: Session):
    return db.query(BookMark).get(id)


def get_bookmark_by_url(url: str, db: Session):
    return db.query(BookMark).filter(BookMark.url == url).first()


def delete_bookmark_by_id(bookmark: BookMark, db: Session):
    id = bookmark.id
    if os.path.isfile(bookmark.screenshot):
        os.remove(bookmark.screenshot)
    db.query(BookMark).filter(BookMark.id == id).delete()
    db.commit()
    return id


def update_bookmark(data: BookMarkRequestUpdate, id: int, db: Session):
    bookmark = get_bookmark_by_id(id=id, db=db)
    for key, value in data.dict().items():
        if value:
            setattr(bookmark, key, value)
    db.commit()
    return bookmark
