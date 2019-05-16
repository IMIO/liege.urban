# -*- coding: utf-8 -*-

from liege.urban.workflows.urbanevent_workflow import StateRolesMapping as BaseRolesMapping


class StateRolesMapping(BaseRolesMapping):
    """
    """

    mapping = {
        'writing_report': {
            'inspectors': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

        'to_validate': {
            'inspectors': ('Reader',),
            'technical_editors': ('reader',),
            'technical_validators': ('Contributor',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

        'preparing_documents': {
            'inspectors': ('Reader',),
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

        'validating_documents': {
            'inspectors': ('Reader',),
            'administrative_editors': ('reader',),
            'administrative_validators': ('Contributor',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

        'sending_documents': {
            'inspectors': ('Reader',),
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

        'closed': {
            'inspectors': ('Reader',),
            BaseRolesMapping.get_readers: ('Reader',),
        },

    }
