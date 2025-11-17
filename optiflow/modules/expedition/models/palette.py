from sqlalchemy import Column, String, Integer, Date, ForeignKey
from optiflow.common.base.basemodel import BaseModel, Base
from optiflow.database import engine
from sqlalchemy.orm import relationship

class Palette(Base):
    __tablename__ = "palettes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    date_commande = Column(Date)
    client_id = Column(String(36), ForeignKey("clients.id"))
    nombre_uvc = Column(Integer)
    nombre_palette = Column(Integer)

    # Relation inverse vers Client
    client = relationship("Client", back_populates="palettes")