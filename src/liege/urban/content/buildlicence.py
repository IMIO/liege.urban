# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import StringField
from Products.Archetypes.public import DisplayList

from Products.MasterSelectWidget.MasterSelectWidget import MasterSelectWidget

from Products.urban.BuildLicence import BuildLicence


slave_fields_composition = (
    {
        'name': 'missingParts',
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
            schemata='urban_description',
            vocabulary=DisplayList((
                ('285', 'Art. 285 - complet avec architecte'),
                ('288', 'Art. 288 - simplifié avec architecte'),
                ('291', 'Art. 291 - simplifié sans architecte'),
            )),
        ),
    ),
    )
    BuildLicenceSchema = baseSchema + specificSchema.copy()

    BuildLicenceSchema['missingParts'].widget.format = None
    # stats INS no longer mandatory
    BuildLicenceSchema['usage'].required = False
    BuildLicenceSchema['roadTechnicalAdvice'].widget.label_msgid = 'urban_label_roadDescription'
    BuildLicenceSchema.moveField('composition', after='workType')

    return BuildLicenceSchema


def getCompositionMissingParts(self, composition):
    """
    """
    urban_voc = self.schema['missingParts'].vocabulary
    all_terms = urban_voc.getAllVocTerms(self)

    display_values = [(term.Title().decode('utf-8'), id) for id, term in all_terms.iteritems() if str(composition) in term.getExtraValue()]

    return DisplayList(display_values)


BuildLicence.getCompositionMissingParts = getCompositionMissingParts
BuildLicence.schema = update_item_schema(BuildLicence.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
