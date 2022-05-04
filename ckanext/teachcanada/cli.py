import click
from ckan.model import meta
from sqlalchemy import Table
import ckan.model as model


def get_commands():
    return [teachcanada]


@click.group()
def teachcanada():
    pass

@teachcanada.command()
def addwaystoparticipate():
    metadata = meta.metadata
    ckanext_pages = metadata.tables['ckanext_pages']
    query = ckanext_pages.insert().values(
        title="Ways to Participate", name="ways-to-participate",
        private=False
    )
    connection = model.Session.connection()
    connection.execute(query)
    model.Session.commit()
    click.secho(u"Way to Participate added to ckanext_pages Table", fg=u"green")






