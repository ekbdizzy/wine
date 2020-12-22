import pandas as pd
from pprint import pprint


def read_vines_from_xslx(xslx_path: str) -> dict:
    dataframe = pd.read_excel(io=xslx_path,
                              usecols=["Категория", "Название", "Сорт", "Цена", "Картинка"],
                              na_values='nan',
                              keep_default_na=False
                              )

    drinks = dataframe.to_dict(orient='records')
    drink_categories = {drink['Категория']: [] for drink in drinks}

    for drink in drinks:
        drink_categories[drink['Категория']].append(
            {
                "Картинка": drink["Картинка"],
                "Категория": drink["Категория"],
                "Название": drink["Название"],
                "Сорт": drink["Сорт"],
                "Цена": drink["Цена"],
            })

    return drink_categories


if __name__ == "__main__":
    vines = read_vines_from_xslx('xls/wine2.xlsx')
    pprint(vines)

    split = {'index': [0, 1, 2, 3, 4, 5],
             'columns': ['Название', 'Сорт', 'Цена', 'Картинка'],
             'data': [['Изабелла', 'Изабелла', 350, 'izabella.png'],
                      ['Гранатовый браслет', 'Мускат розовый', 350, 'granatovyi_braslet.png'],
                      ['Шардоне', 'Шардоне', 350, 'shardone.png'],
                      ['Белая леди', 'Дамский пальчик', 399, 'belaya_ledi.png'],
                      ['Ркацители', 'Ркацители', 499, 'rkaciteli.png'],
                      ['Хванчкара', 'Александраули', 550, 'hvanchkara.png']]}

    dict = {
        'Название': {
            0: 'Изабелла', 1: 'Гранатовый браслет', 2: 'Шардоне', 3: 'Белая леди', 4: 'Ркацители', 5: 'Хванчкара'},
        'Сорт': {
            0: 'Изабелла', 1: 'Мускат розовый', 2: 'Шардоне', 3: 'Дамский пальчик', 4: 'Ркацители',
            5: 'Александраули'}, 'Цена': {
            0: 350, 1: 350, 2: 350, 3: 399, 4: 499, 5: 550},
        'Картинка': {
            0: 'izabella.png', 1: 'granatovyi_braslet.png', 2: 'shardone.png', 3: 'belaya_ledi.png',
            4: 'rkaciteli.png', 5: 'hvanchkara.png'}}

    records = [{'Название': 'Изабелла', 'Сорт': 'Изабелла', 'Цена': 350, 'Картинка': 'izabella.png'},
               {'Название': 'Гранатовый браслет', 'Сорт': 'Мускат розовый', 'Цена': 350,
                'Картинка': 'granatovyi_braslet.png'},
               {'Название': 'Шардоне', 'Сорт': 'Шардоне', 'Цена': 350, 'Картинка': 'shardone.png'},
               {'Название': 'Белая леди', 'Сорт': 'Дамский пальчик', 'Цена': 399, 'Картинка': 'belaya_ledi.png'},
               {'Название': 'Ркацители', 'Сорт': 'Ркацители', 'Цена': 499, 'Картинка': 'rkaciteli.png'},
               {'Название': 'Хванчкара', 'Сорт': 'Александраули', 'Цена': 550, 'Картинка': 'hvanchkara.png'}]
