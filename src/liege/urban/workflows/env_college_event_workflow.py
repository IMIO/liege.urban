# -*- coding: utf-8 -*-

from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    mapping = {
        'draft': {
            'administrative_editors_environment': ('Reader', 'Editor',),
            'administrative_validators_environment': ('Contributor',),
            'urban_readers': ('Reader',),
        },

        'to_validate': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Contributor',),
            'urban_readers': ('Reader',),
        },

        'decision_in_progress': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Contributor',),
            'urban_readers': ('Reader',),
        },

        'closed': {
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'urban_readers': ('Reader',),
        },

    }
