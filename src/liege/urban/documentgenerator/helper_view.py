# -*- coding: utf-8 -*-

from collective.documentgenerator.helper.archetypes import ATDisplayProxyObject

from liege.urban.interfaces import IShore

from zope.component import queryAdapter


class LiegeLicenceProxyObject(ATDisplayProxyObject):
    """
    Archetypes implementation of DisplayProxyObject.
    """

    @property
    def reference(self):
        """
        Append shore abbreviation to the base reference.
        """
        licence = self.context
        to_shore = queryAdapter(licence, IShore)
        ref = '{} {}'.format(licence.reference, to_shore.display())
        return ref
