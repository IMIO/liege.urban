# -*- coding: utf-8 -*-

from Products.urban.EnvClassOne import EnvClassOne
from Products.urban.EnvClassThree import EnvClassThree
from Products.urban.EnvClassTwo import EnvClassTwo


def update_item_schema(baseSchema):
    LicenceSchema = baseSchema.copy()

    # hide some fields
    LicenceSchema['folderCategory'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}

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
    LicenceSchema['procedureChoice'].widget.label_msgid = 'urban_label_procedureType'

    return LicenceSchema

licence_classes = [
    EnvClassOne, EnvClassThree, EnvClassTwo
]

for licence_class in licence_classes:
    licence_class.schema = update_item_schema(licence_class.schema)
