from sqlalchemy import Column, Integer, String

from my_models.database import Base


class Discipline(Base):
	__tablename__ = 'kp_discipline'
	id = Column(Integer, primary_key=True)
	discipline_names = Column(String)
	
	def __repr__(self):
		info: str = f'Дисциплина: {self.discipline_names}'
		return info