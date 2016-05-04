# -*- coding: utf-8 -*-

from imio.schedule.content.condition import EndCondition

from plone import api


class AllParcelsAreValidated(EndCondition):
    """
    Alli parcels should in the state 'validated'.
    """

    def evaluate(self):
        licence = self.task_container
        for parcel in licence.getParcels():
            if api.content.get_state(parcel) != 'validated':
                return False
        return True
