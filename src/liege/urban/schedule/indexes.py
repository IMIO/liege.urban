# -*- coding: utf-8 -*-

from imio.schedule.content.task import IAutomatedTask

from plone.indexer import indexer


@indexer(IAutomatedTask)
def task_reference_index(task):
    """
    Index licence reference on their tasks to be able
    to query on it.
    """
    licence = task.get_container()
    reference = licence.getReference()
    return reference


@indexer(IAutomatedTask)
def task_shore_index(task):
    """
    Index licence shore on their tasks to be able
    to query on it.
    """
    licence = task.get_container()
    shore = licence.getShore()
    return [shore]
