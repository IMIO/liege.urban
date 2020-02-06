# encoding: utf-8

from imio.schedule.config import states_by_status
from imio.schedule.config import STARTED
from imio.schedule.interfaces import TaskConfigNotFound

from Products.urban.interfaces import IUrbanEventType

from plone import api


import logging

logger = logging.getLogger('urban: migrations')


def migrate_env_class_three_tasks(context):
    """ recreate tasks 'recevable', 'irrecevable', ...  for envclassthree """
    logger = logging.getLogger('urban: migrate env class three tasks')
    logger.info("starting migration step")
    catalog = api.portal.get_tool('portal_catalog')
    for task_id in ['TASK_recevable', 'TASK_irrecevable', 'TASK_recevable_avec_conditions']:
        open_task_brains = catalog(portal_type='AutomatedTask', id=task_id, review_state=states_by_status[STARTED])
        for brain in open_task_brains:
            task = brain.getObject()
            try:
                task.get_task_config()
            except TaskConfigNotFound:
                api.content.delete(obj=task)
                logger.info("updated licence {}".format(task.aq_parent.Title()))

    logger.info("migration step done!")


def migrate_default_text_newlines_for_pmws(context):
    """ Delete all new lines from default text of events sent to pm"""
    logger = logging.getLogger('urban: migrate newlines for default texts sent to pm')
    logger.info("starting migration step")
    catalog = api.portal.get_tool('portal_catalog')
    event_type_brains = catalog(object_provides=IUrbanEventType.__interface__)
    for brain in event_type_brains:
        event_type = brain.getObject()
        if event_type.getEventPortalType() in ['UrbanEventCollege', 'UrbanEventMayor', 'UrbanEventNotificationCollege']:
            import ipdb; ipdb.set_trace()
    logger.info("migration step done!")


def migrate(context):
    logger = logging.getLogger('urban: migrate to 2.3')
    logger.info("starting migration steps")
    migrate_env_class_three_tasks(context)
    migrate_default_text_newlines_for_pmws(context)
    logger.info("migration done!")
