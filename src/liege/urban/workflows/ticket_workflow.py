# -*- coding: utf-8 -*-

from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """ """

    mapping = {
        'creation': {
            'inspection_editors': ('Editor', 'AddressEditor'),
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'prosecution_analysis': {
            'inspection_editors': ('Editor', 'AddressEditor'),
            'administrative_editors': ('Editor', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'in_progress_with_prosecutor': {
            'inspection_editors': ('Editor', 'AddressEditor'),
            'administrative_editors': ('Editor', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'in_progress_without_prosecutor': {
            'inspection_editors': ('Editor', 'AddressEditor'),
            'administrative_editors': ('Editor', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'ended': {
            'inspection_editors': ('Editor', 'AddressEditor'),
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },
    }
