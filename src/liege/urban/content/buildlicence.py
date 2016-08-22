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

    # move some road fields to location schemata
    BuildLicenceSchema['sevesoSite'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('sevesoSite', after='airportNoiseZoneDetails')
    BuildLicenceSchema['natura_2000'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('natura_2000', after='sevesoSite')
    BuildLicenceSchema['roadDgrneUnderground'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('roadDgrneUnderground', after='natura_2000')
    BuildLicenceSchema['roadType'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('roadType', after='roadDgrneUnderground')
    BuildLicenceSchema['pash'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('pash', after='roadType')
    BuildLicenceSchema['pashDetails'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('pashDetails', after='pash')
    BuildLicenceSchema['catchmentArea'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('catchmentArea', after='pashDetails')
    BuildLicenceSchema['catchmentAreaDetails'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('catchmentAreaDetails', after='catchmentArea')
    BuildLicenceSchema['karstConstraints'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('karstConstraints', after='catchmentAreaDetails')
    BuildLicenceSchema['karstConstraintsDetails'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('karstConstraintsDetails', after='karstConstraints')
    BuildLicenceSchema['floodingLevel'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('floodingLevel', after='karstConstraintsDetails')
    BuildLicenceSchema['floodingLevelDetails'].schemata = 'urban_location'
    BuildLicenceSchema.moveField('floodingLevelDetails', after='floodingLevel')

    # stats INS no longer mandatory
    BuildLicenceSchema['usage'].required = False
    BuildLicenceSchema['roadTechnicalAdvice'].widget.label_msgid = 'urban_label_roadDescription'
    BuildLicenceSchema['locationTechnicalRemarks'].widget.label_msgid = 'urban_label_description'
    BuildLicenceSchema['missingParts'].widget.size = 15
    BuildLicenceSchema['RCU'].widget.label_msgid = 'urban_label_RCB'
    BuildLicenceSchema['rcuDetails'].widget.label_msgid = 'urban_label_rcbDetails'

    return BuildLicenceSchema


BuildLicence.schema = update_item_schema(BuildLicence.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
