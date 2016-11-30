# -*- coding: utf-8 -*-

from plone import api

from Products.urban.config import URBAN_TYPES
from Products.urban.setuphandlers import createScheduleConfig

from imio.schedule.utils import set_schedule_view

from zope.interface import alsoProvides

import os


def post_install(context):
    """Post install script"""
    if context.readDataFile('liegeurban_default.txt') is None:
        return
    # Do something during the installation of this package

    setEventTypeMapping(context)
    addLiegeGroups(context)
    setupSurveySchedule(context)
    setupOpinionsSchedule(context)
    addScheduleConfigs(context)
    addTestUsers(context)


def setEventTypeMapping(context):
    """
    """
    portal_urban = api.portal.get_tool('portal_urban')
    portal_urban.eventtype_portaltype_mapping['Products.urban.interfaces.IWalloonRegionOpinionRequestEvent'] = 'UrbanEventFDOpinion'
    portal_urban.eventtype_portaltype_mapping['Products.urban.interfaces.IAcknowledgmentEvent'] = 'UrbanEventAcknowledgment'
    portal_urban.eventtype_portaltype_mapping['liege.urban.interfaces.IInternalOpinionRequestEvent'] = 'UrbanEventOpinionRequest'


def addLiegeGroups(context):
    """
    Add a groups of application users.
    """

    portal_groups = api.portal.get_tool('portal_groups')
    portal_urban = api.portal.get_tool('portal_urban')

    portal_groups.addGroup("administrative_editors", title="Administrative Editors")
    portal_groups.setRolesForGroup('administrative_editors', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("administrative_editors", ("Reader", ))
    portal_groups.addPrincipalToGroup("administrative_editors", 'urban_readers')
    portal_groups.addPrincipalToGroup("administrative_editors", 'urban_editors')

    portal_groups.addGroup("administrative_validators", title="Administrative Validators")
    portal_groups.setRolesForGroup('administrative_validators', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("administrative_validators", ("Reader", ))
    portal_groups.addPrincipalToGroup("administrative_editors", 'urban_readers')
    portal_groups.addPrincipalToGroup("administrative_editors", 'urban_editors')

    portal_groups.addGroup("technical_editors", title="Technical Editors")
    portal_groups.setRolesForGroup('technical_editors', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("technical_editors", ("Reader", ))
    portal_groups.addPrincipalToGroup("administrative_editors", 'urban_readers')

    portal_groups.addGroup("technical_validators", title="Technical Validators")
    portal_groups.setRolesForGroup('technical_validators', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("technical_validators", ("Reader", ))
    portal_groups.addPrincipalToGroup("administrative_editors", 'urban_readers')

    portal_groups.addGroup("survey_editors", title="Survey Editors")
    portal_groups.setRolesForGroup('survey_editors', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("survey_editors", ("Reader", ))

    # external services
    portal_groups.addGroup("opinions_editors", title="Opinion Editors")
    portal_groups.setRolesForGroup('opinions_editors', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("opinions_editors", ("Reader", ))
    services = ['Voirie', 'Access', 'Plantation', 'SSSP', 'EDII']
    for service in services:
        portal_groups.addGroup("{}_editors".format(service), title="{} Editors".format(service))
        portal_groups.setRolesForGroup('{}_editors'.format(service), ('UrbanMapReader', ))
        portal_urban.manage_addLocalRoles("{}_editors".format(service), ("Reader", ))
        portal_groups.addPrincipalToGroup("{}_editors".format(service), 'opinions_editors')
        portal_groups.addGroup("{}_validators".format(service), title="{} Validators".format(service))
        portal_groups.setRolesForGroup('{}_validators'.format(service), ('UrbanMapReader', ))
        portal_urban.manage_addLocalRoles("{}_validators".format(service), ("Reader", ))
        portal_groups.addPrincipalToGroup("{}_validators".format(service), 'opinions_editors')

    portal_urban.reindexObjectSecurity()


def setupSurveySchedule(context):
    """
    Enable schedule faceted navigation on schedule folder.
    """
    site = context.getSite()
    urban_folder = site.urban
    portal_urban = api.portal.get_tool('portal_urban')

    if not hasattr(urban_folder, 'survey_schedule'):
        urban_folder.invokeFactory('Folder', id='survey_schedule')
    schedule_folder = getattr(urban_folder, 'survey_schedule')
    schedule_folder.manage_addLocalRoles("survey_editors", ("Reader", ))
    schedule_folder.reindexObjectSecurity()

    schedule_config = createScheduleConfig(
        container=portal_urban,
        portal_type='GenericLicence',
        title=u'Configuration d\'échéances survey',
        id='survey_schedule'
    )

    config_path = '{}/schedule/config/survey_schedule.xml'.format(os.path.dirname(__file__))
    set_schedule_view(schedule_folder, config_path, schedule_config)


def setupOpinionsSchedule(context):
    """
    Enable schedule faceted navigation on schedule folder.
    """
    site = context.getSite()
    urban_folder = site.urban
    portal_urban = api.portal.get_tool('portal_urban')

    if not hasattr(urban_folder, 'opinions_schedule'):
        urban_folder.invokeFactory('Folder', id='opinions_schedule')
    schedule_folder = getattr(urban_folder, 'opinions_schedule')
    schedule_folder.manage_addLocalRoles("opinions_editors", ("Reader", ))
    schedule_folder.reindexObjectSecurity()

    schedule_config = createScheduleConfig(
        container=portal_urban,
        portal_type='UrbanEventOpinionRequest',
        id='opinions_schedule',
        title=u'Configuration d\'échéances avis de services',
    )

    config_path = '{}/schedule/config/survey_schedule.xml'.format(os.path.dirname(__file__))
    set_schedule_view(schedule_folder, config_path, schedule_config)


def addScheduleConfigs(context):
    """
    Add schedule config for each licence type.
    """
    if context.readDataFile('liegeurban_default.txt') is None:
        return

    profile_name = context._profile_path.split('/')[-1]
    module_name = 'liege.urban.profiles.%s.schedule_config' % profile_name
    attribute = 'schedule_config'
    module = __import__(module_name, fromlist=[attribute])
    schedule_config = getattr(module, attribute)

    portal_urban = api.portal.get_tool('portal_urban')

    for schedule_config_id in ['survey_schedule', 'opinions_schedule']:
        schedule_folder = getattr(portal_urban, schedule_config_id)
        _create_task_configs(schedule_folder, schedule_config[schedule_config_id])

    for urban_type in URBAN_TYPES:
        licence_config_id = urban_type.lower()
        if licence_config_id in schedule_config:
            config_folder = getattr(portal_urban, licence_config_id)
            schedule_folder = getattr(config_folder, 'schedule')
            taskconfigs = schedule_config[licence_config_id]
            _create_task_configs(schedule_folder, taskconfigs)


def _create_task_configs(container, taskconfigs):
    """
    """
    for taskconfig_kwargs in taskconfigs:
        subtasks = taskconfig_kwargs.get('subtasks', [])
        task_config_id = taskconfig_kwargs['id']

        if task_config_id not in container.objectIds():
            marker_interface = taskconfig_kwargs.get('marker_interface', None)

            task_config_id = container.invokeFactory(**taskconfig_kwargs)
            task_config = getattr(container, task_config_id)

            # set custom view fields
            task_config.dashboard_collection.customViewFields = (
                u'sortable_title',
                u'address_column',
                u'assigned_user_column',
                u'status',
                u'due_date',
                u'task_actions_column',
            )

            # set marker_interface
            if marker_interface:
                alsoProvides(task_config, marker_interface)

        task_config = getattr(container, task_config_id)
        for subtasks_kwargs in subtasks:
            _create_task_configs(container=task_config, taskconfigs=subtasks)


def addTestUsers(context):
    """
    Add some test users for each group
    """
    password = '12345'
    email = 'dll@imio.be'

    users = [
        {
            'username': 'armin',
            'group': 'administrative_editors',
            'properties': {'fullname': 'Edi Armin'},
        },
        {
            'username': 'valere',
            'group': 'administrative_validators',
            'properties': {'fullname': 'Valère Armin'},
        },
        {
            'username': 'teckel',
            'group': 'technical_editors',
            'properties': {'fullname': 'Eddy Teckel'},
        },
        {
            'username': 'valtec',
            'group': 'technical_validators',
            'properties': {'fullname': 'Valérie Teckel'},
        },
        {
            'username': 'survivor',
            'group': 'survey_editors',
            'properties': {'fullname': 'Survivor Survey'},
        },
    ]

    for user_args in users:
        group_id = user_args.pop('group')
        if not api.user.get(username=user_args.get('username')):
            user = api.user.create(password=password, email=email, **user_args)
            api.group.add_user(groupname=group_id, username=user.id)
