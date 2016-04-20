# -*- coding: utf-8 -*-

from eea.facetednavigation.layout.interfaces import IFacetedLayout

from imio.dashboard.browser.facetedcollectionportlet import Assignment
from imio.dashboard.utils import _updateDefaultCollectionFor

from plone import api
from plone.portlets.interfaces import IPortletManager
from plone.portlets.interfaces import ILocalPortletAssignmentManager
from plone.portlets.interfaces import IPortletAssignmentMapping
from plone.portlets.constants import CONTEXT_CATEGORY

from Products.urban.config import URBAN_TYPES
from Products.urban.setuphandlers import createFolderDefaultValues
from Products.urban.setuphandlers import createScheduleConfig
from Products.urban.setuphandlers import setFolderAllowedTypes

from urban.schedule.utils import create_tasks_collection

from zope.component import getMultiAdapter
from zope.component import getUtility

import os


def post_install(context):
    """Post install script"""
    if context.readDataFile('liegeurban_default.txt') is None:
        return
    # Do something during the installation of this package

    addLiegeGroups(context)
    setupSurveySchedule(context)
    setupOpinionsSchedule(context)
    addScheduleConfigs(context)


def addLiegeGroups(context):
    """
    Add a groups of application users.
    """

    portal_groups = api.portal.get_tool('portal_groups')
    portal_urban = api.portal.get_tool('portal_urban')

    portal_groups.addGroup("administrative_editors", title="Administrative Editors")
    portal_groups.setRolesForGroup('administrative_editors', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("administrative_editors", ("Reader", ))

    portal_groups.addGroup("administrative_validators", title="Administrative Validators")
    portal_groups.setRolesForGroup('urban_readers', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("administrative_validators", ("Reader", ))

    portal_groups.addGroup("technical_editors", title="Technical Editors")
    portal_groups.setRolesForGroup('technical_editors', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("technical_editors", ("Reader", ))

    portal_groups.addGroup("technical_validators", title="Technical Validators")
    portal_groups.setRolesForGroup('technical_validators', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("technical_validators", ("Reader", ))

    portal_groups.addGroup("survey_editors", title="Survey Editors")
    portal_groups.setRolesForGroup('survey_editors', ('UrbanMapReader', ))
    portal_urban.manage_addLocalRoles("survey_editors", ("Reader", ))

    # external services
    services = ['Voirie', 'Access', 'Plantation', 'SSSP', 'EDII']
    for service in services:
        portal_groups.addGroup("{}_editors".format(service), title="{} Editors".format(service))
        portal_groups.setRolesForGroup('{}_editors'.format(service), ('UrbanMapReader', ))
        portal_urban.manage_addLocalRoles("{}_editors".format(service), ("Reader", ))
        portal_groups.addGroup("{}_validators".format(service), title="{} Validators".format(service))
        portal_groups.setRolesForGroup('{}_validators'.format(service), ('UrbanMapReader', ))
        portal_urban.manage_addLocalRoles("{}_validators".format(service), ("Reader", ))

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

    # block parent portlets
    manager = getUtility(IPortletManager, name='plone.leftcolumn')
    blacklist = getMultiAdapter((schedule_folder, manager), ILocalPortletAssignmentManager)
    blacklist.setBlacklistStatus(CONTEXT_CATEGORY, True)

    # assign collection portlet
    manager = getUtility(IPortletManager, name='plone.leftcolumn', context=schedule_folder)
    mapping = getMultiAdapter((schedule_folder, manager), IPortletAssignmentMapping)
    if 'schedules' not in mapping.keys():
        mapping['schedules'] = Assignment('schedules')

    if not hasattr(portal_urban, 'survey_schedule'):
        createScheduleConfig(container=portal_urban, portal_type='GenericLicence', id='survey_schedule')
    schedule_config = portal_urban.survey_schedule

    setFolderAllowedTypes(schedule_folder, 'Folder')

    collection_id = 'survey_tasks'
    folder_id = schedule_folder.id
    collection_folder = getattr(schedule_folder, folder_id)

    config_path = '/schedule/config/{}.xml'.format(folder_id)
    subtyper = collection_folder.restrictedTraverse('@@faceted_subtyper')
    if not subtyper.is_faceted:
        subtyper.enable()
        collection_folder.restrictedTraverse('@@faceted_settings').toggle_left_column()
        IFacetedLayout(collection_folder).update_layout('faceted-table-items')
        collection_folder.unrestrictedTraverse('@@faceted_exportimport').import_xml(
            import_file=open(os.path.dirname(__file__) + config_path)
        )

    if not hasattr(collection_folder, collection_id):
        setFolderAllowedTypes(collection_folder, 'DashboardCollection')
        create_tasks_collection(
            schedule_config,
            container=collection_folder,
            id=collection_id,
            title="À faire",
            customViewFields=(
                u'pretty_link',
                u'sortable_title',
                u'address_column',
                u'parcelreferences_column',
                u'due_date',
                u'assigned_user_column'
            ),
            query=[
                {
                    'i': 'review_state',
                    'o': 'plone.app.querystring.operation.selection.is',
                    'v': ['to_do']
                }
            ]
        )
        setFolderAllowedTypes(collection_folder, [])

    setFolderAllowedTypes(schedule_folder, [])

    survey_collection = getattr(schedule_folder, collection_id)
    _updateDefaultCollectionFor(schedule_folder, survey_collection.UID())


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

    # block parent portlets
    manager = getUtility(IPortletManager, name='plone.leftcolumn')
    blacklist = getMultiAdapter((schedule_folder, manager), ILocalPortletAssignmentManager)
    blacklist.setBlacklistStatus(CONTEXT_CATEGORY, True)

    # assign collection portlet
    manager = getUtility(IPortletManager, name='plone.leftcolumn', context=schedule_folder)
    mapping = getMultiAdapter((schedule_folder, manager), IPortletAssignmentMapping)
    if 'schedules' not in mapping.keys():
        mapping['schedules'] = Assignment('schedules')

    if not hasattr(portal_urban, 'opinions_schedule'):
        createScheduleConfig(container=portal_urban, portal_type='UrbanEventOpinionRequest', id='opinions_schedule')
    schedule_config = portal_urban.opinions_schedule

    setFolderAllowedTypes(schedule_folder, 'Folder')

    collection_id = 'opinions_tasks'
    folder_id = schedule_folder.id
    collection_folder = getattr(schedule_folder, folder_id)

    config_path = '/schedule/config/{}.xml'.format(folder_id)
    subtyper = collection_folder.restrictedTraverse('@@faceted_subtyper')
    if not subtyper.is_faceted:
        subtyper.enable()
        collection_folder.restrictedTraverse('@@faceted_settings').toggle_left_column()
        IFacetedLayout(collection_folder).update_layout('faceted-table-items')
        collection_folder.unrestrictedTraverse('@@faceted_exportimport').import_xml(
            import_file=open(os.path.dirname(__file__) + config_path)
        )

    if not hasattr(collection_folder, collection_id):
        setFolderAllowedTypes(collection_folder, 'DashboardCollection')
        create_tasks_collection(
            schedule_config,
            container=collection_folder,
            id=collection_id,
            title="À faire",
            customViewFields=(
                u'pretty_link',
                u'sortable_title',
                u'address_column',
                u'parcelreferences_column',
                u'due_date',
                u'assigned_user_column'
            ),
            query=[
                {
                    'i': 'review_state',
                    'o': 'plone.app.querystring.operation.selection.is',
                    'v': ['to_do']
                }
            ]
        )
        setFolderAllowedTypes(collection_folder, [])

    setFolderAllowedTypes(schedule_folder, [])

    opinions_collection = getattr(schedule_folder, collection_id)
    _updateDefaultCollectionFor(schedule_folder, opinions_collection.UID())


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
        createFolderDefaultValues(
            schedule_folder,
            schedule_config[schedule_config_id]
        )

    for urban_type in URBAN_TYPES:
        licence_config_id = urban_type.lower()
        if licence_config_id in schedule_config:
            config_folder = getattr(portal_urban, licence_config_id)
            schedule_folder = getattr(config_folder, 'schedule')
            createFolderDefaultValues(
                schedule_folder,
                schedule_config[licence_config_id]
            )
