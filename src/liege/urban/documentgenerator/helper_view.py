# -*- coding: utf-8 -*-

from liege.urban.interfaces import IShore

from plone import api

from Products.urban.docgen.helper_view import EventDisplayProxyObject
from Products.urban.docgen.helper_view import LicenceDisplayProxyObject
from Products.urban.interfaces import IEnvironmentBase

from zope.component import queryAdapter


class LiegeLicenceProxyObject(LicenceDisplayProxyObject):
    """
    Archetypes implementation of DisplayProxyObject.
    """

    def authorized(self):
        return self.context.workflow_history['buildlicence_workflow'][-1]['review_state'] == 'authorized'

    def getShore(self):
        licence = self.context
        to_shore = queryAdapter(licence, IShore)
        return to_shore.display()

    @property
    def reference(self):
        """
        Append shore abbreviation to the base reference.
        """
        licence = self.context
        if IEnvironmentBase.providedBy(licence):
            return licence.reference
        to_shore = queryAdapter(licence, IShore)
        ref = '{} {}'.format(licence.reference, to_shore.display())
        return ref

    def get_first_folder_manager(self, group='', grade=''):
        """
        """
        groups_mapping = {
            'urban': [
                'administrative_editors',
                'administrative_validators',
                'technical_editors',
                'technical_validators'
            ],
            'environment': [
                'administrative_editors_environment',
                'administrative_validators_environment',
                'technical_editors_environment',
                'technical_validators_environment'
            ],
            'inspection': [
                'inspection_editors',
                'inspection_validators',
            ],
        }
        folder_managers = [fm for fm in self.getFoldermanagers() if not grade or fm.getGrade() == grade]
        for folder_manager in folder_managers:
            if group:
                groups = set([g.id for g in api.group.get_groups(username=folder_manager.getPloneUserId())])
                if groups.intersection(groups_mapping.get(group, set())):
                    fm_proxy = folder_manager.restrictedTraverse('@@document_generation_helper_view').context
                    return fm_proxy

            else:
                fm_proxy = folder_manager.restrictedTraverse('@@document_generation_helper_view').context
                return fm_proxy


class LiegeEventProxyObject(EventDisplayProxyObject):
    """
    """

    def get_wspm_detailedDescription_text(self, style='UrbanBody'):
        field_name = 'detailedDescription'
        description_text = self._get_wspm_field(field_name)
        if description_text != 'NO FIELD {} FOUND'.format(field_name):
            description_text = self.helper_view.xhtml(description_text, style)
        return description_text

    def get_wspm_motivation_text(self, style='UrbanBody'):
        field_name = 'motivation'
        motivation_text = self._get_wspm_field(field_name)
        if motivation_text != 'NO FIELD {} FOUND'.format(field_name):
            motivation_text = self.helper_view.xhtml(motivation_text, style)
        return motivation_text

    def get_wspm_decisionSuite_text(self, style='UrbanBody'):
        field_name = 'decisionSuite'
        decision_text = self._get_wspm_field(field_name)
        if decision_text != 'NO FIELD {} FOUND'.format(field_name):
            decision_text = self.helper_view.xhtml(decision_text, style)
        return decision_text

    def get_wspm_decisionEnd_text(self, style='UrbanBody'):
        field_name = 'decisionEnd'
        decision_text = self._get_wspm_field(field_name)
        if decision_text != 'NO FIELD {} FOUND'.format(field_name):
            decision_text = self.helper_view.xhtml(decision_text, style)
        return decision_text

    def get_wspm_observations_text(self, style='UrbanBody'):
        field_name = 'observations'
        observations_text = self._get_wspm_field(field_name)
        if observations_text != 'NO FIELD {} FOUND'.format(field_name):
            observations_text = self.helper_view.xhtml(observations_text, style)
        return observations_text
