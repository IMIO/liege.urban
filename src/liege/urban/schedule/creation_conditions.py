# -*- coding: utf-8 -*-

from imio.schedule.content.condition import CreationCondition

from plone import api


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
