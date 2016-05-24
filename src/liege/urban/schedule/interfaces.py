# -*- coding: utf-8 -*-

from zope.interface import Interface


class ICreateOpinionRequestsTask(Interface):
    """ Marker interface for opinion requests creation task."""


class ISendOpinionRequestsTask(Interface):
    """ Marker interface for opinion requests sending task."""
