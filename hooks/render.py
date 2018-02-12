from jinja2 import Environment, FileSystemLoader, select_autoescape
import json
import os

dir_path = os.path.dirname(os.path.realpath(__file__))

print("running from inside {}".format(dir_path))

env = Environment(
    loader=FileSystemLoader(os.path.abspath(os.path.join(dir_path, os.pardir)))
)

template = env.get_template('template.html')

data = json.load(open('cv.json'))

print(template.render(data))