# -*- coding: utf-8 -*-

from liege.urban.workflows.licences_workflow import DefaultStateRolesMapping as LiegeBase


class StateRolesMapping(LiegeBase):
    """
    State role mapping adapter for RoadDecree content type
    """

    mapping = {

        'folder_creation': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadDecree'),
        },

        'public_investigation': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadDecree'),
        },

        'technical_analysis_post_investigation': {
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadDecree'),
        },

        'technical_analysis_validation': {
            'fittingout_technicians': ('Reader',),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadDecree'),
        },

        'college_council_passage': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadDecree'),
        },

        'display_in_progress': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadDecree'),
        },

        'authorized': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadDecree'),
        },

        'refused': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadDecree'),
        },

        'abandoned': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadDecree'),
        },
    }
