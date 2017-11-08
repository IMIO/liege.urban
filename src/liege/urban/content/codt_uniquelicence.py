# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import Schema

from Products.urban.CODT_UniqueLicence import CODT_UniqueLicence

# buildlicence and uniquelicence schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema as base_update_item_schema

specific_schema = Schema((
),)


def update_item_schema(baseSchema):
    LicenceSchema = baseSchema + specific_schema.copy()

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

    # rename some fields
    LicenceSchema['reference'].widget.label_msgid = 'urban_label_urbanReference'
    LicenceSchema['referenceDGATLP'].widget.label_msgid = 'urban_label_referenceFD'

    return LicenceSchema

CODT_UniqueLicence.schema = update_item_schema(base_update_item_schema(CODT_UniqueLicence.schema))


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
