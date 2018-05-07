# -*- coding: utf-8 -*-

from liege.urban import UrbanMessage as _
from Products.urban.EnvClassOne import EnvClassOne
from Products.urban.EnvClassThree import EnvClassThree
from Products.urban.EnvClassTwo import EnvClassTwo


def update_base_schema(baseSchema):
    LicenceSchema = baseSchema.copy()

    # hide some fields
    LicenceSchema['folderCategory'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
    LicenceSchema['natura2000'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
    LicenceSchema['natura2000location'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
    LicenceSchema['natura2000Details'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}

    # move road fields schemata
    LicenceSchema['businessDescription'].schemata = 'urban_environment'
    LicenceSchema['pipelines'].schemata = 'urban_environment'
    LicenceSchema['pipelinesDetails'].schemata = 'urban_environment'
    LicenceSchema['sevesoSite'].schemata = 'urban_environment'
    LicenceSchema['natura_2000'].schemata = 'urban_environment'
    LicenceSchema['rubrics'].schemata = 'urban_environment'
    LicenceSchema['rubricsDetails'].schemata = 'urban_environment'
    LicenceSchema['minimumLegalConditions'].schemata = 'urban_environment'
    LicenceSchema['additionalLegalConditions'].schemata = 'urban_environment'
    # show and hide inquiry fields
    LicenceSchema['investigationArticles'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    LicenceSchema['investigationArticlesText'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    LicenceSchema['derogation'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
    LicenceSchema['derogationDetails'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
    LicenceSchema['divergence'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
    LicenceSchema['divergenceDetails'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
    LicenceSchema['investigationReasons'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    LicenceSchema['demandDisplay'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    LicenceSchema['investigationDetails'].widget.visible = {'edit': 'visible', 'view': 'visible'}
    # reorder fields
    LicenceSchema.moveField('rubricsDetails', after='rubrics')
    LicenceSchema.moveField('minimumLegalConditions', after='rubricsDetails')
    LicenceSchema.moveField('additionalLegalConditions', after='minimumLegalConditions')
    LicenceSchema.moveField('businessDescription', after='additionalLegalConditions')
    LicenceSchema.moveField('natura_2000', after='sevesoSite')
    # rename fields
    LicenceSchema['procedureChoice'].widget.label = _('urban_label_procedureType')
    LicenceSchema['workLocations'].widget.label = _('urban_label_exploitationAddress')
    LicenceSchema['folderCategoryTownship'].widget.label = _('urban_label_ExploitationUsage')

    return LicenceSchema

env_base_classes = [
    EnvClassOne, EnvClassThree, EnvClassTwo
]

for licence_class in env_base_classes:
    licence_class.schema = update_base_schema(licence_class.schema)


def update_licences_schema(baseSchema):
    LicenceSchema = baseSchema.copy()

    # hide some fields
    LicenceSchema['isSeveso'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}
    # rename fields
    LicenceSchema['ftSolicitOpinionsTo'].widget.label = _('urban_label_decisionNotificationTo')
    LicenceSchema['commentsOnSPWOpinion'].widget.label = _('urban_label_CommentsOnDecisionProject')

    return LicenceSchema

env_licence_classes = [
    EnvClassOne, EnvClassTwo
]

for licence_class in env_licence_classes:
    licence_class.schema = update_licences_schema(licence_class.schema)
