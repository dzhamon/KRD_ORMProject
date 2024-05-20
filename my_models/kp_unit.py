from sqlalchemy import Column, Integer, String, ForeignKey

from my_models.database import Base

class Unit(Base):
	__table__ = 'kp_unit'
	id = Column(Integer, primary_key=True)
	good_unit = Column(String)
	name_u = Column(String)
	
