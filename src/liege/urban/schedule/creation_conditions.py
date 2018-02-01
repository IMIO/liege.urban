# -*- coding: utf-8 -*-

from imio.schedule.content.condition import CreationCondition

from plone import api


class LicenceInValidatingAddressState(CreationCondition):
    """
    """

    def evaluate(self):
        licence = self.task_container
        return api.content.get_state(licence) == 'validating_address'
