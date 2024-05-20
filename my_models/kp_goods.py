from sqlalchemy import Column, Integer, String, ForeignKey, Numeric

from my_models.database import Base

class Goods(Base):
	__tablename__= 'kp_goods'
	id = Column(Integer, primary_key=True)
	good_name = Column(String)
	
	def __repr__(self, good_name=None):
		info: str = f'Наименование товара [{good_name}]'
		return info
	