# -*- coding: utf-8 -*-

from liege.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    mapping = {
        'draft': {
            'administrative_editors': ('Reader', 'Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'to_validate': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'decision_in_progress': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'closed': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

    }
