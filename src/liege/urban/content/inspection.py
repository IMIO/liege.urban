# -*- coding: utf-8 -*-

from liege.urban import UrbanMessage as _

from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import StringField

from Products.urban.content.licence.Inspection import Inspection


specific_schema = Schema((
    StringField(
        name='formal_notice_old_reference',
        widget=StringField._properties['widget'](
            size=60,
            label=_('urban_label_formal_notice_old_reference', default='Formal_notice_old_reference'),
        ),
        schemata='urban_description',
    ),
),)


def update_item_schema(baseSchema):
    LicenceSchema = baseSchema + specific_schema.copy()

    # move some fields
    LicenceSchema.moveField('formal_notice_old_reference', after='referenceDGATLP')
    return LicenceSchema


Inspection.schema = update_item_schema(Inspection.schema)
