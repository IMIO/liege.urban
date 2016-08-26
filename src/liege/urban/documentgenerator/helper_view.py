# -*- coding: utf-8 -*-

from collective.documentgenerator.helper.archetypes import ATDisplayProxyObject
from collective.documentgenerator.helper.archetypes import ATDocumentGenerationHelperView
from plone import api


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

    def get_work_location(self, index):
        """
        return a dictionary whithin all work'location infos
        """
        work_location = {
                'bestAddressKey': '',
                'streetCode': '',
                'streetName': '',
                'startDate': '',
                'endDate': '',
                'regionalRoad': '',
                'number': '',
        }
        workLocation = self.context.getWorkLocations()[index]
        catalog = api.portal.get_tool("uid_catalog")
        street = catalog(UID=workLocation['street'])[0].getObject()
        work_location['bestAddressKey'] = street.getBestAddressKey()
        work_location['streetCode'] = street.getStreetCode()
        work_location['streetName'] = street.getStreetName()
        work_location['startDate'] = street.getStartDate()
        work_location['endDate'] = street.getEndDate()
        work_location['regionalRoad'] = street.getRegionalRoad()
        work_location['number'] =  workLocation['number']
        return work_location

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
