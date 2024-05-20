from sqlalchemy import Column, Integer, String

from my_models.database import Base


class Currency(Base):
	__tablename__ = 'kp_currency'
	id = Column(Integer, primary_key=True)
	currency = Column(String)
	
	def __repr__(self):
		info: str = f'[Валюта контракта: {self.currency}]'
		return info