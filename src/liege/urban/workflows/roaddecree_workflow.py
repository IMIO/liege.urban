# -*- coding: utf-8 -*-

from liege.urban.workflows.licences_workflow import DefaultStateRolesMapping as LiegeBase


class StateRolesMapping(LiegeBase):
    """
    State role mapping adapter for RoadDecree content type
    """

    mapping = {

        'folder_creation': {
            LiegeBase.get_editors: ('Editor',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'validating_address': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'waiting_address': {
            LiegeBase.get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'technical_analysis_post_investigation': {
            'survey_editors': ('Reader', 'AddressEditor'),
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor', )
        }
    }
