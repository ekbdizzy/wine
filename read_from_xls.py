import os
import sys
import pandas as pd
from pprint import pprint
from collections import defaultdict

import settings


def get_drinks_from_xslx(xslx_path: str) -> dict:
    if not os.path.exists(xslx_path):
        sys.exit(f'File {xslx_path} does not exists')

    drinks = pd.read_excel(
        io=xslx_path,
        usecols=["Категория", "Название", "Сорт", "Цена", "Картинка", "Акция"],
        na_values='nan',
        keep_default_na=False).to_dict(orient='records')

    drinks_by_category = defaultdict(list)
    for drink in drinks:
        drinks_by_category[drink['Категория']].append(drink)

    return drinks_by_category


if __name__ == "__main__":
    vines = get_drinks_from_xslx(settings.XLSX_FILE_PATH)
    pprint(vines, indent=4)
