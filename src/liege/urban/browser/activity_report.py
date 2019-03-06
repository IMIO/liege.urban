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
from liege.urban import UrbanMessage as _

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
            'form_address': self.extract_form_address(licence),
            'subject': licence.getLicenceSubject(),
            'workflow_state': brain.review_state,
            'folder_managers': [self.extract_folder_managers(fm)
                                for fm in licence.getFoldermanagers()],
            'applicants': [self.extract_applicants(obj) for obj in licence.objectValues()
                           if interfaces.IContact.providedBy(obj)],
            'deposit_dates': self.extract_deposit_dates(licence),
            'incomplete_dates': self.extract_incomplete_dates(licence),
            'inquiry_dates': self.extract_inquiry_dates(licence),
            'decision_date': self.extract_decision_date(licence),
            'decision': self.extract_decision(licence),
        }
        if brain.licence_final_duedate and brain.licence_final_duedate.year < 9000:
            licence_dict['due_date'] = str(brain.licence_final_duedate)
        else:
            licence_dict['due_date'] = ''

        if hasattr(licence, 'getLastAcknowledgment'):
            licence_dict['acknowledgement_date'] = licence.getLastAcknowledgment() and str(licence.getLastAcknowledgment().getEventDate()) or ''

        if hasattr(licence, 'getLastLicenceNotification'):
            licence_dict['notification_date'] = licence.getLastLicenceNotification() and str(licence.getLastLicenceNotification().getEventDate()) or ''

        if hasattr(licence, 'getLastRecourse'):
            licence_dict['recourse_date'] = licence.getLastRecourse() and str(licence.getLastRecourse().getEventDate()) or ''

        if hasattr(licence, 'annoncedDelay'):
            licence_dict['delay'] = self.extract_annonced_delay(licence, cfg)

        if hasattr(licence, 'procedureChoice'):
            licence_dict['procedure_choice'] = licence.getProcedureChoice()

        if hasattr(licence, 'workType'):
            licence_dict['worktype_220'] = licence.getWorkType()

        if hasattr(licence, 'folderCategoryTownship'):
            licence_dict['worktype_city'] = self.extract_foldercategory_township(licence, cfg)

        if hasattr(licence, 'habitationsBeforeLicence'):
            licence_dict['habitations_before_licence'] = licence.getHabitationsBeforeLicence() or 0
            licence_dict['habitations_asked'] = licence.getAdditionalHabitationsAsked() or 0
            licence_dict['habitations_authorized'] = licence.getAdditionalHabitationsGiven() or 0

        if hasattr(licence, 'authority'):
            licence_dict['authority'] = self.extract_authority(licence, cfg)

        if hasattr(licence, 'folderTendency'):
            licence_dict['folder_tendency'] = licence.getFolderTendency()

        if hasattr(licence, 'rubrics'):
            licence_dict['rubrics'] = self.extract_rubrics(licence)

        if licence.portal_type == 'EnvClassBordering':
            licence_dict['external_address'] = self.extract_external_address(licence)
            licence_dict['external_parcels'] = self.extract_external_parcels(licence)

        if interfaces.IEnvironmentBase.providedBy(licence):
            licence_dict['authorization_start_date'] = licence.getLastLicenceEffectiveStart() and str(licence.getLastLicenceEffectiveStart().getEventDate()) or ''
            licence_dict['authorization_end_date'] = licence.getLastLicenceExpiration() and str(licence.getLastLicenceExpiration().getEventDate()) or ''
            licence_dict['displaying_date'] = licence.getLastDisplayingTheDecision() and str(licence.getLastDisplayingTheDecision().getEventDate()) or ''
            licence_dict['archives_date'] = licence.getLastSentToArchives() and str(licence.getLastSentToArchives().getEventDate()) or ''
            licence_dict['archives_description'] = licence.getLastSentToArchives() and str(licence.getLastSentToArchives().getEventDate()) or ''
            licence_dict['activity_ended_date'] = licence.getLastActivityEnded() and licence.getLastActivityEnded().description() or ''
            licence_dict['forced_end_date'] = licence.getLastForcedEnd() and str(licence.getLastForcedEnd().getEventDate()) or ''
            licence_dict['modification_registry_date'] = licence.getLastModificationRegistry() and str(licence.getLastModificationRegistry().getEventDate()) or ''
            licence_dict['iile_prescription_date'] = licence.getLastIILEPrescription() and str(licence.getLastIILEPrescription().getEventDate()) or ''
            licence_dict['provocation_date'] = licence.getLastProvocation() and str(licence.getLastProvocation().getEventDate()) or ''

        return licence_dict

    def extract_decision_date(self, licence):
        decision_event = self._get_decision_event(licence)
        decision_date = decision_event and decision_event.getDecisionDate() or ''
        decision_date = decision_date and str(decision_date) or ''
        return decision_date

    def extract_decision(self, licence):
        decision_event = self._get_decision_event(licence)
        decision = decision_event and decision_event.getDecision() or ''
        decision = decision and str(decision) or ''
        return decision

    def _get_decision_event(self, licence):
        if interfaces.IEnvironmentBase.providedBy(licence):
            decision_event = licence.getLastLicenceDelivery()
        else:
            decision_event = licence.getLastTheLicence()
        return decision_event

    def extract_annonced_delay(self, licence, cfg):
        delay = ''
        if licence.getAnnoncedDelay() and any(licence.getAnnoncedDelay()):
            raw_delay = licence.getAnnoncedDelay()
            vocterm = hasattr(cfg, 'folderdelays') and cfg.folderdelays.get(licence.getAnnoncedDelay()) or None
            if not vocterm:
                match = re.match('(\d+)j', raw_delay)
                delay = match and match.groups()[0] or ''
            else:
                delay = vocterm.getDeadLineDelay()
        return delay

    def extract_foldercategory_township(self, licence, cfg):
        if licence.getFolderCategoryTownship():
            term = cfg.townshipfoldercategories.get(licence.getFolderCategoryTownship())
            worktypes = []
            if term:
                match = re.match('(.*)\((.*)\)', term.Title())
                if match:
                    code, label = match.groups()
                    worktypes.append({'code': code, 'label': label})
                else:
                    worktypes.append({'code': '', 'label': term.Title()})
            return worktypes
        else:
            return []

    def extract_authority(self, licence, cfg):
        if licence.getAuthority():
            term = cfg.authority.get(licence.getAuthority())
            if term:
                return term.Title()
        return ''

    def extract_rubrics(self, licence):
        rubrics = []
        for rubric in licence.getRubrics():
            rubric = {
                'num': rubric.id,
                'class': rubric.getExtraValue(),
                'description': rubric.description(),
            }
            rubrics.append(rubric)
        return rubrics

    def extract_address(self, address):
        address_dict = {
            'street_name': address.getStreet_name(),
            'street_number': address.getStreet_number(),
            'street_code': address.getStreet_code(),
            'zipe_code': address.getZip_code(),
            'address_point': address.getAddress_point(),
            'shore': address.getShore(),
        }
        try:
            capakey = address.get_capakey()
        except:
            capakey = ''
        address_dict['capakey'] = capakey
        return address_dict

    def extract_external_address(self, licence):
        addresses_dict = []
        for address in licence.getWorkLocations():
            address_dict = {
                'street_name': address['street'],
                'street_number': address['number'],
                'zipe_code': licence.getZipcode(),
                'city': licence.getCity(),
            }
            addresses_dict.append(address_dict)
        return addresses_dict

    def extract_external_parcels(self, licence):
        parcels_dict = []
        for parcel in licence.getManualParcels():
            parcel_dict = {
                'parcel': parcel['ref'],
                'capakey': parcel['capakey'],
            }
            parcels_dict.append(parcel_dict)
        return parcels_dict

    def extract_form_address(self, licence):
        catalog = api.portal.get_tool('portal_catalog')
        addresses_dict = []
        for address in licence.getWorkLocations():
            street_brain = catalog(UID=address['street'])
            street = street_brain and street_brain[0].getObject() or None
            address_dict = {
                'street_name': street and street.getStreetName() or '',
                'street_code': street and street.getStreetCode() or '',
                'street_number': address['number'],
            }
            addresses_dict.append(address_dict)
        return addresses_dict

    def extract_folder_managers(self, folder_manager):
        fm_dict = {
            'firstname': folder_manager.getName2(),
            'lastname': folder_manager.getName1(),
        }
        return fm_dict

    def extract_applicants(self, applicant_obj):
        applicant = {
            'firstname': applicant_obj.getName2(),
            'lastname': applicant_obj.getName1(),
            'street': applicant_obj.getStreet(),
            'number': applicant_obj.getNumber(),
            'zipe_code': applicant_obj.getZipcode(),
            'city': applicant_obj.getCity(),
            'country': applicant_obj.getCountry(),
            'phone': applicant_obj.getPhone(),
        }
        if not applicant['firstname'] and not applicant['lastname']:
            if hasattr(applicant_obj, 'denomination'):
                applicant['lastname'] = applicant_obj.getDenomination()
            if hasattr(applicant_obj, 'legalForm'):
                applicant['firstname'] = applicant_obj.getLegalForm()
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
