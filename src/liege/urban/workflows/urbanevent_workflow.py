# -*- coding: utf-8 -*-

from collections import OrderedDict
from Products.urban.workflows.urbanevent_workflow import StateRolesMapping as BaseRolesMapping


class StateRolesMapping(BaseRolesMapping):
    """
    """

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
            (BaseRolesMapping.get_readers, ('Reader',)),
            (get_editors, ('Editor',)),  # !!! order matters, let editors group be overwritten
        ]),

        'closed': OrderedDict([
            (BaseRolesMapping.get_readers, ('Reader',)),
            (get_editors, ('Editor',)),  # !!! order matters, let editors group be overwritten
        ]),
    }
