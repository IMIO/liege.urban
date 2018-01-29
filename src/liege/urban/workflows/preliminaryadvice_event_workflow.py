# -*- coding: utf-8 -*-

from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    mapping = {
        'in_progress': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Reader',),
            'technical_editors_environment': ('Reader',),
            'technical_validators_environment': ('Reader',),
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor', 'Contributor'),
            'urban_readers': ('Reader',),
        },

        'technical_validation': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Reader',),
            'technical_editors_environment': ('Reader',),
            'technical_validators_environment': ('Reader',),
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Editor', 'Contributor'),
            'urban_readers': ('Reader',),
        },

        'executive_validation': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Reader',),
            'technical_editors_environment': ('Reader',),
            'technical_validators_environment': ('Reader',),
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Editor', 'Contributor'),
            'urban_readers': ('Reader',),
        },

        'preliminary_advice_sent': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Reader',),
            'technical_editors_environment': ('Reader',),
            'technical_validators_environment': ('Reader',),
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Editor', 'Contributor'),
            'urban_readers': ('Reader',),
        },

    }
