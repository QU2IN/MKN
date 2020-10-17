from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from flask import Blueprint

admin_page = Blueprint('admin_page', __name__, template_folder='templates')


@admin_page.route('/')
def home():
    return '<h1>Hello Kek</h1>'
