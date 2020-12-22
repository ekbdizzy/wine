from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape
from datetime import datetime

from read_from_xls import read_vines_from_xslx

env = Environment(
    loader=FileSystemLoader('.'),
    autoescape=select_autoescape(['html', 'xml'])
)

vines = [vine for vine in read_vines_from_xslx('xls/wine2.xlsx') if vine['Сорт']]
print(vines)

template = env.get_template('template.html')

year = datetime.now().year - 1920

rendered_page = template.render(
    year=year,
    vines=vines,
)

with open('index.html', 'w', encoding="utf8") as file:
    file.write(rendered_page)

server = HTTPServer(('0.0.0.0', 8000), SimpleHTTPRequestHandler)
server.serve_forever()
