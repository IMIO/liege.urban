# -*- coding: utf-8 -*-

from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """ """

    mapping = {
        'deposit': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor', 'AddressEditor'),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'analysis': {
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'analysis_validation': {
            'technical_validators': ('Contributor',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'college': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'favorable': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'defavorable': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'abandoned': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },
    }
