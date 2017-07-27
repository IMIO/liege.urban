# -*- coding: utf-8 -*-

from liege.urban.interfaces import IShore

from Products.CMFCore.utils import getToolByName
from Products.urban.docgen.helper_view import LicenceDisplayProxyObject

from zope.component import queryAdapter


class LiegeLicenceProxyObject(LicenceDisplayProxyObject):
    """
    Archetypes implementation of DisplayProxyObject.
    """

    def authorized(self):
        return self.context.workflow_history['buildlicence_workflow'][-1]['review_state'] == 'authorized'

    def getShore(self):
        licence = self.context
        to_shore = queryAdapter(licence, IShore)
        return to_shore.display()

    @property
    def reference(self):
        """
        Append shore abbreviation to the base reference.
        """
        licence = self.context
        to_shore = queryAdapter(licence, IShore)
        ref = '{} {}'.format(licence.reference, to_shore.display())
        return ref
