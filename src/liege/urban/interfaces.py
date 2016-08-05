# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.interface import Interface

from zope.publisher.interfaces.browser import IDefaultBrowserLayer


class ILiegeUrbanLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""


class IFDOpinionEvent(Interface):
    """IFDOpinion type marker interface"""
