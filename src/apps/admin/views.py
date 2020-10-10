from flask import Blueprint, render_template, abort
from jinja2 import TemplateNotFound
from apps import admin_page


@admin_page.route('/', defaults={'page': 'index'})
@admin_page.route('/<page>')
def show(page):
    try:
        return render_template(f'{page}.html')
    except TemplateNotFound:
        abort(404)