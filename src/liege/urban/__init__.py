# -*- coding: utf-8 -*-

from liege.urban.licence_fields_permissions import init_field_permissions

from zope.i18nmessageid import MessageFactory

import liege.urban.content.portion_out
import liege.urban.content.genericlicence

_ = MessageFactory('liege.urban')

init_field_permissions()
