# -*- coding: utf-8 -*-

from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import provider
from zope.interface import Interface
from zope import schema
from liege.urban import UrbanMessage as _
from plone.supermodel import model


@provider(IFormFieldProvider)
class IAddress(model.Schema):

    street_code = schema.TextLine(
        title=_(u"Street code"),
        required=False,
    )

    street_name = schema.TextLine(
        title=_(u"Street name"),
        required=False,
    )

    street_number = schema.TextLine(
        title=_(u"Street number"),
        required=False,
    )

    zip_code = schema.TextLine(
        title=_(u"Zip Code"),
        required=False,
    )

    address_point = schema.Int(
        title=_(u"Address Point"),
        required=False,
    )
