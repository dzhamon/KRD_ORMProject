from sqlalchemy import Column, Integer, String

from my_models.database import Base


class Project(Base):
	__tablename__ = 'kp_project'
	id = Column(Integer, Primary_key=True)
	project_name = Column(String)
	
	def __repr__(self):
		info: str = f'Наименование проекта: {self.actor_name}'
		return info