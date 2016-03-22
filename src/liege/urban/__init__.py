# -*- coding: utf-8 -*-

from liege.urban.licence_fields_permissions import init_field_permissions

from Products.CMFCore.permissions import setDefaultRoles

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('liege.urban')

init_field_permissions()
