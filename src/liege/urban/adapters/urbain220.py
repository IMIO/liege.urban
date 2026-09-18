# -*- coding: utf-8 -*-

from Products.CMFPlone.utils import safe_unicode
from Products.urban.interfaces import IToUrbain220Street
from zope.interface import implements


class LiegeLicenceToUrbain220Street(object):
    """ """

    implements(IToUrbain220Street)

    def __init__(self, licence):
        first_address = None
        for address in (
            licence.listFolderContents(contentFilter={"portal_type": "Parcel"})
        ):
            if address.street_name and address.street_code:
                first_address = address
                break

        self.street_name = first_address and safe_unicode(first_address.street_name)
        self.street_code = first_address and safe_unicode(first_address.street_code)
        self.street_number = first_address and first_address.street_number
