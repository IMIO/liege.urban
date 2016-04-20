# -*- coding: utf-8 -*-

from liege.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    mapping = {
        'draft': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'survey_editors': ('AddressEditor',),
        },

        'validated': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'survey_editors': ('AddressEditor',),
        },

    }
