from fastapi import Depends, FastAPI
from fastapi_pagination import add_pagination
from config.database import init_db
from models import Banner
from routes.banner_routes import router_banner

app = FastAPI();
add_pagination(app);

init_db();

app.include_router(prefix="/api", router=router_banner);