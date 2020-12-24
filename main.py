from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime

from read_from_xls import get_drinks_from_xslx

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

template = env.get_template('template.html')

drinks_by_category = get_drinks_from_xslx('xls/wine3.xlsx')
year = datetime.now().year - 1920

rendered_page = template.render(
    year=year,
    drinks=drinks_by_category,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
