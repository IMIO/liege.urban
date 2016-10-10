# -*- coding: utf-8 -*-

from liege.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """ """

    mapping = {
        'deposit': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor', 'AddressEditor'),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'analysis': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
        },

        'analysis_proposition': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Contributor',),
        },

        'college_in_progress': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'opinion_sent': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },
    }
