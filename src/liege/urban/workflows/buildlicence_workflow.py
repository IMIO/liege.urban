# -*- coding: utf-8 -*-

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
                task = task_config.get_started_task(opinion_request)
                if task:
                    break

            if task:
                opinion_editors.append(task.assigned_group)
        return opinion_editors

    mapping = {
        'deposit': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
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
        },

        'checking_completion': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Editor',),
            'technical_validators': ('Contributor',),
        },

        'incomplete': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'validating_completion': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Contributor',),
        },

        'complete': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'get_opinion_editors': ('ExternalReader',),
        },

    }
