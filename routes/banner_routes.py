from fastapi import APIRouter, Depends
from fastapi_pagination import Page, paginate
from sqlmodel import Session, select

from config.session import get_session
from models import Banner

router_banner = APIRouter(
    prefix="/banners",
    );

@router_banner.get("/", response_model=list[Banner])
def getAll(session: Session = Depends(get_session)):
    data = session.exec(select(Banner)).all();
    return data;

@router_banner.post("/", response_model=Banner)
def createBanner(banner: Banner, session: Session = Depends(get_session)):
    session.add(banner);
    session.commit();
    session.refresh(banner);
    return banner;

@router_banner.get("/paginate")
def get_paginate(session: Session = Depends(get_session)) -> Page[Banner]:
    return paginate(session, select(Banner));