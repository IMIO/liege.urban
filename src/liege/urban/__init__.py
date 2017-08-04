# -*- coding: utf-8 -*-

from zope.i18nmessageid import MessageFactory

import liege.urban.content.genericlicence
# !!! import order matters, always import genericlicence schema changes
# before other licence types schema changes
import liege.urban.content.article127
import liege.urban.content.buildlicence
import liege.urban.content.codt_article127
import liege.urban.content.codt_buildlicence
import liege.urban.content.codt_cu2
import liege.urban.content.codt_integratedlicence
import liege.urban.content.codt_uniquelicence
import liege.urban.content.contact
import liege.urban.content.cu2
import liege.urban.content.integratedlicence
import liege.urban.content.uniquelicence
import liege.urban.content.foldermanager
import liege.urban.content.inquiry_event
import liege.urban.content.inquiry_licence
import liege.urban.content.portion_out
import liege.urban.content.urbanevent
import liege.urban.content.urbanevent_opinionrequest

_ = MessageFactory('liege.urban')


# hide assigned_user and assigned_group fields from task
from collective.task.behaviors import ITask
from plone.directives.form import mode
from zope.interface import Interface
mode_values = ITask._Element__tagged_values.get(mode.key, [])
mode_values.append((Interface, 'assigned_user', 'hidden'))
mode_values.append((Interface, 'assigned_group', 'hidden'))
ITask._Element__tagged_values[mode.key] = mode_values
# END # hide assigned_user and assigned_group fields from task
