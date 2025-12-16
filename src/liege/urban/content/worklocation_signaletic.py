# -*- coding: utf-8 -*-


from Products.CMFPlone.utils import safe_unicode
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
                zip_code = safe_unicode(address.zip_code)
                city = address.getDivisionAlternativeName()
                city = city and safe_unicode(city.split('(')[0]) or ''
                street = safe_unicode(address.street_name)
                number = safe_unicode(address.street_number)
                separator = safe_unicode(u"à")
                if signaletic:
                    signaletic += safe_unicode(' %s ' % translate('and', 'urban', context=licence.REQUEST))
                if number:
                    signaletic += "%s %s %s %s %s" % (street, number, separator, zip_code, city)
                else:
                    signaletic += "%s - %s %s" % (street, zip_code, city)
            return signaletic
        else:
            return safe_unicode(licence.getDefaultWorkLocationSignaletic())

    def get_street_and_number(self):
        licence = self.licence
        address_points = licence.getParcels()
        if address_points:
            signaletic = ''
            for address in address_points:
                street = safe_unicode(address.street_name)
                number = safe_unicode(address.street_number)
                if number:
                    signaletic = '{} {} {}'.format(signaletic, street, number)
                else:
                    signaletic = '{} {}'.format(signaletic, street)
            return signaletic
        else:
            return safe_unicode(licence.getDefaultStreetAndNumber())
