# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import Schema

from Products.urban.CODT_UniqueLicence import CODT_UniqueLicence

from liege.urban import UrbanMessage as _
# buildlicence and uniquelicence schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema as base_update_item_schema
from liege.urban.licence_fields_permissions import set_field_permissions

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
    LicenceSchema.moveField('inquiry_category', after='divergenceDetails')
    LicenceSchema.moveField('rubrics', after='folderTendency')
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
    # change permissions of some fields
    LicenceSchema['claimsSynthesis'].read_permission = 'liege.urban: External Reader'
    LicenceSchema['claimsSynthesis'].write_permission = 'Review portal content'
    LicenceSchema['environmentTechnicalAdviceAfterInquiry'].read_permission = 'liege.urban: External Reader'
    LicenceSchema['environmentTechnicalAdviceAfterInquiry'].write_permission = 'Review portal content'

    return LicenceSchema

CODT_UniqueLicence.schema = update_item_schema(base_update_item_schema(CODT_UniqueLicence.schema))

permissions_mapping = {
    'urban_description': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_analysis': ('liege.urban: External Reader', 'liege.urban: Urban Editor'),
    'urban_environment': ('liege.urban: External Reader', 'liege.urban: Environment Editor'),
    'urban_location': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
    'urban_habitation': ('liege.urban: External Reader', 'urban: Add PortionOut'),
}

# claimsSynthesis and environmentTechnicalAdviceAfterInquiry must have reviewer
# write permission to be able to freeze them in the workflow
exceptions = [
    'portal_type', 'claimsSynthesis', 'environmentTechnicalAdviceAfterInquiry'
]

CODT_UniqueLicence.schema = set_field_permissions(
    CODT_UniqueLicence.schema,
    permissions_mapping,
    exceptions,
)
