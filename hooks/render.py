#!/usr/bin/env python3

import json
import os
from jinja2 import Environment, FileSystemLoader

dir_path = os.path.dirname(os.path.realpath(__file__))

env = Environment(
    loader=FileSystemLoader(os.path.abspath(os.path.join(dir_path, os.pardir)))
)

template = env.get_template('template.html')

data = json.load(open('cv.json'))

print(template.render(data))