# -*- coding: utf-8 -*-

from imio.schedule.content.task import IAutomatedTask

from Products.urban.interfaces import IGenericLicence

from plone.indexer import indexer


@indexer(IGenericLicence)
def genericlicence_shoreindex(licence):
    """
    Index Liège shore value
    """
    shores = set([p.getShore() for p in licence.getParcels()])
    return list(shores)


@indexer(IAutomatedTask)
def task_shoreindex(task):
    """
    Index Liège shore value
    """
    licence = task.get_container()
    shores = set([p.getShore() for p in licence.getParcels()])
    return list(shores)
