# encoding: utf-8

from imio.schedule.content.config import states_by_status
from imio.schedule.content.config import STARTED

from plone import api


import logging

logger = logging.getLogger('urban: migrations')


def migrate_env_class_three_tasks(context):
    """ """
    logger = logging.getLogger('urban: migrate env class three tasks')
    logger.info("starting migration step")
    catalog = api.portal.get_tool('portal_catalog')
    for task_id in ['TASK_recevable', 'TASK_irrecevable', 'TASK_recevable_avec_conditions']:
        open_task_brains = catalog(portal_type='AutomatedTask', id=task_id, review_state=states_by_status[STARTED])
        for brain in open_task_brains:
            task = brain.getObject()
            api.content.delete(obj=task)
            logger.info("updated licence {}".format(task.aq_prent.Title()))

    logger.info("migration step done!")


def migrate(context):
    logger = logging.getLogger('urban: migrate to 2.3')
    logger.info("starting migration steps")
    migrate_env_class_three_tasks(context)
    logger.info("migration done!")
