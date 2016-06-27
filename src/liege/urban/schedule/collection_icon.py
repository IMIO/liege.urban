# -*- coding: utf-8 -*-

from imio.schedule.content.task_config import ITaskConfig
from imio.schedule.interfaces import IToIcon

from zope.interface import implements


class ScheduleCollectionToIcon(object):
    """
    """
    implements(IToIcon)

    def __init__(self, collection):
        self.collection = collection

    def get_icon_url(self):
        """
        """
        cfg = self.collection.aq_parent

        if ITaskConfig.providedBy(cfg) and cfg.default_assigned_group:
            icon_url = '++resource++liege.urban/{}.png'.format(cfg.default_assigned_group)
            return icon_url

        return '++resource++liege.urban/all.png'
