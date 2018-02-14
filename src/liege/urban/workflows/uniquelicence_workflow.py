# -*- coding: utf-8 -*-

from liege.urban.workflows.licences_workflow import DefaultStateRolesMapping as LiegeBase


class StateRolesMapping(LiegeBase):
    """ """

    mapping = {
        'deposit': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'urban_readers': ('Reader',),
        },

        'validating_address': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'waiting_address': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'internal_preliminary_advice': {
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'internal_advice_done': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Contributor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'incomplete': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Contributor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'complete': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Contributor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'authorized': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Editor', 'UrbanEditor'),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'refused': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Editor', 'UrbanEditor'),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'inacceptable': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Editor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Editor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Editor', 'UrbanEditor'),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'suspension': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Editor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Editor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Editor', 'UrbanEditor'),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'abandoned': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Editor', 'UrbanEditor'),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },
    }
