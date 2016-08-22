# -*- coding: utf-8 -*-

from Products.urban.BuildLicence import BuildLicence


def update_item_schema(baseSchema):
    BuildLicenceSchema = baseSchema

    # some fields are edit only
    BuildLicenceSchema['annoncedDelayDetails'].edit_only = True
    BuildLicenceSchema['pebDetails'].edit_only = True
    BuildLicenceSchema['pebTechnicalAdvice'].edit_only = True

    # move PEB fields to analysis schemata
    BuildLicenceSchema['pebType'].schemata = 'urban_analysis'
    BuildLicenceSchema.moveField('pebType', after='usage')
    BuildLicenceSchema['pebDetails'].schemata = 'urban_analysis'
    BuildLicenceSchema.moveField('pebDetails', after='pebType')
    BuildLicenceSchema['pebStudy'].schemata = 'urban_analysis'
    BuildLicenceSchema.moveField('pebStudy', after='pebDetails')
    BuildLicenceSchema['pebTechnicalAdvice'].schemata = 'urban_analysis'
    BuildLicenceSchema.moveField('pebTechnicalAdvice', after='pebStudy')

    # stats INS no longer mandatory
    BuildLicenceSchema['usage'].required = False
    BuildLicenceSchema['roadTechnicalAdvice'].widget.label_msgid = 'urban_label_roadDescription'
    BuildLicenceSchema['locationTechnicalRemarks'].widget.label_msgid = 'urban_label_description'
    BuildLicenceSchema['missingParts'].widget.size = 15

    return BuildLicenceSchema


BuildLicence.schema = update_item_schema(BuildLicence.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
