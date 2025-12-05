# -*- coding: utf-8 -*-

from zope.interface import Interface
from zope import schema
from liege.urban import UrbanMessage as _


class IBank(Interface):
    shore = schema.Choice(
        title=_(u"Bank"),
        required=False,
        vocabulary="liege.shore"
    )
