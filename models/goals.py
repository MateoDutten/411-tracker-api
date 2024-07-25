from sqlalchemy import String
from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from models.base import Base

class Goals(Base):
    __tablename__ = "goals"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    timeframe: Mapped[str] = mapped_column(String(255))
    start_date: Mapped[DateTime] = mapped_column(DateTime())