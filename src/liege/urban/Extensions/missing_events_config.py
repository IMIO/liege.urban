# -*- coding: utf-8 -*-

from Products.urban.interfaces import IGenericLicence
from Products.urban.interfaces import IUrbanEvent

from plone import api


def list_missing_events():
    """
    """
    catalog = api.portal.get_tool('portal_catalog')
    licences = [b.getObject() for b in catalog(object_provides=IGenericLicence.__identifier__)]
    all_broken_events = {}
    for licence in licences:
        broken_events = [obj for obj in licence.objectValues()
                         if IUrbanEvent.providedBy(obj) and not obj.getUrbaneventtypes()]
        for broken_event in broken_events:
            if licence.portal_type not in all_broken_events:
                all_broken_events[licence.portal_type] = {}
            events_by_licence = all_broken_events[licence.portal_type]
            if broken_event.Title() in events_by_licence:
                events_by_licence[broken_event.Title()].append(licence)
            else:
                events_by_licence[broken_event.Title()] = [licence]

    import ipdb; ipdb.set_trace()
