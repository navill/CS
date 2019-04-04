import os
from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = os.path.join(os.getcwd(), 'templates')

def get_html(source_file, context={}):
    env=Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    return env.get_template(source_file).render(**context)
