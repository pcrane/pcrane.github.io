#!/usr/bin/env python3

import json
import os
import sys
from jinja2 import Environment, FileSystemLoader

dir_path = os.path.dirname(os.path.realpath(__file__))

env = Environment(
    loader=FileSystemLoader(os.path.abspath(os.path.join(dir_path, os.pardir)))
)


with open('cv.json', 'r', encoding="utf-8") as cv:
    data = json.load(cv)

    stdout = sys.stdout
    with open('index.html', 'w', encoding="utf-8") as f:
        sys.stdout = f
        template = env.get_template('template.html')
        content = template.render(data)
        print(content)

    with open('README.md', 'w', encoding="utf-8") as f:
        sys.stdout = f
        template = env.get_template('template.md')
        content = template.render(data)
        print(content)

    sys.stdout = stdout