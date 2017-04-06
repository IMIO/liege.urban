# -*- coding: utf-8 -*-

from liege.urban.interfaces import IShore

from plone.indexer import indexer

from Products.urban.interfaces import IArticle127
from Products.urban.interfaces import IBuildLicence
from Products.urban.interfaces import IGenericLicence
from Products.urban.interfaces import ISimpleCollegeEvent

from zope.component import queryAdapter


@indexer(IGenericLicence)
def genericlicence_shore_index(licence):
    """
    Index Liège shore value
    """
    adapter = queryAdapter(licence, IShore)
    shore = adapter.get_shore()
    return shore


@indexer(IArticle127)
def article127_decisiondate(licence):
    decision_event = licence._getLastEvent(ISimpleCollegeEvent, use_catalog=False)
    if decision_event:
        return decision_event.getEventDate()


@indexer(IBuildLicence)
def buillicence_decisiondate(licence):
    decision_event = licence._getLastEvent(ISimpleCollegeEvent, use_catalog=False)
    if decision_event:
        return decision_event.getEventDate()
