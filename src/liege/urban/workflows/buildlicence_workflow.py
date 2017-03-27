# -*- coding: utf-8 -*-

from imio.schedule.config import DONE
from imio.schedule.config import STARTED
from imio.schedule.config import status_by_state
from imio.schedule.content.task import IAutomatedTask

from plone import api

from liege.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """ """

    def get_opinion_editors(self):
        """
        Return groups who have external opinion to give on the licence.
        Thes groups should be to able to partially read the licence (
        'ExternalReader' role)
        """
        portal_urban = api.portal.get_tool('portal_urban')
        schedule_config = portal_urban.opinions_schedule

        exceptions = ['Voirie_editors', 'Voirie_Validators']
        opinion_editors = []
        all_opinion_request = self.context.getOpinionRequests()

        for opinion_request in all_opinion_request:
            task = None
            for task_config in schedule_config.get_all_task_configs():
                for obj in opinion_request.objectValues():
                    if IAutomatedTask.providedBy(obj) and obj.task_config_UID == task_config.UID():
                        task = obj
                        if task and status_by_state[api.content.get_state(task)] in [STARTED, DONE]:
                            group = task.assigned_group
                            if group not in exceptions:
                                opinion_editors.append(group)

        return opinion_editors

    mapping = {
        'deposit': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'validating_address': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'waiting_address': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'procedure_choice': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'checking_completion': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'incomplete': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'complete': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'procedure_choosen': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Contributor',),
            get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'procedure_validated': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'report_written': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'FD_opinion': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'decision_in_progress': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            get_opinion_editors: ('ExternalReader',),
            'urban_readers': ('Reader',),
        },

        'authorized': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'accepted': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

        'refused': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Editor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'Voirie_editors': ('RoadReader',),
            'Voirie_validators': ('RoadReader',),
            get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
            'urban_readers': ('Reader',),
        },

    }
