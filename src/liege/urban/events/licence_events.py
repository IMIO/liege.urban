# -*- coding: utf-8 -*-

from imio.schedule.utils import query_container_tasks


def reindex_licence_tasks(licence, event):
    """
    """
    for task in query_container_tasks(licence, the_objects=True):
        task.reindexObject(idxs=['shore'])
