from ckanext.pages.blueprint import pages
import ckanext.pages.utils as  utils

from flask import Blueprint

about = Blueprint('about',__name__)

def show():
    return utils.pages_show('about', page_type='page')


about.add_url_rule('/about', view_func=show)
