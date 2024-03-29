# -*- coding: utf-8 -*-

from liege.urban.workflows.licences_workflow import DefaultStateRolesMapping as LiegeBase
from Products.urban.interfaces import ICODT_IntegratedLicence


class StateRolesMapping(LiegeBase):
    """ """

    def __init__(self, context):
        self.context = context
        self.licence = self.context
        if ICODT_IntegratedLicence.providedBy(context):
            self.mapping = LiegeBase.mapping

    mapping = {
        'deposit': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            LiegeBase.get_readers: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
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
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
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
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
        },

        'internal_preliminary_advice': {
            'administrative_editors_environment': ('Editor', 'EnvironmentEditor'),
            'administrative_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'technical_editors_environment': ('Editor', 'EnvironmentEditor'),
            'technical_validators_environment': ('Contributor', 'EnvironmentEditor'),
            'administrative_validators': ('Contributor', 'UrbanEditor'),
            'technical_editors': ('Editor', 'UrbanEditor'),
            'technical_validators': ('Contributor', 'UrbanEditor'),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
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
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
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
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'environment_readers': ('Reader', 'RoadReader'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'environment_readers': ('Reader', 'RoadReader'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'environment_readers': ('Reader', 'RoadReader'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
        },

        'frozen_suspension': {
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
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
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
            'environment_readers': ('Reader', 'RoadReader'),
        },
    }
