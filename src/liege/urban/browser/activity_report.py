# -*- coding: utf-8 -*-

from plone import api
from plone.z3cform.layout import FormWrapper

from Products.urban import interfaces

from z3c.form import button
from z3c.form import form, field
from z3c.form.browser.checkbox import CheckBoxFieldWidget

from zope import schema
from zope.browserpage.viewpagetemplatefile import ViewPageTemplateFile
from zope.interface import Interface
from liege.urban import _

import json
import re


class ILicencesExtractForm(Interface):

    start_date = schema.Date(
        title=_(u'Date start'),
        required=False,
    )

    end_date = schema.Date(
        title=_(u'Date end'),
        required=False,
    )

    date_index = schema.Choice(
        title=_(u'Date index'),
        vocabulary='urban.vocabularies.licence_date_indexes',
        default='created',
        required=False,
    )

    licence_type = schema.Set(
        title=_(u'Licence types'),
        value_type=schema.Choice(source='urban.vocabularies.licence_types'),
        required=False,
    )


class LicencesExtractForm(form.Form):

    method = 'get'
    fields = field.Fields(ILicencesExtractForm)
    ignoreContext = True

    fields['licence_type'].widgetFactory = CheckBoxFieldWidget

    def updateWidgets(self):
        super(LicencesExtractForm, self).updateWidgets()

    def render(self):
        if hasattr(self, 'result'):
            result = self.result
            delattr(self, 'result')
            return result
        else:
            return super(LicencesExtractForm, self).render()

    @button.buttonAndHandler(u'Search')
    def handleSearch(self, action):
        data, errors = self.extractData()
        if errors:
            return False
        licences = self.query_licences(**data)
        licences_dict = self.compute_json(licences)
        licences_json = json.dumps(licences_dict)
        response = self.context.REQUEST.RESPONSE
        response.setHeader('Content-type', 'application/json')
        response.setHeader('Content-disposition', 'report.json')
        response.setBody(licences_json)
        self.result = licences_json
        return licences_json

    def query_licences(self, start_date, end_date, date_index='created', licence_type=[]):
        catalog = api.portal.get_tool('portal_catalog')
        query = {'portal_type': list(licence_type)}
        query[date_index] = {'query': (start_date, end_date), 'range': 'min:max'}
        licence_brains = catalog(**query)
        licences = [(br, br.getObject()) for br in licence_brains]
        return licences

    def compute_json(self, licences):
        licences_dict = [self.extract_licence_dict(*licence) for licence in licences]
        return licences_dict

    def extract_licence_dict(self, brain, licence):
        cfg = licence.getUrbanConfig()
        licence_dict = {
            'portal_type': brain.portal_type,
            'reference': brain.getReference,
            'address': [self.extract_address(addr) for addr in licence.getParcels()],
            'subject': licence.getLicenceSubject(),
            'workflow_state': brain.review_state,
            'folder_managers': [self.extract_folder_managers(fm)
                                for fm in licence.getFoldermanagers()],
            'applicants': [self.extract_applicants(obj) for obj in licence.objectValues()
                           if interfaces.IContact.providedBy(obj)],
            'deposit_dates': self.extract_deposit_dates(licence),
            'incomplete_dates': self.extract_incomplete_dates(licence),
            'acknowledgement_date': licence.getLastAcknowledgment() and str(licence.getLastAcknowledgment().getEventDate()) or '',
            'inquiry_dates': self.extract_inquiry_dates(licence),
            'decision_date': licence.getLastTheLicence() and str(licence.getLastTheLicence().getDecisionDate()) or '',
            'decision': licence.getLastTheLicence() and licence.getLastTheLicence().getDecision() or '',
            'notification_date': licence.getLastLicenceNotification() and str(licence.getLastLicenceNotification().getEventDate()) or '',
        }
        if brain.licence_final_duedate and brain.licence_final_duedate.year < 9000:
            licence_dict['due_date'] = str(brain.licence_final_duedate)
        else:
            licence_dict['due_date'] = ''

        if hasattr(licence, 'annoncedDelay'):
            if licence.getAnnoncedDelay():
                raw_delay = licence.getAnnoncedDelay()
                vocterm = cfg.folderdelays.get(licence.getAnnoncedDelay())
                if not vocterm:
                    match = re.match('\d+j', raw_delay)
                    licence_dict['delay'] = match and match.groups()[0] or ''
                else:
                    licence_dict['delay'] = vocterm.getDeadLineDelay()
            else:
                licence_dict['delay'] = ''

        if hasattr(licence, 'procedureChoice'):
            licence_dict['procedure_choice'] = licence.getProcedureChoice()

        if hasattr(licence, 'workType'):
            licence_dict['worktype_220'] = licence.getWorkType()

        if hasattr(licence, 'folderCategoryTownship'):
            licence_dict['worktype_city'] = self.extract_foldercategory_township(licence, cfg)

        return licence_dict

    def extract_foldercategory_township(self, licence, cfg):
        if licence.getFolderCategoryTownship():
            vocterms = [cfg.townshipfoldercategories.get(val) for val in licence.getFolderCategoryTownship()]
            worktypes = []
            for term in vocterms:
                if term:
                    code, label = re.match('(.*)\((.*)\)', term.Title()).groups()
                    worktypes.append({'code': code, 'label': label})
            return worktypes
        else:
            return []

    def extract_address(self, address):
        address_dict = {
            'street_name': address.getStreet_name(),
            'street_number': address.getStreet_number(),
            'street_code': address.getStreet_code(),
            'zipe_code': address.getZip_code(),
            'capakey': address.get_capakey(),
            'address_point': address.getAddress_point(),
            'shore': address.getShore(),
        }
        return address_dict

    def extract_folder_managers(self, folder_manager):
        fm_dict = {
            'firstname': folder_manager.getName2(),
            'lastname': folder_manager.getName1(),
        }
        return fm_dict

    def extract_applicants(self, applicant):
        applicant = {
            'firstname': applicant.getName2(),
            'lastname': applicant.getName1(),
            'street': applicant.getStreet(),
            'number': applicant.getNumber(),
            'zipe_code': applicant.getZipcode(),
            'city': applicant.getCity(),
            'country': applicant.getCountry(),
            'phone': applicant.getPhone(),
        }
        return applicant

    def extract_deposit_dates(self, licence):
        deposits = licence.getAllEvents(interfaces.IDepositEvent)
        dates = [str(event.getEventDate()) for event in deposits]
        return dates

    def extract_incomplete_dates(self, licence):
        deposits = licence.getAllEvents(interfaces.IMissingPartEvent)
        dates = [str(event.getEventDate()) for event in deposits]
        return dates

    def extract_inquiry_dates(self, licence):
        inquiries = licence.getAllEvents(interfaces.IInquiryEvent)
        announcements = licence.getAllEvents(interfaces.IAnnouncementEvent)
        all_inquiries = inquiries + announcements
        dates = [{'start_date': str(inq.getInvestigationStart()), 'end_date': str(inq.getInvestigationEnd())} for inq in all_inquiries]
        return dates


class LicencesExtractFormView(FormWrapper):
    """
    """
    form = LicencesExtractForm
    index = ViewPageTemplateFile('templates/activity_report.pt')

    def __init__(self, context, request):
        super(LicencesExtractFormView, self).__init__(context, request)
        # disable portlets on licences
        self.request.set('disable_plone.rightcolumn', 1)
        self.request.set('disable_plone.leftcolumn', 1)
