# -*- coding: utf-8 -*-

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

        opinion_editors = []
        all_opinion_request = self.context.getOpinionRequests()

        for opinion_request in all_opinion_request:
            task = None
            for task_config in schedule_config.get_all_task_configs():
                for obj in opinion_request.objectValues():
                    if IAutomatedTask.providedBy(obj) and obj.task_config_UID == task_config.UID():
                        task = obj
                        break

            if task and status_by_state[api.content.get_state(task)] is STARTED:
                opinion_editors.append(task.assigned_group)
        return opinion_editors

    mapping = {
        'deposit': {
            'administrative_editors': ('Editor', 'AddressEditor'),
            'administrative_validators': ('Contributor', 'AddressEditor'),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'validating_address': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'waiting_address': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'procedure_choice': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            get_opinion_editors: ('ExternalReader',),
        },

        'checking_completion': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            get_opinion_editors: ('ExternalReader',),
        },

        'incomplete': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            get_opinion_editors: ('ExternalReader',),
        },

        'complete': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            get_opinion_editors: ('ExternalReader',),
        },

        'procedure_choosen': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Contributor',),
            get_opinion_editors: ('ExternalReader',),
        },

        'procedure_validated': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
            get_opinion_editors: ('ExternalReader',),
        },

        'report_written': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Contributor',),
            get_opinion_editors: ('ExternalReader',),
        },

        'decision_in_progress': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            get_opinion_editors: ('ExternalReader',),
        },

        'accepted': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            get_opinion_editors: ('ExternalReader',),
        },

        'refused': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            get_opinion_editors: ('ExternalReader',),
        },

    }
