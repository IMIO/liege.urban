# -*- coding: utf-8 -*-

from imio.schedule.content.task import IAutomatedTask

from Products.urban.workflows.adapter import LocalRoleAdapter

from plone import api


class StateRolesMapping(LocalRoleAdapter):
    """
    """

    def get_opinion_group(self, groupe_type='editors'):
        opinion_request = self.context

        portal_urban = api.portal.get_tool('portal_urban')
        schedule_config = portal_urban.opinions_schedule

        task = None
        for task_config in schedule_config.get_all_task_configs():
            for obj in opinion_request.objectValues():
                is_task = IAutomatedTask.providedBy(obj)
                if is_task and obj.task_config_UID == task_config.UID():
                    if obj.assigned_group.endswith(groupe_type):
                        task = obj
                        break

        if task:
            return (task.assigned_group,)

        return ('technical_editors',)

    def get_opinion_editor(self):
        return self.get_opinion_group('editors')

    def get_opinion_validator(self):
        return self.get_opinion_group('validators')

    def get_opinion_editor_role(self):
        groups = self.get_opinion_editor()
        if 'technical_editors' in groups:
            return ('Reader', 'Contributor',)
        return ('Reader', 'Editor',)

    def get_technical_roles(self):
        if 'technical_editors' in self.get_opinion_editor():
            return ('Reader', 'Contributor',)
        return ('Reader',)

    mapping = {
        'creation': {
            'administrative_editors': ('Reader', 'Editor',),
            'administrative_validators': ('Reader', 'Contributor',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'opinions_editors': ('Reader',),
            'Voirie_editors': ('Reader',),
            'Voirie_validators': ('Reader',),
            'survey_editors': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'waiting_opinion': {
            'administrative_editors': (get_technical_roles,),
            'administrative_validators': (get_technical_roles,),
            'technical_editors': (get_technical_roles,),
            'technical_validators': ('Reader',),
            'Voirie_editors': ('Reader',),   # !!! order matters, let voirie role be overwritten
            'Voirie_validators': ('Reader',),# by 'get_opinion_...' if needed
            get_opinion_editor: (get_opinion_editor_role,),
            get_opinion_validator: (get_opinion_editor_role,),
            'survey_editors': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'opinion_validation': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'Voirie_editors': ('Reader',),   # !!! order matters, let voirie role be overwritten
            'Voirie_validators': ('Reader',),# by 'get_opinion_...' if needed
            get_opinion_editor: ('Reader',),
            get_opinion_validator: ('Reader', 'Contributor',),
            'survey_editors': ('Reader',),
            'urban_readers': ('Reader',),
        },

        'opinion_given': {
            'administrative_editors': ('Reader',),
            'administrative_validators': ('Reader',),
            'technical_editors': ('Reader',),
            'technical_validators': ('Reader',),
            'Voirie_editors': ('Reader',),   # !!! order matters, let voirie role be overwritten
            'Voirie_validators': ('Reader',),# by 'get_opinion_...' if needed
            get_opinion_editor: ('Reader',),
            get_opinion_validator: ('Reader',),
            'survey_editors': ('Reader',),
            'urban_readers': ('Reader',),
        },

    }
