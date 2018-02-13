# -*- coding: utf-8 -*-

from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    mapping = {
        'draft': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor', 'Contributor'),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'to_validate': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Editor', 'Contributor'),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'to_send': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor', 'Contributor'),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'closed': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Editor', 'Contributor'),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
        },

    }
