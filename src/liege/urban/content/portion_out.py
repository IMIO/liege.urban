# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import IntegerField
from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import StringField
from Products.Archetypes.atapi import SelectionWidget
from Products.Archetypes.public import DisplayList

from Products.urban.PortionOut import PortionOut


def update_item_schema(baseSchema):

    specificSchema = Schema((
        StringField(
            name='street_code',
            widget=StringField._properties['widget'](
                visible={'edit': 'visible', 'view': 'hidden'},
                label='Street_code',
                label_msgid='urban_label_street_code',
                i18n_domain='urban',
            ),
        ),
        StringField(
            name='street_name',
            widget=StringField._properties['widget'](
                visible={'edit': 'visible', 'view': 'visible'},
                label='Street_name',
                label_msgid='urban_label_street_name',
                i18n_domain='urban',
            ),
        ),
        StringField(
            name='street_number',
            widget=StringField._properties['widget'](
                visible={'edit': 'visible', 'view': 'visible'},
                label='Street_number',
                label_msgid='urban_label_street_number',
                i18n_domain='urban',
            ),
        ),
        StringField(
            name='zip_code',
            widget=StringField._properties['widget'](
                visible={'edit': 'visible', 'view': 'visible'},
                label='Zip_code',
                label_msgid='urban_label_zip_code',
                i18n_domain='urban',
            ),
        ),
        IntegerField(
            name='address_point',
            widget=IntegerField._properties['widget'](
                visible={'edit': 'visible', 'view': 'visible'},
                label='Address_point',
                label_msgid='urban_label_address_point',
                i18n_domain='urban',
            ),
        ),
        StringField(
            name='shore',
            widget=SelectionWidget(
                format='select',
                label='Shore',
                label_msgid='urban_label_Shore',
                i18n_domain='urban',
            ),
            optional=True,
            vocabulary=DisplayList(
                (
                    ('D', 'Droite'),
                    ('G', 'Gauche'),
                    ('C', 'Centre'),
                )
            ),
        ),
    ),)

    PortionOutSchema = baseSchema + specificSchema.copy()

    return PortionOutSchema


PortionOut.schema = update_item_schema(PortionOut.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
