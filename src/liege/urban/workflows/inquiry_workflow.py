# -*- coding: utf-8 -*-

from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    mapping = {
        'preparing_documents': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'urban_readers': ('Reader',),
        },

        'to_validate': {
            'administrative_validators': ('Contributor',),
            'urban_readers': ('Reader',),
        },

        'sending_documents': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'urban_readers': ('Reader',),
        },

        'in_progress': {
            'administrative_editors': ('Editor', 'ClaimantEditor'),
            'administrative_validators': ('Contributor',  'ClaimantEditor'),
            'urban_readers': ('Reader',),
        },

        'closed': {
            'administrative_editors': ('ClaimantEditor'),
            'administrative_validators': ('ClaimantEditor'),
            'urban_readers': ('Reader',),
        },

    }
