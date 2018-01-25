# -*- coding: utf-8 -*-

from imio.schedule.interfaces import IDefaultEndingStates

from liege.urban.config import LICENCE_FINAL_STATES

from zope.interface import implements


class LiegeLicencesDefaultEndingStates(object):
    """
    """
    implements(IDefaultEndingStates)

    def __init__(self, task_container):
        self.licence = task_container

    def __call__(self):
        return LICENCE_FINAL_STATES
