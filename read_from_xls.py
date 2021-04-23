import os
import sys
import pandas as pd
from pprint import pprint
from collections import defaultdict

import settings


def get_sorted_dict(dict):
    """Return dict sorted by keys."""
    return {key: value for key, value in sorted(dict.items())}


def get_drinks_from_xslx(xslx_path: str) -> dict:
    if not os.path.exists(xslx_path):
        sys.exit(f'File {xslx_path} does not exists')

    drinks = pd.read_excel(
        io=xslx_path,
        usecols=["Категория", "Название", "Сорт", "Цена", "Картинка", "Акция"],
        na_values='nan',
        keep_default_na=False)
    drinks_dict = drinks.to_dict(orient='records')

    sorted_by_category_drinks = defaultdict(list)

    for drink in drinks_dict:
        sorted_by_category_drinks[drink['Категория']].append(
            {key: drink[key] for key in drink.keys()})

    return get_sorted_dict(sorted_by_category_drinks)


if __name__ == "__main__":
    vines = get_drinks_from_xslx(settings.XLSX_FILE_PATH)
    pprint(vines, indent=4)
