from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime
import argparse
import settings

from read_from_xls import get_drinks_from_xslx


def main():
    env = Environment(loader=FileSystemLoader('.'),
                      autoescape=select_autoescape(['html', 'xml']))

    parser = argparse.ArgumentParser()
    parser.add_argument('-f', '--file',
                        help="path to xls file with drinks",
                        action='store',
                        default=settings.XLSX_FILE_PATH)
    args = parser.parse_args()

    template = env.get_template(settings.TEMPLATE_NAME)
    sorted_by_category_drinks = get_drinks_from_xslx(args.file)
    company_age = datetime.now().year - settings.FOUNDATION_YEAR
    rendered_page = template.render(age=company_age, drinks=sorted_by_category_drinks.items())

    with open('index.html', 'w', encoding="utf8") as file:
        file.write(rendered_page)

    server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
    server.serve_forever()


if __name__ == '__main__':
    main()
