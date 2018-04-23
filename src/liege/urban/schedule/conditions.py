# -*- coding: utf-8 -*-

from imio.schedule.content.condition import Condition
from imio.schedule.content.condition import CreationCondition

from liege.urban.config import LICENCE_FINAL_STATES

from plone import api

from zope.component import getMultiAdapter


class WriteInquiryDocumentsCondition(CreationCondition):
    """
    Licence inquiry documents are produced.
    """

    def evaluate(self):
        licence = self.task_container
        inquiry = licence.getLastInquiry()
        if not inquiry:
            return False

        return api.content.get_state(inquiry) == 'preparing_documents'


class InquiryDocumentsDone():
    """
    Licence inquiry documents are produced.
    """

    def evaluate(self):
        licence = self.task_container
        inquiry = licence.getLastInquiry()
        if not inquiry:
            return False

        return api.content.get_state(inquiry) == 'to_validate'


class InquiryDocumentsDoneCondition(InquiryDocumentsDone, Condition):
    """
    Licence inquiry documents are produced.
    """


class InquiryDocumentsDoneCreationCondition(InquiryDocumentsDone, CreationCondition):
    """
    Licence inquiry documents are produced.
    """


class InquiryDocumentsValidatedCondition(Condition):
    """
    Licence inquiry documents are validated.
    """

    def evaluate(self):
        licence = self.task_container
        inquiry = licence.getLastInquiry()
        if not inquiry:
            return False

        return api.content.get_state(inquiry) == 'sending_documents'


class InquiryDocumentsSentCondition(Condition):
    """
    Licence inquiry documents are sent.
    """

    def evaluate(self):
        licence = self.task_container
        inquiry = licence.getLastInquiry()
        if not inquiry:
            return False

        return api.content.get_state(inquiry) == 'in_progress'


class WriteAnnouncementDocumentsCondition(CreationCondition):
    """
    Licence announcement documents are produced.
    """

    def evaluate(self):
        licence = self.task_container
        announcement = licence.getLastAnnouncement()
        if not announcement:
            return False

        return api.content.get_state(announcement) == 'preparing_documents'


class AnnouncementDocumentsDone():
    """
    Licence announcement documents are produced.
    """

    def evaluate(self):
        licence = self.task_container
        announcement = licence.getLastAnnouncement()
        if not announcement:
            return False

        return api.content.get_state(announcement) == 'to_validate'


class AnnouncementDocumentsDoneCondition(AnnouncementDocumentsDone, Condition):
    """
    Licence announcement documents are produced.
    """


class AnnouncementDocumentsDoneCreationCondition(AnnouncementDocumentsDone, CreationCondition):
    """
    Licence announcement documents are produced.
    """


class AnnouncementDocumentsValidatedCondition(Condition):
    """
    Licence announcement documents are validated.
    """

    def evaluate(self):
        licence = self.task_container
        announcement = licence.getLastAnnouncement()
        if not announcement:
            return False

        return api.content.get_state(announcement) == 'sending_documents'


class AnnouncementDocumentsSentCondition(Condition):
    """
    Licence announcement documents are sent.
    """

    def evaluate(self):
        licence = self.task_container
        announcement = licence.getLastAnnouncement()
        if not announcement:
            return False

        return api.content.get_state(announcement) == 'in_progress'


class AcknowledgmentWrittenCondition(Condition):
    """
    Draft of acknowledgment document is done.
    """

    def evaluate(self):
        licence = self.task_container
        ack_event = licence.getLastAcknowledgment()
        if not ack_event:
            return False

        return api.content.get_state(ack_event) == 'to_validate'


class AcknowledgmentValidatedCondition(Condition):
    """
    Validation of acknowledgment document is done.
    """

    def evaluate(self):
        licence = self.task_container
        ack_event = licence.getLastAcknowledgment()
        if not ack_event:
            return False

        return api.content.get_state(ack_event) == 'to_send'


class IsInternalOpinionRequest(CreationCondition):
    """
    Licence folderComplete event is created.
    """

    def evaluate(self):
        opinion_request = self.task_container
        opinion_config = opinion_request.getUrbaneventtypes()
        is_internal = opinion_config.id in self.task_config.id
        return is_internal


class OnlyNeedFDOpinion(CreationCondition):
    """
    Procedure choice is FD opinion only.
    """

    def evaluate(self):
        licence = self.task_container
        choice = licence.getProcedureChoice()
        only_FD = 'FD' in choice and len(choice) is 1
        return only_FD


class LicenceStateIsFDOpinion(CreationCondition):
    """
    Licence state is 'FD_opinion'.
    """

    def evaluate(self):
        return api.content.get_state(self.task_container) == 'FD_opinion'


class SimpleCollegeCondition(Condition):
    """
    Base class for college event based conditions
    """

    def __init__(self, licence, task):
        super(SimpleCollegeCondition, self).__init__(licence, task)
        self.college_event = licence.getLastSimpleCollege()


class CollegeProjectWritten(SimpleCollegeCondition):
    """
    College project is written
    """

    def evaluate(self):
        if not self.college_event:
            return False
        return api.content.get_state(self.college_event) == 'to_validate'


class CollegeProjectValidated(SimpleCollegeCondition):
    """
    College project is validated
    """

    def evaluate(self):
        if not self.college_event:
            return False
        return api.content.get_state(self.college_event) == 'decision_in_progress'


class ProjectSentToCollege(SimpleCollegeCondition):
    """
    College project is sent to college
    """

    def evaluate(self):
        if not self.college_event:
            return False
        request = api.portal.getRequest()
        ws4pm = getMultiAdapter((api.portal.get(), request), name='ws4pmclient-settings')

        sent = ws4pm.checkAlreadySentToPloneMeeting(self.college_event)

        return sent


class CollegeDone(SimpleCollegeCondition):
    """
    College is done
    """

    def evaluate(self):
        if not self.college_event:
            return False

        request = api.portal.getRequest()
        ws4pm = getMultiAdapter((api.portal.get(), request), name='ws4pmclient-settings')

        # if the current user has no acces to pm return False
        if not ws4pm._soap_getUserInfos():
            return False

        items = ws4pm._soap_searchItems({'externalIdentifier': self.college_event.UID()})
        if not items:
            return False

        accepted_states = ['accepted', 'accepted_but_modified', 'accepted_and_returned']
        college_done = items and items[0]['review_state'] in accepted_states

        return college_done


class CollegeEventClosed(SimpleCollegeCondition):
    """
    College event state is 'closed'
    """

    def evaluate(self):
        if not self.college_event:
            return False
        return api.content.get_state(self.college_event) == 'closed'


class FDCondition(Condition):
    """
    Base class for FD opinion request condition
    """

    def __init__(self, licence, task):
        super(FDCondition, self).__init__(licence, task)
        self.FD_event = licence.getLastWalloonRegionOpinionRequest()


class FDOpinionAsked(FDCondition):
    """
    Opinion request is sent to FD
    """

    def evaluate(self):
        if not self.FD_event:
            return False
        return api.content.get_state(self.FD_event) == 'waiting_opinion'


class FDOpinionReceived(FDCondition):
    """
    """

    def evaluate(self):
        if not self.FD_event:
            return False
        return api.content.get_state(self.FD_event) == 'opinion_given'


class DecisionProjectDraftedCondition(Condition):
    """
    Licence decision project is drafted.
    """

    def evaluate(self):
        licence = self.task_container
        decision_event = licence.getLastTheLicence()
        if not decision_event:
            return False

        if api.content.get_state(decision_event) == 'draft':
            return False

        return True


class DecisionProjectSentCondition(Condition):
    """
    Licence decision project is sent to PM.
    """

    def evaluate(self):
        licence = self.task_container
        decision_event = licence.getLastTheLicence()
        if not decision_event:
            return False

        if api.content.get_state(decision_event) not in ['decision_in_progress', 'notification', 'closed']:
            return False

        return True


class DecisionNotifiedCondition(Condition):
    """
    Licence decision has been notified to applicants, FD, ...
    """

    def evaluate(self):
        licence = self.task_container
        decision_event = licence.getLastTheLicence()
        if not decision_event:
            return False

        return api.content.get_state(decision_event) == 'closed'


class LicenceEndedCondition(Condition):
    """
    Licence is in a final state
    """

    def evaluate(self):
        licence = self.task_container
        is_ended = api.content.get_state(licence) in LICENCE_FINAL_STATES
        return is_ended


class PreliminaryAdviceCondition(Condition):
    """
    """
    def __init__(self, licence, task):
        super(PreliminaryAdviceCondition, self).__init__(licence, task)
        self.preliminary_advice_event = licence.getLastInternalPreliminaryAdvice()


class PreliminaryAdviceWritten(PreliminaryAdviceCondition):
    """
    Preliminary advice event is created and proposed to technical validation
    """

    def evaluate(self):
        if not self.preliminary_advice_event:
            return False
        return api.content.get_state(self.preliminary_advice_event) == 'technical_validation'


class PreliminaryAdviceTechnicalValidationDone(PreliminaryAdviceCondition):
    """
    Preliminary advice event is proposed to executive validation
    """

    def evaluate(self):
        if not self.preliminary_advice_event:
            return False
        return api.content.get_state(self.preliminary_advice_event) == 'executive_validation'


class PreliminaryAdviceSent(PreliminaryAdviceCondition):
    """
    Preliminary advice event is sent
    """

    def evaluate(self):
        if not self.preliminary_advice_event:
            return False
        return api.content.get_state(self.preliminary_advice_event) == 'preliminary_advice_event'
