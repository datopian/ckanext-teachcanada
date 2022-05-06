import ckan.plugins as plugins
import ckan.plugins.toolkit as toolkit
from flask import Blueprint, render_template
from ckanext.teachcanada.blueprints import form_blueprint, participate, resourcebank
from ckanext.teachcanada.cli import get_commands


def hello_plugin():
    return u'Hello from the Datopian Theme extension'


class TeachCanadaPlugin(plugins.SingletonPlugin):
    plugins.implements(plugins.IConfigurer)
    plugins.implements(plugins.IBlueprint)
    plugins.implements(plugins.IClick)

    # IConfigurer

    def update_config(self, config_):
        toolkit.add_template_directory(config_, 'templates')
        toolkit.add_public_directory(config_, 'public')
        toolkit.add_resource('assets',
                             'teachcanada')

    # IBlueprint

    def get_blueprint(self):
        return [
            form_blueprint,
            participate,
            resourcebank
        ]

    #IClick
    def get_commands(self):
        return get_commands()