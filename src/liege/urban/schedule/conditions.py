# -*- coding: utf-8 -*-

from imio.schedule.content.condition import Condition
from imio.schedule.content.condition import CreationCondition

from plone import api


class InquiryZoneIdentifiedCondition(Condition):
    """
    Licence inquiry zone is identified.
    """

    def evaluate(self):
        licence = self.task_container
        inquiry = licence.getLastInquiry()
        if not inquiry:
            return False

        if not inquiry.getRecipients():
            return False

        if api.content.get_state(inquiry) == 'zone_identification':
            return False

        return True


class InquiryDocumentsDoneCondition(Condition):
    """
    Licence inquiry documents are produced and validated.
    """

    def evaluate(self):
        licence = self.task_container
        inquiry = licence.getLastInquiry()
        if not inquiry:
            return False

        if not api.content.get_state(inquiry) in ['in_progress', 'done']:
            return False

        return True


class IsInternalOpinionRequest(CreationCondition):
    """
    Licence folderComplete event is created.
    """

    def evaluate(self):
        opinion_request = self.task_container
        opinion_config = opinion_request.getUrbaneventtypes()
        is_internal = opinion_config.id == self.task_config.id
        return is_internal
