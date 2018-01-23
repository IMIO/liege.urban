# -*- coding: utf-8 -*-

from liege.urban.workflows.licences_workflow import DefaultStateRolesMapping as LiegeBase


class StateRolesMapping(LiegeBase):
    """ """

    mapping = {
        'deposit': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor',),
            'technical_validators_environment': ('Contributor',),
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'validating_address': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Reader',),
            'technical_editors_environment': ('Reader',),
            'technical_validators_environment': ('Reader',),
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'waiting_address': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Reader',),
            'technical_editors_environment': ('Reader',),
            'technical_validators_environment': ('Reader',),
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'internal_preliminary_advice': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Reader',),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
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
    }
