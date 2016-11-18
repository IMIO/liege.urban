# -*- coding: utf-8 -*-

from imio.schedule.content.task import IAutomatedTask

from liege.urban.workflows.adapter import LocalRoleAdapter

from plone import api


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    def get_opinion_editor(self):
        opinion_request = self.context

        portal_urban = api.portal.get_tool('portal_urban')
        schedule_config = portal_urban.opinions_schedule

        task = None
        for task_config in schedule_config.get_all_task_configs():
            for obj in opinion_request.objectValues():
                if IAutomatedTask.providedBy(obj) and obj.task_config_UID == task_config.UID():
                    task = obj
                    break

        if task:
            return (task.assigned_group,)

        return ('technical_editors',)

    def get_opinion_editor_role(self):
        groups = self.get_opinion_editor()
        if 'technical_editors' in groups:
            return ('Contributor',)
        return ('Editor',)

    def get_technical_roles(self):
        if  'technical_editors' in self.get_opinion_editor():
            return ('Contributor',)
        return ('Reader',)

    mapping = {
        'creation': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
        },

        'waiting_opinion': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': (get_technical_roles,),
            'technical_validators': ('Reader',),
            get_opinion_editor: (get_opinion_editor_role,),
        },

        'opinion_validation': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            get_opinion_editor: ('Editor',),
        },

        'opinion_given': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            get_opinion_editor: ('Reader',),
        },

    }
