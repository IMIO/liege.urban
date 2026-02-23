# -*- coding: utf-8 -*-

from liege.urban import UrbanMessage as _
from plone.autoform.interfaces import IFormFieldProvider
from plone.supermodel import model
from zope import schema
from zope.interface import provider


@provider(IFormFieldProvider)
class IBank(model.Schema):
    shore = schema.Choice(
        title=_(u"Bank"),
        required=False,
        vocabulary="liege.shore"
    )
