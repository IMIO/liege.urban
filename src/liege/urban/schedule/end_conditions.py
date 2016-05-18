# -*- coding: utf-8 -*-

from imio.schedule.content.condition import EndCondition

from plone import api


class ParcelsAdded(EndCondition):
    """
    At least one parcel should be defined.
    """

    def evaluate(self):
        licence = self.task_container
        return bool(licence.getParcels())


class AllParcelsAreValidated(EndCondition):
    """
    All parcels should be in the state 'validated'.
    """

    def evaluate(self):
        licence = self.task_container
        for parcel in licence.getParcels():
            if api.content.get_state(parcel) != 'validated':
                return False
        return True
