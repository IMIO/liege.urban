# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory

import liege.urban.content.genericlicence
# !!! import order matters, always import genericlicence schema changes
# before other licence types schema changes
import liege.urban.content.buildlicence
import liege.urban.content.contact
import liege.urban.content.foldermanager
import liege.urban.content.inquiry_event
import liege.urban.content.inquiry_licence
import liege.urban.content.portion_out
import liege.urban.content.urbanevent
import liege.urban.content.urbanevent_opinionrequest

_ = MessageFactory('liege.urban')
