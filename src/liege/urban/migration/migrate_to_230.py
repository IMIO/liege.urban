# encoding: utf-8

from plone import api


import logging

logger = logging.getLogger('urban: migrations')


def migrate_college_urban_event_types(context):
    """ """
    logger = logging.getLogger('urban: migrate colleg urban event types')
    logger.info("starting migration step")
    catalog = api.portal.get_tool('portal_catalog')
    to_migrate = [b.getObject() for b in catalog(portal_type='OpinionRequestEventType') if b.id.startswith('ask_')]
    for event_type in to_migrate:
        event_type.setIs_internal_service(True)
        event_type.setInternal_service(event_type.id.split('_')[1])
    logger.info("migration step done!")


def migrate(context):
    logger = logging.getLogger('urban: migrate to 2.3')
    logger.info("starting migration steps")
    migrate_college_urban_event_types(context)
    logger.info("migration done!")
