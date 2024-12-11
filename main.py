from fastapi import Depends, FastAPI
from fastapi_pagination import Page, add_pagination, paginate
from sqlmodel import Session, select;
from database import init_db, engine
from models import Banner

app = FastAPI();
add_pagination(app);

init_db();

def get_session():
    with Session(engine) as session:
        yield session;

@app.get("/", response_model=list[Banner])
def getAll(session: Session = Depends(get_session)):
    data = session.exec(select(Banner)).all();
    return data;

@app.post("/", response_model=Banner)
def createBanner(banner: Banner, session: Session = Depends(get_session)):
    session.add(banner);
    session.commit();
    session.refresh(banner);
    return banner;

@app.get("/paginate")
def get_paginate(session: Session = Depends(get_session)) -> Page[Banner]:
    return paginate(session, select(Banner));