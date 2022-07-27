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
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
        },

        'public_investigation': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
        },

        'technical_analysis_post_investigation': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
        },

        'technical_analysis_validation': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'fittingout_technicians': ('Reader',),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
        },

        'college_council_passage': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
        },

        'display_in_progress': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
        },

        'authorized': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
        },

        'refused': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
        },

        'abandoned': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor',),
            'fittingout_technicians': ('Editor', ),
            'fittingout_technicians_validators': ('Contributor',),
            'urban_readers': ('Reader', 'RoadReader'),
            'urban_internal_readers': ('InternalReader', 'RoadReader'),
        },
    }
