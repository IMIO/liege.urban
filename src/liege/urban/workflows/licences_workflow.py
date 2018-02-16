# -*- coding: utf-8 -*-

from imio.schedule.config import DONE
from imio.schedule.config import STARTED
from imio.schedule.config import status_by_state
from imio.schedule.content.task import IAutomatedTask

from plone import api

from Products.urban.workflows.licence_workflow import StateRolesMapping as BaseRolesMapping


class DefaultStateRolesMapping(BaseRolesMapping):
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
        'in_progress': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'accepted': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'incomplete': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'refused': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },

        'retired': {
            BaseRolesMapping.get_readers: ('Reader',),
            BaseRolesMapping.get_editors: ('Editor',),
            'Voirie_editors': ('RoadEditor',),
            'Voirie_validators': ('RoadEditor',),
            get_opinion_editors: ('ExternalReader',),
            'survey_editors': ('Reader', 'AddressEditor'),
        },
    }
