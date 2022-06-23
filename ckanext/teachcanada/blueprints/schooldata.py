from crypt import methods
import ckan.plugins.toolkit as toolkit
from flask import Blueprint

school_blueprint = Blueprint('schooldata', __name__, url_prefix=u"/schooldata")

def page():
    return toolkit.render('schooldata/index.html')


school_blueprint.add_url_rule(
    rule='',
    view_func=page,
    methods=[u'GET']
)