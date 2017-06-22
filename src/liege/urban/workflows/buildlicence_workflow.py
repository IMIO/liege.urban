# -*- coding: utf-8 -*-

from liege.urban.workflows.licences_workflow import DefaultStateRolesMapping as LiegeBase


class StateRolesMapping(LiegeBase):
    """ """

    mapping = {
        'deposit': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'validating_address': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'waiting_address': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'procedure_choice': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'checking_completion': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'incomplete': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'complete': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'procedure_choosen': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'procedure_validated': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'report_written': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'FD_opinion': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'decision_in_progress': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'authorized': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
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
            'urban_readers': ('Reader',),
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
            'urban_readers': ('Reader',),
        },

        'suspension': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

    }
