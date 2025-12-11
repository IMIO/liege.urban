# -*- coding: utf-8 -*-

from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import provider
from zope.interface import Interface
from zope import schema
from liege.urban import UrbanMessage as _
from plone.supermodel import model


@provider(IFormFieldProvider)
class IBank(model.Schema):
    shore = schema.Choice(
        title=_(u"Bank"),
        required=False,
        vocabulary="liege.shore"
    )
