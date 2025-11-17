import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.orm import declarative_base
from optiflow.database import session  # import de la session globale

Base = declarative_base()

class BaseModel(Base):
    __abstract__ = True
    query = session.query_property()

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def save(self, commit=True):
        try:
            session.add(self)
            if commit:
                session.commit()
        except Exception:
            session.rollback()
            raise

    def delete(self, commit=True):
        try:
            session.delete(self)
            if commit:
                session.commit()
        except Exception:
            session.rollback()
            raise

    def __repr__(self):
        return f"<{self.__class__.__name__} id={self.id}>"
