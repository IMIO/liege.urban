from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import StringField
from Products.Archetypes.atapi import SelectionWidget
from Products.Archetypes.public import DisplayList

from Products.urban.PortionOut import PortionOut


def update_item_schema(baseSchema):

    specificSchema = Schema((
        # field for defining label that will be used when the item is in the Council
        # in College, this is a proposal that will be copied to the item sent to Council
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
                    ('right', 'Droite'),
                    ('left', 'Gauche'),
                    ('center', 'Centre'),
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
