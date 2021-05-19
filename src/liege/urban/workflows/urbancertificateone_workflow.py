# -*- coding: utf-8 -*-

from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """ """

    mapping = {
        'deposit': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor', 'AddressEditor'),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'analysis': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'urban_readers': ('Reader',),
        },

        'college': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'done': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'urban_readers': ('Reader',),
        },
    }
