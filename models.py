from sqlmodel import SQLModel, Field

class Banner(SQLModel, table=True):
    id: int = Field(primary_key=True)
    title: str
    image: str
    link: str
    priority: int