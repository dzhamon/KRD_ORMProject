from sqlalchemy import Column, Integer, String

from my_models.database import Base

class Winner(Base):
	__table__ = 'kp_winner'
	id = Column(Integer, primary_key=True)
	winner_name = Column(String, nullable=False)