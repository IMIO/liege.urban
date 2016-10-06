# -*- coding: utf-8 -*-

from collective.documentgenerator.helper.archetypes import ATDisplayProxyObject

from liege.urban.interfaces import IShore

from zope.component import queryAdapter

from plone import api


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

    def getShore(self):
        licence = self.context
        to_shore = queryAdapter(licence, IShore)
        return to_shore.display()

    def get_work_location_signaletic(self, separator=', '):
        """
        Adresse(s) des travaux (workLocations)
        """
        licence = self.context
        workLocations = licence.getWorkLocations()
        workLocation_signaletic = self._get_work_location_signaletic(workLocations[0])
        for workLocation in workLocations[1:]:
            workLocation_signaletic += separator + self.get_work_location_signaletic(workLocation)
        return workLocation_signaletic

    def _get_work_location_signaletic(self, workLocation):
        catalog = api.portal.get_tool("uid_catalog")
        street = catalog(UID=workLocation['street'])[0].getObject()
        return street.getStreetName() + ' ' +  workLocation['number']

    def get_work_location(self, index):
        """
        return a dictionary containing all work locations informations
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
        licence = self.context
        workLocation = licence.getWorkLocations()[index]
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
