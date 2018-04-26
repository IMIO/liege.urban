# -*- coding: utf-8 -*-

from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    mapping = {
        'in_progress': {
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor', 'Contributor'),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'technical_validation': {
            'technical_validators': ('Editor', 'Contributor'),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'executive_validation': {
            'administrative_validators': ('Editor', 'Contributor'),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'preliminary_advice_sent': {
            'administrative_validators': ('Editor', 'Contributor'),
            'technical_validators': ('Editor', 'Contributor'),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

    }
