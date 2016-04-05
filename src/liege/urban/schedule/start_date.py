# -*- coding: utf-8 -*-

from urban.schedule.content.logic import StartDate


class AskOpinionDate(StartDate):
    """
    Returns ask date of the opinion request.
    """

    def start_date(self):
        opinion_request = self.task_container
        ask_date = opinion_request.getEventDate()
        return ask_date
