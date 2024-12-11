from sqlmodel import create_engine, SQLModel


# DATABASE_URL = "sqlite:///db.sqlite"
DATABASE_URL = "mysql+pymysql://an1rs09vlfub_admin_dengfuchinese:dengfuchinese%40123@137.59.105.45:3306/an1rs09vlfub_dengfuchinese"

engine = create_engine(DATABASE_URL, echo=True)

def init_db():  
    SQLModel.metadata.create_all(engine)
