# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import Schema

from Products.urban.content.licence.CODT_IntegratedLicence import CODT_IntegratedLicence
from Products.urban.content.licence.UniqueLicence import updateTitle

from liege.urban import UrbanMessage as _
# buildlicence and integratedlicence schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema as base_update_item_schema


specific_schema = Schema((
),)


def update_item_schema(baseSchema):
    LicenceSchema = baseSchema + specific_schema.copy()

    # move some fields
    LicenceSchema['pipelines'].schemata = 'urban_environment'
    LicenceSchema['pipelinesDetails'].schemata = 'urban_environment'
    LicenceSchema['procedureChoice'].schemata = 'urban_description'
    LicenceSchema['annoncedDelay'].schemata = 'urban_description'
    LicenceSchema['annoncedDelayDetails'].schemata = 'urban_description'
    LicenceSchema['prorogation'].schemata = 'urban_description'
    # show and hide inquiry fields
    LicenceSchema['inquiry_type'].widget.visible = {'view': 'invisible', 'edit': 'invisible'}
    LicenceSchema['investigationArticles'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    LicenceSchema['investigationArticlesText'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    LicenceSchema['derogationDetails'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    LicenceSchema['investigationReasons'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    LicenceSchema['demandDisplay'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    LicenceSchema['investigationDetails'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    # reorder fields
    LicenceSchema.moveField('folderTendency', after='licenceSubject')
    LicenceSchema.moveField('inquiry_category', after='divergenceDetails')
    LicenceSchema.moveField('rubricsDetails', after='rubrics')
    LicenceSchema.moveField('minimumLegalConditions', after='rubricsDetails')
    LicenceSchema.moveField('additionalLegalConditions', after='minimumLegalConditions')
    LicenceSchema.moveField('description', after='ftSolicitOpinionsTo')
    LicenceSchema.moveField('procedureChoice', after='folderCategory')
    LicenceSchema.moveField('annoncedDelay', after='procedureChoice')
    LicenceSchema.moveField('annoncedDelayDetails', after='annoncedDelay')
    LicenceSchema.moveField('prorogation', after='annoncedDelayDetails')
    # rename some fields
    LicenceSchema['reference'].widget.label = _('urban_label_urbanReference')
    LicenceSchema['referenceDGATLP'].widget.label = _('urban_label_referenceFD')
    LicenceSchema['procedureChoice'].widget.label = _('urban_label_folderCategory')
    LicenceSchema['commentsOnSPWOpinion'].widget.label = _('urban_label_CommentsOnDecisionProject')
    LicenceSchema['ftSolicitOpinionsTo'].widget.label = _('urban_label_decisionNotificationTo')

    return LicenceSchema


CODT_IntegratedLicence.schema = update_item_schema(base_update_item_schema(CODT_IntegratedLicence.schema))


CODT_IntegratedLicence.updateTitle = updateTitle
