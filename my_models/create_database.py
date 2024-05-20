from typing import List
import pandas as pd
from my_models.functions import del_nan, clear_dataframe
from my_models.database import create_db, Session
from my_models.kp_currency import Currency
from my_models.kp_discipline import Discipline
from my_models.kp_assoc import Kpassoc
from my_models.kp_unit import Unit
from my_models.kp_actor import Actors
from my_models.kp_goods import Goods
from my_models.kp_project import Project
from my_models.kp_winner import Winner


def create_database(load_exc_data: bool=True):
	create_db()
	if load_exc_data:
		_load_exc_data(Session())
		
def _load_exc_data(session: Session):
	# здесь алгоритм выгрузки информации из Excel таблицы и загрузка ее в созданную БД
	
	# загружаем файл Excel с лотами
	file_name = 'KP_030723_311223.xlsx'
	df = pd.read_excel(file_name)
	df = clear_dataframe(data_df=df)
	
	lot_number = del_nan(set(df['Номер_лота']))
	discipline_names = del_nan(set(df['Дисциплина']))
	project_names = del_nan(set(df['Наименование_проекта']))
	print(project_names)
	print('*' * 30)
	open_date = del_nan(set(df['Дата_открытия_лота']))
	close_date = del_nan(set(df['Дата закрытия лота']))
	actor_names = del_nan(set(df['Исполнитель_МТО']))
	good_name = del_nan(set(df['Наименование_ТМЦ']))
	good_count = del_nan(set(df['Количество_ТМЦ']))
	unit = del_nan(set(df['Ед_изм_ТМЦ']))
	provider_count = del_nan(set(df['Кол-во_поставщика']))
	provider_unit = del_nan(set(df['Ед_изм_поставщика']))
	winner_name = del_nan(set(df['Присуждено_контрагенту']))
	unit_price = del_nan(set(df['Цена']))
	total_price = del_nan(set(df['Сумма_контракта']))
	currency = del_nan(set(df['Валюты_контракта']))
	