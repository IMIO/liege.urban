# -*- coding: utf-8 -*-

from imio.schedule.utils import query_container_tasks

from plone import api


def reindex_licence_tasks(licence, event):
    """
    """
    with api.env.adopt_roles(['Manager']):
        for task in query_container_tasks(licence, the_objects=True):
            task.reindexObject(idxs=['shore'])
