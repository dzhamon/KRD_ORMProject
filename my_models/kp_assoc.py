from sqlalchemy import Column, Integer, String, ForeignKey, Numeric, Table
from sqlalchemy.orm import relationship
from my_models.database import Base

association_table = Table(
	"kp_lots", Base.metadata,
	Column('id', Integer, primary_key=True),
	Column('lot_number', Integer),
	Column('id_discipline', ForeignKey('kp_discipline.id'), nullable=False),
	Column('id_project', ForeignKey('kp_project.id'), nullable=False),
	Column('open_date', String),
	Column('close_date', String),
	Column('id_actor', Integer, ForeignKey('kp_actors.id'))
)


class Kpassoc(Base):
	__tablename_ = 'kpassociation'
	lot_number = Column(Integer)
	id_good_name = Column(ForeignKey('kp_goods.id'), nullable=False)
	good_count = Column(Numeric, nullable=False)
	id_unit = Column(ForeignKey('kp_unit.id'), nullable=False)
	provider_count = Column(Numeric)
	id_provider_unit = Column(ForeignKey('kp_unit.id'), nullable=False)
	id_winner = Column(ForeignKey('kp_winner.id'), nullable=False)
	unit_price = Column(Numeric, nullable=False)
	total_price = Column(Numeric, nullable=False)
	id_currency = Column(ForeignKey('kp_currency.id'), nullable=False)
	lots = relationship('Actors', secondary=association_table, backref='lots_actors')
	
	