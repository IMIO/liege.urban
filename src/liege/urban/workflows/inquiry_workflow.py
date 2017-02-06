# -*- coding: utf-8 -*-

from liege.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    mapping = {
        'preparing_documents': {
            'administrative_editors': ('Reader', 'Editor',),
            'administrative_validators': ('Reader', 'Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'to_validate': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader', 'Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'sending_documents': {
            'administrative_editors': ('Reader', 'Editor',),
            'administrative_validators': ('Reader', 'Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'in_progress': {
            'administrative_editors': ('Reader', 'Editor',),
            'administrative_validators': ('Reader', 'Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'closed': {
            'administrative_editors': ('Reader', 'ClaimantEditor'),
            'administrative_validators': ('Reader', 'ClaimantEditor'),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

    }
