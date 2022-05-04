from ckanext.pages.blueprint import pages
import ckanext.pages.utils as  utils

from flask import Blueprint

participate = Blueprint('participate',__name__)

def show():
    return utils.pages_show('ways-to-participate', page_type='page')


participate.add_url_rule('/ways-to-participate', view_func=show)
