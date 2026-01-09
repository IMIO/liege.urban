# -*- coding: utf-8 -*-

from Acquisition import aq_inner
from Products.urban.browser.licence.licenceview import LicenceView
from plone import api
from zope.i18n import translate


class LiegeLicenceView(LicenceView):

    def getKeyDates(self):
        context = aq_inner(self.context)
        urban_tool = api.portal.get_tool("portal_urban")
        with_empty_dates = urban_tool.getDisplayEmptyKeyDates()
        config = context.getLicenceConfig()
        ordered_dates = []
        key_dates = {}
        dates = {}

        # search in the config for all the Key eventconfigs and their key dates
        for eventconfig in config.eventconfigs.objectValues():
            if eventconfig.getIsKeyEvent():
                keydates = [
                    (
                        date,
                        date == "eventDate"
                        and eventconfig.getEventDateLabel()
                        or translate(
                            "urban_label_" + date,
                            "urban",
                            default=date,
                            context=self.request,
                        ),
                    )
                    for date in eventconfig.getKeyDates()
                ]
                ordered_dates.append((eventconfig.UID(), eventconfig.getKeyDates()))
                key_dates[eventconfig.UID()] = keydates
                dates[eventconfig.UID()] = dict(
                    [
                        (
                            date[0],
                            {
                                "dates": [],
                                "label": date[0] == "eventDate"
                                and eventconfig.Title()
                                or "%s (%s)"
                                % (eventconfig.Title().decode("utf8"), date[1]),
                            },
                        )
                        for date in keydates
                    ]
                )
        for event in context.getAllEvents():
            eventconfig_uid = event.getUrbaneventtypes().UID()
            if eventconfig_uid in dates.keys() and not dates[eventconfig_uid].get(
                "url", ""
            ):
                for date in key_dates[eventconfig_uid]:
                    date_value = getattr(event, date[0])
                    if with_empty_dates or date_value:
                        dates[eventconfig_uid][date[0]]["dates"].append(
                            {
                                "url": event.absolute_url(),
                                "date": date_value
                                and urban_tool.formatDate(
                                    date_value, translatemonth=False
                                )
                                or None,
                            }
                        )

        # flatten the result to a list before returning it
        dates_list = []
        for uid, date_names in ordered_dates:
            for date in date_names:
                date_value = dates[uid].get(date, None)
                if date_value["dates"] or with_empty_dates:
                    dates_list.append(date_value)

        return dates_list
