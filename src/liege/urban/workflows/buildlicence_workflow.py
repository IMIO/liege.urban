# -*- coding: utf-8 -*-

from liege.urban.workflows.licences_workflow import DefaultStateRolesMapping as LiegeBase


class StateRolesMapping(LiegeBase):
    """ """

    mapping = {
        'deposit': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'validating_address': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'waiting_address': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'procedure_choice': {
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'checking_completion': {
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'incomplete': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'complete': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'procedure_choosen': {
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'procedure_validated': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'report_written': {
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'FD_opinion': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'decision_in_progress': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'authorized': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'accepted': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'refused': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'suspension': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'frozen_suspension': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'Voirie_editors': ('RoadEditor', 'RoadReader'),
            'Voirie_validators': ('RoadEditor', 'RoadReader'),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'filed_away': {
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

        'abandoned': {
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader', 'RoadReader'),
        },

    }
