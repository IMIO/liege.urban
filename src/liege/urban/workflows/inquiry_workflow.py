# -*- coding: utf-8 -*-

from liege.urban.workflows.urbanevent_workflow import StateRolesMapping as LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    def get_editors(self):
        """ """
        event = self.event
        licence = self.licence
        mapping = {
            'urban_only': [
                'administrative_editors',
            ],
            'environment_only': [
                'administrative_editors_environment',
            ],
            'urban_and_environment': [
                'administrative_editors',
                'administrative_editors_environment',
            ]
        }
        allowed_group = self.get_allowed_groups(licence, event)
        if allowed_group in mapping:
            return mapping.get(allowed_group)

    def get_contributors(self):
        """ """
        event = self.event
        licence = self.licence
        mapping = {
            'urban_only': [
                'administrative_validators',
            ],
            'environment_only': [
                'administrative_validators_environment',
            ],
            'urban_and_environment': [
                'administrative_validators',
                'administrative_validators_environment',
            ]
        }
        allowed_group = self.get_allowed_groups(licence, event)
        if allowed_group in mapping:
            return mapping.get(allowed_group)

    mapping = {
        'preparing_documents': {
            get_editors: ('Editor',),
            get_contributors: ('Contributor',),
            'urban_readers': ('Reader',),
        },

        'to_validate': {
            get_contributors: ('Contributor',),
            'urban_readers': ('Reader',),
        },

        'sending_documents': {
            get_editors: ('Editor',),
            get_contributors: ('Contributor',),
            'urban_readers': ('Reader',),
        },

        'in_progress': {
            get_editors: ('Editor', 'ClaimantEditor'),
            get_contributors: ('Contributor',  'ClaimantEditor'),
            'urban_readers': ('Reader',),
        },

        'closed': {
            get_editors: ('ClaimantEditor',),
            get_contributors: ('Contributor', 'ClaimantEditor',),
            'urban_readers': ('Reader',),
        },

    }
