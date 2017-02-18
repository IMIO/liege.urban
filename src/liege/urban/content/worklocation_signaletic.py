# -*- coding: utf-8 -*-


from Products.urban.interfaces import IWorklocationSignaletic

from zope.i18n import translate
from zope.interface import implements


class LiegeLicenceToWorklocationsSignaletic(object):
    """ """
    implements(IWorklocationSignaletic)

    def __init__(self, licence):
        self.licence = licence

    def get_signaletic(self):
        licence = self.licence
        address_points = licence.getParcels()
        if address_points:
            signaletic = ''
            for address in address_points:
                zip_code = address.getZip_code()
                city = address.getDivisionAlternativeName()
                city = city and city.split('(')[0].encode('utf-8') or ''
                street = address.getStreet_name()
                number = address.getStreet_number()
                if signaletic:
                    signaletic += ' %s ' % translate('and', 'urban', context=self.REQUEST).encode('utf8')
                if number:
                    signaletic += "%s %s à %s %s" % (street, number, zip_code, city)
                else:
                    signaletic += "%s - %s %s" % (street, zip_code, city)
            return signaletic
        else:
            return licence.getDefaultWorkLocationSignaletic()
