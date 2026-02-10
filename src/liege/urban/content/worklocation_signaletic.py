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

    def get_number(self, address):
        number = address.street_number
        number = number and safe_unicode(number) or u""
        if isinstance(number, int):
            number = str(number)
        number = number and number.encode("utf-8") or ""
        return number

    def get_zip_code(self, address):
        zip_code = address.zip_code
        zip_code = zip_code and safe_unicode(zip_code) or u""
        if isinstance(zip_code, int):
            zip_code = str(zip_code)
        zip_code = zip_code and zip_code.encode("utf-8") or ""
        return zip_code

    def get_street(self, address):
        street = address.street_name
        street = safe_unicode(street)
        return street and street.encode("utf-8") or ""

    def get_signaletic(self):
        licence = self.licence
        address_points = licence.getParcels()
        if address_points:
            signaletic = ''
            for address in address_points:
                zip_code = self.get_zip_code(address)
                city = address.getDivisionAlternativeName()
                city = city and safe_unicode(city.split('(')[0]).encode("utf-8") or ''
                street = self.get_street(address)
                number = self.get_number(address)
                separator = safe_unicode(u"à").encode("utf-8")
                if signaletic:
                    signaletic += safe_unicode(' %s ' % translate('and', 'urban', context=licence.REQUEST)).encode("utf-8")
                if number:
                    signaletic += "%s %s %s %s %s" % (street, number, separator, zip_code, city)
                else:
                    signaletic += "%s - %s %s" % (street, zip_code, city)
            return signaletic
        else:
            return safe_unicode(licence.getDefaultWorkLocationSignaletic()).encode("utf-8")

    def get_street_and_number(self):
        licence = self.licence
        address_points = licence.getParcels()
        if address_points:
            signaletic = ''
            for address in address_points:
                street = self.get_street(address)
                number = self.get_number(address)
                if number:
                    signaletic = '{} {} {}'.format(signaletic, street, number)
                else:
                    signaletic = '{} {}'.format(signaletic, street)
            return signaletic
        else:
            return safe_unicode(licence.getDefaultStreetAndNumber()).encode("utf-8")
