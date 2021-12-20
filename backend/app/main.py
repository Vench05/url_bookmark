from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import bookmark
from app.database import Base, engine


def create_app() -> FastAPI:
    application = FastAPI()

    # middleware
    application.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # add route
    application.include_router(bookmark.router,
                               tags=['Bookmark'],
                               prefix='/bookmarks')

    return application


app = create_app()


@app.on_event('startup')
def startup():
    Base.metadata.create_all(engine)
