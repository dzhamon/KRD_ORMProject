from sqlalchemy import  Column, Integer, String

from my_models.database import Base

class Actors(Base):
	__tablename__= 'kp_actors'
	id = Column(Integer, Primary_key=True)
	actor_name = Column(String)
	
	def __repr__(self):
		info: str = f'Исполнитель [ФИО: {self.actor_name}]'
		return info
	