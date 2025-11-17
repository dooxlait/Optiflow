from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from optiflow.common.base.basemodel import BaseModel, Base
from optiflow.database import engine
from optiflow.modules.expedition.models.palette import Palette

class Client(BaseModel):
    __tablename__ = "clients"

    nom = Column(String(120), nullable=False)
    code_postal = Column(String(10))
    ville = Column(String(100))
    compte = Column(String(20))

    # Relation avec Palette
    palettes = relationship("Palette", back_populates="client", cascade="all, delete-orphan")
    