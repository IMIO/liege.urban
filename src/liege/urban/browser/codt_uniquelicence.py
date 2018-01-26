# -*- coding: utf-8 -*-

from plone import api


class IsLeaderUser(object):
    """
    Return is a user is in the group of the 'folder_tendency' field
    of the unique licence
    """

    def __init__(self, context, request):
        self.licence = context
        self.request = request

    def __call__(self):
        """
        """
        tendency_mapping = {
            'env': set([
                'administrative_editors_environment',
                'administrative_validators_environment',
                'technical_editors_environment',
                'technical_validators_environment',
            ]),
            'urb': set([
                'administrative_editors',
                'administrative_validators',
                'technical_editors',
                'technical_validators',
            ]),
            '': set([])
        }
        tendency_groups = tendency_mapping.get(self.licence.getFolderTendency(), set([]))
        current_user = api.user.get_current()
        user_groups = set([g.id for g in api.group.get_groups(user=current_user)])
        is_leader = bool(tendency_groups.intersection(user_groups))
        is_admin = api.user.get_permissions(user=current_user, obj=self.licence)['Manage portal']
        return is_leader or is_admin
