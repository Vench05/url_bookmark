from typing import List
from fastapi import APIRouter, Depends, HTTPException
from fastapi.exceptions import HTTPException
from sqlalchemy.orm.session import Session

from app.database import get_db
from app.schema.bookmark import BookMarkRequest, BookMarkResponse, BookMarkRequestUpdate
from app.crud.bookmark import \
    create_bookmark, \
    get_all_bookmark, \
    get_bookmark_by_id, \
    delete_bookmark_by_id, \
    update_bookmark

router = APIRouter()


@router.post('/', response_model=BookMarkResponse, status_code=201)
def post_bookmark(req: BookMarkRequest, db: Session = Depends(get_db)):
    new_bookmark = create_bookmark(req=req, db=db)
    if not new_bookmark:
        raise HTTPException(
            detail='URL already exist',
            status_code=409
        )
    return new_bookmark


@router.get('/', response_model=List[BookMarkResponse])
def get_bookmark_all(db: Session = Depends(get_db)):
    return get_all_bookmark(db=db)


@router.get('/{id}', response_model=BookMarkResponse)
def get_bookmark(id: int, db: Session = Depends(get_db)):
    bookmark = get_bookmark_by_id(id=id, db=db)
    if not bookmark:
        raise HTTPException(detail=f'bookmark ID:{id} not found',
                            status_code=404)
    return bookmark


@router.delete('/{id}/delete' )
def delete_bookmark(id: int, db: Session = Depends(get_db)):
    bookmark = get_bookmark_by_id(id=id, db=db)
    if not bookmark:
        raise HTTPException(detail=f'bookmark ID:{id} not found',
                            status_code=404)
    return delete_bookmark_by_id(bookmark=bookmark, db=db)


@router.put('/{id}/update', response_model=BookMarkResponse)
def put_bookmark(data: BookMarkRequestUpdate, id: int, db: Session = Depends(get_db)):
    bookmark = get_bookmark_by_id(id=id, db=db)
    if not bookmark:
        raise HTTPException(detail=f'bookmark ID:{id} not found',
                            status_code=404)
    return update_bookmark(data=data, id=id, db=db)
