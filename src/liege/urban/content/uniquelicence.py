# -*- coding: utf-8 -*-

from Products.urban.content.licence.UniqueLicence import UniqueLicence

# buildlicence and uniquelicence schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema
from liege.urban.interfaces import IShore

from zope.i18n import translate
from zope.component import queryAdapter


UniqueLicence.schema = update_item_schema(UniqueLicence.schema)


def updateTitle(self):
    """
        Update the title to clearly identify the licence
    """
    if self.getApplicants():
        applicantTitle = self.getApplicants()[0].Title()
    else:
        applicantTitle = translate('no_applicant_defined', 'urban', context=self.REQUEST).encode('utf8')
    to_shore = queryAdapter(self, IShore)
    title = "%s %s - %s - %s - %s" % (self.getReference(), to_shore.display(), self.getReferenceSPE(), self.getLicenceSubject(), applicantTitle)
    self.setTitle(title)
    self.reindexObject(idxs=('Title', 'applicantInfosIndex', 'sortable_title', ))
    return title


UniqueLicence.updateTitle = updateTitle
