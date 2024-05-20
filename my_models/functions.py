import pandas as pd

def del_nan(list_name):
	L1 = [item for item in list_name if not (pd.isnull(item)) == True]
	L1, list_name = list_name, L1
	return list_name

def clear_dataframe(data_df):
	# Заменяем пробелы в названиях столбцов на знаки "_" и избавляемся от (.)
	data_df = data_df.rename(columns=lambda x: x.replace(' ', '_'))
	data_df = data_df.rename(columns=lambda x: x.replace('.', '_'))
	# переименуем столбец Исполнитель_МТО_(Ф_И_О) на Исполнитель_МТО
	data_df = data_df.rename(columns={'Исполнитель_МТО_(Ф_И_О_)': 'Исполнитель_МТО'})
	data_df[['Номер_лота']] = data_df[['Номер_лота']].astype(object)
	return data_df