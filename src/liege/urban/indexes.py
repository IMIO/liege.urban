# -*- coding: utf-8 -*-

from Products.urban.interfaces import IGenericLicence

from plone.indexer import indexer


@indexer(IGenericLicence)
def genericlicence_shore_index(licence):
    """
    Index Liège shore value
    """
    shore = licence.getShore()
    return [shore]
