# -*- coding: utf-8 -*-

from liege.urban.workflows.adapter import LocalRoleAdapter

from plone import api


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    def get_parcel_roles(self):
        licence = self.context.aq_parent
        if api.content.get_state(licence) == 'deposit':
            return ('Editor', 'Reader')
        return ('Reader',)

    mapping = {
        'draft': {
            'administrative_editors': (get_parcel_roles,),
            'administrative_validators': (get_parcel_roles,),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
            'survey_editors': ('AddressEditor',),
        },

        'validated': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
            'survey_editors': ('AddressEditor',),
        },

    }
