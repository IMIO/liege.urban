# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import StringField
from Products.Archetypes.public import DisplayList

from Products.MasterSelectWidget.MasterSelectWidget import MasterSelectWidget

from Products.urban.BuildLicence import BuildLicence


slave_fields_composition = (
    {
        'name': 'locationMissingParts',
        'action': 'vocabulary',
        'vocab_method': 'getCompositionMissingParts',
        'control_param': 'composition',
    },
)


def update_item_schema(baseSchema):

    specificSchema = Schema((
        StringField(
            name='composition',
            widget=MasterSelectWidget(
                slave_fields=slave_fields_composition,
                label='Composition',
                label_msgid='urban_label_composition',
                i18n_domain='urban',
            ),
            schemata='urban_location',
            vocabulary=DisplayList((
                ('285', 'Art. 285 - complet avec architecte'),
                ('288', 'Art. 288 - simplifié avec architecte'),
                ('291', 'Art. 291 - simplifié sans architecte'),
            )),
        ),
    ),
    )
    BuildLicenceSchema = baseSchema + specificSchema.copy()

    BuildLicenceSchema['locationMissingParts'].widget.format = None
    # stats INS no longer mandatory
    BuildLicenceSchema['usage'].required = False
    BuildLicenceSchema['roadTechnicalAdvice'].widget.label_msgid = 'urban_label_roadDescription'
    BuildLicenceSchema.moveField('composition', before='locationMissingParts')

    return BuildLicenceSchema


def getCompositionMissingParts(self, composition):
    """
    """
    urban_voc = self.schema['locationMissingParts'].vocabulary
    all_terms = urban_voc.listAllVocTerms(self)

    display_values = [(term.Title().decode('utf-8'), term.id) for term in all_terms if str(composition) in term.getExtraValue()]

    return DisplayList(display_values)


BuildLicence.getCompositionMissingParts = getCompositionMissingParts
BuildLicence.schema = update_item_schema(BuildLicence.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
