# -*- coding: utf-8 -*-

from liege.urban.content.genericlicence import updateTitle as base_updateTitle

from Products.urban.content.licence.EnvClassBordering import EnvClassBordering
from Products.CMFPlone.utils import safe_unicode


def updateTitle(self):
    """
        Update the title to clearly identify the licence
    """
    base_title = base_updateTitle(self)
    streets = u", ".join([safe_unicode(wl["street"]) for wl in self.getWorkLocations()])
    title = u"{} - {}".format(base_title, streets)
    self.setTitle(title)
    self.reindexObject(idxs=("Title", "applicantInfosIndex", "sortable_title", ))
    return title


EnvClassBordering.updateTitle = updateTitle
