# -*- coding: utf-8 -*-

from collections import OrderedDict

from Products.urban.interfaces import ICODT_UniqueLicence
from Products.urban.interfaces import IEnvironmentBase
from Products.urban.interfaces import IEnvironmentOnlyEvent
from Products.urban.interfaces import IUniqueLicence
from Products.urban.interfaces import IUrbanAndEnvironmentEvent
from Products.urban.interfaces import IUrbanOrEnvironmentEvent
from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    def __init__(self, context):
        self.context = context
        self.event = context
        self.licence = self.context.aq_parent

    def get_allowed_groups(self, licence, event):
        if IEnvironmentBase.providedBy(licence):
            if IUniqueLicence.providedBy(licence) or ICODT_UniqueLicence.providedBy(licence):
                if IEnvironmentOnlyEvent.providedBy(event):
                    return 'environment_only'
                elif IUrbanOrEnvironmentEvent.providedBy(event):
                    if 'urb' in licence.getFolderTendency():
                        return 'urban_only'
                    elif 'env' in licence.getFolderTendency():
                        return 'environment_only'
                elif IUrbanAndEnvironmentEvent.providedBy(event):
                    return 'urban_and_environment'
                else:
                    return 'urban_only'
            else:
                return 'environment_only'
        else:
            return 'urban_only'

    def get_editors(self):
        """ """
        event = self.event
        licence = self.licence
        mapping = {
            'urban_only': [
                'technical_editors',
                'administrative_editors',
            ],
            'environment_only': [
                'technical_editors_environment',
                'administrative_editors_environment',
            ],
            'urban_and_environment': [
                'technical_editors',
                'administrative_editors',
                'technical_editors_environment',
                'administrative_editors_environment',
            ]
        }
        allowed_group = self.get_allowed_groups(licence, event)
        if allowed_group in mapping:
            return mapping.get(allowed_group)

    mapping = {
        'in_progress': OrderedDict([
            ('urban_readers', ('Reader',)),
            ('technical_editors', ('Reader',)),
            ('administrative_editors', ('Reader',)),
            ('technical_editors_environment', ('Reader',)),
            ('administrative_editors_environment', ('Reader',)),
            (get_editors, ('Editor',)),  # !!! order matters, let editors group be overwritten
        ]),

        'closed': OrderedDict([
            ('urban_readers', ('Reader',)),
            ('technical_editors', ('Reader',)),
            ('administrative_editors', ('Reader',)),
            ('technical_editors_environment', ('Reader',)),
            ('administrative_editors_environment', ('Reader',)),
            (get_editors, ('Editor',)),  # !!! order matters, let editors group be overwritten
        ]),
    }
