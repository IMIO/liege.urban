# -*- coding: utf-8 -*-

from Products.urban.interfaces import IEnvClassBordering
from Products.urban.workflows.licence_workflow import StateRolesMapping as BaseRolesMapping


class DefaultStateRolesMapping(BaseRolesMapping):
    """ """

    def get_readers(self):
        """ """
        licence = self.licence
        # Bordering can be read by urban groups as well.
        if IEnvClassBordering.providedBy(licence):
            return ['urban_readers', 'environment_readers']
        else:
            return super(DefaultStateRolesMapping, self).get_readers()

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
            get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'accepted': {
            get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'incomplete': {
            get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'refused': {
            get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'inacceptable': {
            get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'retired': {
            get_readers: ('Reader',),
            get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor', 'Reader'),
            'Voirie_validators': ('RoadEditor', 'Reader'),
            BaseRolesMapping.get_opinion_editors: ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },
    }
