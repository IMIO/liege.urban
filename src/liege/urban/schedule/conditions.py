# -*- coding: utf-8 -*-

from urban.schedule.content.condition import CreationCondition


class IsInternalOpinionRequest(CreationCondition):
    """
    Licence folderComplete event is created.
    """

    def evaluate(self, task_config):
        opinion_request = self.context
        opinion_config = opinion_request.getUrbaneventtypes()
        is_internal = opinion_config.id == task_config.id
        return is_internal
