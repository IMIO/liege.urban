# -*- coding: utf-8 -*-

from Products.urban.workflows.licence_workflow import StateRolesMapping as BaseRolesMapping


class DefaultStateRolesMapping(BaseRolesMapping):
    """ """

    def get_editors(self):
        """ """
        licence = self.licence
        mapping = {
            'urban_only': [
                'urban_editors',
            ],
            'environment_only': [
                'administrative_editors_environment',
                'administrative_validators_environment',
                'technical_editors_environment',
                'technical_validators_environment',
            ],
            'urban_and_environment': [
                'urban_editors',
                'administrative_editors_environment',
                'administrative_validators_environment',
                'technical_editors_environment',
                'technical_validators_environment',
            ]
        }
        allowed_group = self.get_allowed_groups(licence)
        if allowed_group in mapping:
            return mapping.get(allowed_group)

    mapping = {
        'in_progress': {
            BaseRolesMapping.get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'accepted': {
            BaseRolesMapping.get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'incomplete': {
            BaseRolesMapping.get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'refused': {
            BaseRolesMapping.get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'inacceptable': {
            BaseRolesMapping.get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'retired': {
            BaseRolesMapping.get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },
    }
