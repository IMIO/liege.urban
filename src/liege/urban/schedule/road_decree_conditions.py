# -*- coding: utf-8 -*-

from imio.schedule.content.condition import Condition


class StreetTechnicalAnalysisCompleted(Condition):

    def evaluate(self):
        licence = self.task_container
        if licence.getRoadAnalysis():
            return True
        return False


class StreetTechnicalAnalysisValidated(Condition):

    def evaluate(self):
        # XXX Should be implemented
        return True


class DecreeProjectWrited(Condition):

    def evaluate(self):
        # XXX Should be implemented
        return True


class DecreeProjectValidatedSended(Condition):

    def evaluate(self):
        # XXX Should be implemented
        return True


class CollegeInProgress(Condition):

    def evaluate(self):
        # XXX Should be implemented
        return True


class CollegeCompleted(Condition):

    def evaluate(self):
        # XXX Should be implemented
        return True


class CouncilInProgress(Condition):

    def evaluate(self):
        # XXX Should be implemented
        return True


class CouncilCompleted(Condition):

    def evaluate(self):
        # XXX Should be implemented
        return True
