from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime

from read_from_xls import get_drinks_from_xslx

FOUNDATION_YEAR = 1920
TEMPLATE_NAME = 'template.html'
XLSX_FILE_PATH = 'xls/wine3.xlsx'

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template(TEMPLATE_NAME)

sorted_by_category_drinks = get_drinks_from_xslx(XLSX_FILE_PATH)
company_age = datetime.now().year - FOUNDATION_YEAR

rendered_page = template.render(
    age=company_age,
    drinks=sorted_by_category_drinks,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
