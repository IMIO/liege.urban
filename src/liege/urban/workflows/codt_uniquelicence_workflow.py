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
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            LiegeBase.get_readers: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'validating_address': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'survey_editors': ('Reader', 'AddressEditor'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'waiting_address': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'survey_editors': ('Reader', 'AddressEditor'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'internal_preliminary_advice': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'administrative_validators': ('Contributor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
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
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
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
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
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
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'technical_report_validation': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Reviewer', 'Contributor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Contributor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'college_in_progress': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Reviewer', 'Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Reviewer', 'Contributor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Contributor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'technical_synthesis_validation': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Reviewer', 'Contributor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Contributor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'final_decision_in_progress': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Contributor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'authorized': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Editor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Editor', 'UrbanEditor'),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'refused': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Editor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Editor', 'UrbanEditor'),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
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
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
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
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'abandoned': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Editor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_editors': ('Editor', 'UrbanEditor'),
            'administrative_validators': ('Editor', 'UrbanEditor'),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
            'environment_readers': ('Reader',),
        },
    }
