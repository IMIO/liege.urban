# -*- coding: utf-8 -*-

from Products.urban.workflows.licence_workflow import StateRolesMapping as BaseRolesMapping


class DefaultStateRolesMapping(BaseRolesMapping):
    """ """

    mapping = {
        'in_progress': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'accepted': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'incomplete': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'refused': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'inacceptable': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'retired': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },
    }
