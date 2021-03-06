# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from Products.urban import UrbanMessage as _
from Products.urban.interfaces import IOpinionRequestEvent

from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from zope.interface import Interface


class ILiegeUrbanLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IAddressFactory(Interface):
    """  """


class IShore(Interface):
    """ """


class IInternalOpinionRequestEvent(IOpinionRequestEvent):
    __doc__ = _("""IInternalOpinionRequestEvent type marker interface""")


class IInspectionBuidlingDivisionAttestationMail(Interface):
    __doc__ = _("""IInspectionBuidlingDivisionAttestationMail type marker interface""")


class IInspectionBuidlingDivisionAttestationCollege(Interface):
    __doc__ = _("""IInspectionBuidlingDivisionAttestationCollege type marker interface""")
