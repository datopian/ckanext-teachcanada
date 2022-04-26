from crypt import methods
import ckan.plugins.toolkit as toolkit
from flask import Blueprint

form_blueprint = Blueprint('teachcanada', __name__, url_prefix=u"/feedback")

def form_page():
    return toolkit.render('feedback/index.html')


form_blueprint.add_url_rule(
    rule='',
    view_func=form_page,
    methods=[u'GET']
)