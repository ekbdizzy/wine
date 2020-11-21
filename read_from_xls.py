import pandas as pd

dataframe = pd.read_excel('xls/wine.xlsx', usecols=["Название", "Сорт", "Цена", "Картинка"])

vines = dataframe.to_dict()
print(vines)