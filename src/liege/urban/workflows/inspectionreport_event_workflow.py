# -*- coding: utf-8 -*-

from liege.urban.workflows.urbanevent_workflow import StateRolesMapping as BaseRolesMapping


class StateRolesMapping(BaseRolesMapping):
    """
    """

    mapping = {
        'writing_report': {
            'inspection_editors': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

        'to_validate': {
            'inspection_editors': ('Reader',),
            'technical_editors': ('reader',),
            'technical_validators': ('Contributor',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

        'preparing_documents': {
            'inspection_editors': ('Reader',),
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

        'validating_documents': {
            'inspection_editors': ('Reader',),
            'administrative_editors': ('reader',),
            'administrative_validators': ('Contributor',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

        'sending_documents': {
            'inspection_editors': ('Reader',),
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

        'closed': {
            'inspection_editors': ('Reader',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

    }
