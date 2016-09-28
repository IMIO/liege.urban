# -*- coding: utf-8 -*-

from liege.urban.interfaces import IAddressFactory

from plone import api

from Products.Five import BrowserView
from Products.urban.services import cadastre

from zope.interface import implements

NOT_FOUND = []


class AdressFactory(BrowserView):
    """
    """
    implements(IAddressFactory)

    def __call__(self):
        address_args = self.get_address_args()
        if address_args:
            self.create_address(**address_args)

        return self.request.response.redirect(self.request['HTTP_REFERER'])

    def get_address_args(self):
        args = {}
        for key in ['address_point', 'street_code', 'street_name', 'street_number', 'zip_code', 'capakey', 'shore']:
            val = self.request.get(key, NOT_FOUND)
            if val is NOT_FOUND:
                return NOT_FOUND
            args[key] = val
        return args

    def create_address(self, **address_args):
        session = cadastre.new_session()
        parcel = session.query_parcel_by_capakey(address_args.pop('capakey'))
        licence = self.context
        portal_urban = api.portal.get_tool('portal_urban')

        with api.env.adopt_roles(['Manager']):
            portal_urban.createPortionOut(licence, **parcel.reference_as_dict())

        address = licence.getParcels()[-1]
        for field_name, value in address_args.iteritems():
            field = address.getField(field_name)
            field.set(address, value)

        licence.updateTitle()
