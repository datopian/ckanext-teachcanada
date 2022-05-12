from ckan.views.group import  (
    read, activity, about,
    members, MembersGroupView,
    BulkProcessView, DeleteGroupView,
    EditGroupView
    )
from flask import Blueprint

resourcebank = Blueprint(u'resourcebank', __name__, url_prefix=u'/group',
                  url_defaults={u'group_type': u'group',
                                u'is_organization': False,
                                u'id': 'resource-bank'})


def register_group_plugin_rules(blueprint):
    actions = [
        u'member_delete', u'history', u'followers', u'follow',
        u'unfollow', u'admins', u'activity'
    ]

    blueprint.add_url_rule('/resourc-bank', methods=[u'GET'], view_func=read)
    blueprint.add_url_rule(
        u'/edit/<id>', view_func=EditGroupView.as_view(str(u'edit')))
    blueprint.add_url_rule(
        u'/activity/<id>/<int:offset>', methods=[u'GET'], view_func=activity)
    blueprint.add_url_rule(u'/about/<id>', methods=[u'GET'], view_func=about)
    blueprint.add_url_rule(
        u'/members/<id>', methods=[u'GET', u'POST'], view_func=members)
    blueprint.add_url_rule(
        u'/member_new/<id>',
        view_func=MembersGroupView.as_view(str(u'member_new')))
    blueprint.add_url_rule(
        u'/bulk_process/<id>',
        view_func=BulkProcessView.as_view(str(u'bulk_process')))
    blueprint.add_url_rule(
        u'/delete/<id>',
        methods=[u'GET', u'POST'],
        view_func=DeleteGroupView.as_view(str(u'delete')))

register_group_plugin_rules(resourcebank)