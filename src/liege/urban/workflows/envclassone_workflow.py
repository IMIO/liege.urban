# -*- coding: utf-8 -*-


from liege.urban.workflows.licences_workflow import DefaultStateRolesMapping as LiegeBase


class StateRolesMapping(LiegeBase):
    """ """

    mapping = {
        'deposit': {
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'environment_readers': ('Reader',),
        },

        'validating_address': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'environment_readers': ('Reader',),
        },

        'waiting_address': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'environment_readers': ('Reader',),
        },


        'checking_completion': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('EnvironmentEditor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },

        'complete': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('EnvironmentEditor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },

        'incomplete': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'environment_readers': ('Reader',),
        },

        'technical_report_validation': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },

        'college_in_progress': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('EnvironmentEditor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },

        'FD_opinion': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('EnvironmentEditor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },

        'technical_synthesis_validation': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },

        'final_decision_in_progress': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('EnvironmentEditor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },

        'inacceptable': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('EnvironmentEditor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },

        'authorized': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('EnvironmentEditor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },

        'refused': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('EnvironmentEditor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },

        'abandoned': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('EnvironmentEditor',),
            'technical_validators_environment': ('EnvironmentContributor',),
            'environment_readers': ('Reader',),
        },
    }
