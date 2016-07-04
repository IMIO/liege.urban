# -*- coding: utf-8 -*-

from collective.documentgenerator.helper.archetypes import ATDocumentGenerationHelperView


class LiegeDocumentHelperView(ATDocumentGenerationHelperView):
    """
    Liege implementation of document generation helper methods.
    """

    def get_division(self):
        """
        """
        parcels = self.context.getParcels()
        parcel_view = parcels and parcels[0].restrictedTraverse('document_generation_helper_view')
        raw_div = parcel_view.context.division
        division = raw_div and raw_div[raw_div.find('(') + 1:-1] or 'DIVISION INCONNUE'
        return division

    def reference(self):
        """
        Append shore abbreviation to the base reference.
        """
        licence = self.real_context
        shore_abbr = {
            'right': u'D',
            'left': u'G',
            'center': u'C',
        }
        ref = '{} {}'.format(licence.reference, shore_abbr[licence.shore])
        return ref
