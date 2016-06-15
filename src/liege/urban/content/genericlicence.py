# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import StringField
from Products.Archetypes.atapi import SelectionWidget
from Products.Archetypes.public import DisplayList

from Products.urban.BuildLicence import BuildLicence


def update_item_schema(baseSchema):

    specificSchema = Schema((
        StringField(
            name='shore',
            widget=SelectionWidget(
                format='select',
                label='Shore',
                label_msgid='urban_label_Shore',
                i18n_domain='urban',
            ),
            schemata='urban_description',
            optional=True,
            vocabulary=DisplayList(
                (
                    ('right', 'Droite'),
                    ('left', 'Gauche'),
                    ('center', 'Centre'),
                )
            ),
        ),
    ),)

    BuildLicenceSchema = baseSchema + specificSchema.copy()

    return BuildLicenceSchema


BuildLicence.schema = update_item_schema(BuildLicence.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
