# -*- coding: utf-8 -*-

from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

from Products.urban.browser.licence.licenceview import LicenceView


class LiegeLicenceView(LicenceView):
    """
    Liege licences browser views.
    """

    index = ViewPageTemplateFile("templates/licencetabsmacros.pt")
