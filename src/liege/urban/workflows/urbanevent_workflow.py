# -*- coding: utf-8 -*-

from liege.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    mapping = {
        'in_progress': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor', 'Contributor'),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor', 'Contributor'),
        },

        'closed': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'preparing_documents': {
            'administrative_editors': ('Reader', 'Editor',),
            'administrative_validators': ('Reader', 'Contributor'),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor', 'Contributor'),
        },
    }
