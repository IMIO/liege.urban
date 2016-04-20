# -*- coding: utf-8 -*-

from imio.schedule.content.logic import AssignTaskGroup


class SurveyGroup(AssignTaskGroup):
    """
    Adapts a TaskContainer(the licence) into a default user
    to assign to its tasks (the licence folder manager).
    """

    def group_id(self):
        return 'survey_editors'
