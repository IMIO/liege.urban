# -*- coding: utf-8 -*-

from imio.schedule.content.condition import CreationCondition


class IsInternalOpinionRequest(CreationCondition):
    """
    Licence folderComplete event is created.
    """

    def evaluate(self):
        opinion_request = self.task_container
        opinion_config = opinion_request.getUrbaneventtypes()
        is_internal = opinion_config.id == self.task_config.id
        return is_internal
