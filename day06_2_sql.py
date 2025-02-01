# veritabanı oluşturma

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *  # tablolar arası ilişki kurmak için
from sqlalchemy import *

Base = declarative_base()


class Birim(Base):
    __tablename__ = "birim"

    birimId = Column(Integer, primary_key=True, autoincrement=True)
    birimAdi = Column(String(200), nullable=False, default="Birimsiz")

    def __repr__(self):
        return self.birimAdi


engine = create_engine('sqlite:///dc_btk.sqlite')
Base.metadata.create_all(engine)










