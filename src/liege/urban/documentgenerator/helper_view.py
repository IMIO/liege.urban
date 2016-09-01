# -*- coding: utf-8 -*-

from collective.documentgenerator.helper.archetypes import ATDisplayProxyObject


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
        shore_abbr = {
            'right': u'D',
            'left': u'G',
            'center': u'C',
        }
        ref = '{} {}'.format(licence.reference, shore_abbr[licence.shore])
        return ref
