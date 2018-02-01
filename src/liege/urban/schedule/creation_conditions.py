# -*- coding: utf-8 -*-

from imio.schedule.content.condition import EndCondition

from plone import api


class LicenceInValidatingAddressState(EndCondition):
    """
    """

    def evaluate(self):
        licence = self.task_container
        return api.content.get_state(licence) == 'validating_address'
