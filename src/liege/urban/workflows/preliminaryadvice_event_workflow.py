# -*- coding: utf-8 -*-

from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    mapping = {
        'in_progress': {
            'administrative_editors': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor', 'Contributor'),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'technical_validation': {
            'administrative_editors': ('Editor',),
            'technical_validators': ('Editor', 'Contributor'),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'executive_validation': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor', 'Contributor'),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'preliminary_advice_sent': {
            'administrative_validators': ('Editor', 'Contributor'),
            'technical_validators': ('Editor', 'Contributor'),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

    }
