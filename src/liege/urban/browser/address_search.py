# -*- coding: utf-8 -*-

from plone import api
from plone.z3cform.layout import FormWrapper

from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile

from z3c.form import button
from z3c.form import form, field

from zope.interface import Interface
from zope.schema import TextLine
from zope.i18nmessageid import MessageFactory
_ = MessageFactory('hello_world')


class StreetNameField(TextLine):
    """ """


class StreetNumberField(TextLine):
    """ """


class IAddressSearchForm(Interface):

    street_name = StreetNameField(
        title=_(u'Street name'),
        required=False
    )

    street_number = StreetNumberField(
        title=_(u'Street number'),
        required=False
    )


class FieldDefaultValue(object):
    """ """

    def __init__(self, licence, request, form, field, widget):
        self.licence = licence
        self.request = request
        self.form = form
        self.field = field
        self.widget = widget

    def get(self):
        """ To implements."""


class DefaulStreetName(FieldDefaultValue):
    """ """

    def get(self):
        """ """
        location = self.licence.getWorkLocations()
        if not location:
            return ''

        catalog = api.portal.get_tool('portal_catalog')
        street_UID = location[0]['street']
        street_brain = catalog(UID=street_UID)
        default_street = street_brain[0].Title.split('(')[0]

        return default_street


class DefaulStreetNumber(FieldDefaultValue):
    """ """

    def get(self):
        """ """
        location = self.licence.getWorkLocations()
        if not location:
            return ''

        street_number = location[0]['number']

        return street_number


class AddressSearchForm(form.Form):

    fields = field.Fields(IAddressSearchForm)
    ignoreContext = True

    def updateWidgets(self):
        super(AddressSearchForm, self).updateWidgets()

    @button.buttonAndHandler(u'Search')
    def handleSearch(self, action):
        data, errors = self.extractData()
        if errors:
            return False


class AddressSearchFormView(FormWrapper):
    """
    """
    form = AddressSearchForm
    index = ViewPageTemplateFile('templates/address_search.pt')

    def __init__(self, context, request):
        super(AddressSearchFormView, self).__init__(context, request)
        # disable portlets on licences
        self.request.set('disable_plone.rightcolumn', 1)
        self.request.set('disable_plone.leftcolumn', 1)

    def do_search(self):
        """
        """
        form_inputs = self.form_instance.extractData()[0]
        do_search = any(form_inputs.values())
        return do_search
