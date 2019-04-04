# -*- coding: utf-8 -*-

from imio.schedule.content.condition import CreationCondition

from plone import api

from zope.component import getMultiAdapter


class LicenceInValidatingAddressState(CreationCondition):
    """
    """

    def evaluate(self):
        licence = self.task_container
        return api.content.get_state(licence) == 'validating_address'


class PreliminaryAdviceCondition(CreationCondition):
    """
    """
    def __init__(self, licence, task_config):
        super(PreliminaryAdviceCondition, self).__init__(licence, task_config)
        self.preliminary_advice_event = licence.getLastInternalPreliminaryAdvice()


class PreliminaryAdviceEventCreated(PreliminaryAdviceCondition):
    """
    Preliminary advice event is created and proposed to technical validation
    """

    def evaluate(self):
        if not self.preliminary_advice_event:
            return False
        return api.content.get_state(self.preliminary_advice_event) == 'in_progress'


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


class MayorCollegeCondition(CreationCondition):
    """
    Base class for college event based conditions
    """

    def __init__(self, licence, task):
        super(MayorCollegeCondition, self).__init__(licence, task)
        self.mayor_events = licence.getAllMayorColleges()


class OneMayorCollegeProjectCreated(MayorCollegeCondition):
    """
    At least one MayorCollege project is created
    """

    def evaluate(self):
        mayor_events = self.licence.getAllMayorColleges()
        if not mayor_events:
            return False
        for event in mayor_events:
            if api.content.get_state(event) == 'draft':
                return True
        return False


class OneMayorCollegeProjectWritten(MayorCollegeCondition):
    """
    At least one MayorCollege project is written
    """

    def evaluate(self):
        if not self.mayor_events:
            return False
        for event in self.mayor_events:
            if api.content.get_state(event) == 'to_validate':
                return True
        return False


class OneProjectsSentToMayorCollege(MayorCollegeCondition):
    """
    At least one MayorCollege project is sent to college and college is not finished
    """

    def evaluate(self):
        if not self.mayor_events:
            return False
        request = api.portal.getRequest()
        ws4pm = getMultiAdapter((api.portal.get(), request), name='ws4pmclient-settings')

        for event in self.mayor_events:
            sent = ws4pm.checkAlreadySentToPloneMeeting(event)
            if sent:
                items = ws4pm._soap_searchItems({'externalIdentifier': event.UID()})
                if not items:
                    return False

                accepted_states = ['accepted', 'accepted_but_modified', 'accepted_and_returned']
                mayor_college_done = items and items[0]['review_state'] in accepted_states

                if not mayor_college_done:
                    return True
        return False
