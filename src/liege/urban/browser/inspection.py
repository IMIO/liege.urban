# -*- coding: utf-8 -*-

from plone import api


class IsInspector(object):
    """
    Return is a user is in the inspection groups
    """

    def __init__(self, context, request):
        self.context = context
        self.request = request

    def __call__(self):
        """
        """
        current_user = api.user.get_current()
        is_admin = api.user.get_permissions(user=current_user, obj=self.context)['Manage portal']
        if is_admin:
            return True
        user_groups = self.get_groups_ids(current_user)
        if 'inspection_editors' in user_groups or 'inspection_validators' in user_groups:
            return True
        return False
