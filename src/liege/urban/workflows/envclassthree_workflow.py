# -*- coding: utf-8 -*-


from liege.urban.workflows.licences_workflow import DefaultStateRolesMapping as LiegeBase


class StateRolesMapping(LiegeBase):
    """ """

    mapping = {
        'deposit': {
            'administrative_editors_environment': ('Editor', 'AddressEditor'),
            'administrative_validators_environment': ('Contributor', 'AddressEditor'),
            'technical_editors_environment': ('Reader',),
            'technical_validators_environment': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'procedure_analysis': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Reader',),
            'technical_editors_environment': ('Editor',),
            'technical_validators_environment': ('Contributor',),
            'environment_readers': ('Reader',),
        },

        'technical_validation': {
            'administrative_editors_environment': ('Reader',),
            'administrative_validators_environment': ('Reader',),
            'technical_editors_environment': ('Editor',),
            'technical_validators_environment': ('Contributor', 'AddressEditor'),
            'environment_readers': ('Reader',),
        },

        'inacceptable': {
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('Reader',),
            'technical_validators_environment': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'acceptable': {
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('Reader',),
            'technical_validators_environment': ('Reader',),
            'environment_readers': ('Reader',),
        },

        'acceptable_with_conditions': {
            'administrative_editors_environment': ('Editor',),
            'administrative_validators_environment': ('Contributor',),
            'technical_editors_environment': ('Reader',),
            'technical_validators_environment': ('Reader',),
            'environment_readers': ('Reader',),
        },
    }
