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


@teachcanada.command()
def addresourcebank():
    metadata = meta.metadata
    group = metadata.tables['group']
    query = group.insert().values(
        title="Resource Bank", name="resource-bank",
        type='group',
    )
    connection = model.Session.connection()
    connection.execute(query)
    model.Session.commit()
    click.secho(u"Add Resource Bank to Group", fg=u"green")



@teachcanada.command()
def addabout():
    metadata = meta.metadata
    ckanext_pages = metadata.tables['ckanext_pages']
    query = ckanext_pages.insert().values(
        title="About", name="about",
        private=False
    )
    connection = model.Session.connection()
    connection.execute(query)
    model.Session.commit()
    click.secho(u"About added to ckanext_pages Table", fg=u"green")



