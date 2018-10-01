# -*- coding: utf-8 -*-

from liege.urban.workflows.licences_workflow import DefaultStateRolesMapping


class StateRolesMapping(DefaultStateRolesMapping):
    """
    State role mapping adapter for RoadDecree content type
    """

    mapping = {
        'technical_analysis_post_investigation': {
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor', )
        }
    }
