# -*- coding: utf-8 -*-

from liege.urban.interfaces import IShore

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
        }
        for folder_manager in self.getFoldermanagers():
            if folder_manager.getGrade() == grade:
               groups = set([g.id for g in api.group.get_groups(username=folder_manager.getPloneUserId())])
               if groups_mapping.get(group, None) and groups.intersection(groups_mapping.get(group)):
                   return folder_manager

