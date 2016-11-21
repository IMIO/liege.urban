# -*- coding: utf-8 -*-

from Products.urban.Article127 import Article127

from liege.urban.licence_fields_permissions import set_field_permissions

permissions_mapping = {
    'urban_description': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_advices': ('liege.urban: Road Reader', 'liege.urban: Internal Editor'),
    'urban_location': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
    'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
}


def update_item_schema(baseSchema):
    LicenceSchema = baseSchema.copy()

    # some fields are edit only
    LicenceSchema['annoncedDelayDetails'].edit_only = True
    LicenceSchema['pebDetails'].edit_only = True
    LicenceSchema['pebTechnicalAdvice'].edit_only = True

    # move PEB fields to analysis schemata
    LicenceSchema['pebType'].schemata = 'urban_analysis'
    LicenceSchema.moveField('pebType', after='usage')
    LicenceSchema['pebDetails'].schemata = 'urban_analysis'
    LicenceSchema.moveField('pebDetails', after='pebType')
    LicenceSchema['pebStudy'].schemata = 'urban_analysis'
    LicenceSchema.moveField('pebStudy', after='pebDetails')
    LicenceSchema['pebTechnicalAdvice'].schemata = 'urban_analysis'
    LicenceSchema.moveField('pebTechnicalAdvice', after='pebStudy')

    # move some road fields to location schemata
    LicenceSchema['sevesoSite'].schemata = 'urban_location'
    LicenceSchema.moveField('sevesoSite', after='airportNoiseZoneDetails')
    LicenceSchema['natura_2000'].schemata = 'urban_location'
    LicenceSchema.moveField('natura_2000', after='sevesoSite')
    LicenceSchema['roadDgrneUnderground'].schemata = 'urban_location'
    LicenceSchema.moveField('roadDgrneUnderground', after='natura_2000')
    LicenceSchema['roadType'].schemata = 'urban_location'
    LicenceSchema.moveField('roadType', after='roadDgrneUnderground')
    LicenceSchema['pash'].schemata = 'urban_location'
    LicenceSchema.moveField('pash', after='roadType')
    LicenceSchema['pashDetails'].schemata = 'urban_location'
    LicenceSchema.moveField('pashDetails', after='pash')
    LicenceSchema['catchmentArea'].schemata = 'urban_location'
    LicenceSchema.moveField('catchmentArea', after='pashDetails')
    LicenceSchema['catchmentAreaDetails'].schemata = 'urban_location'
    LicenceSchema.moveField('catchmentAreaDetails', after='catchmentArea')
    LicenceSchema['karstConstraints'].schemata = 'urban_location'
    LicenceSchema.moveField('karstConstraints', after='catchmentAreaDetails')
    LicenceSchema['karstConstraintsDetails'].schemata = 'urban_location'
    LicenceSchema.moveField('karstConstraintsDetails', after='karstConstraints')
    LicenceSchema['floodingLevel'].schemata = 'urban_location'
    LicenceSchema.moveField('floodingLevel', after='karstConstraintsDetails')
    LicenceSchema['floodingLevelDetails'].schemata = 'urban_location'
    LicenceSchema.moveField('floodingLevelDetails', after='floodingLevel')

    # stats INS no longer mandatory
    LicenceSchema['usage'].required = False
    LicenceSchema['roadTechnicalAdvice'].widget.label_msgid = 'urban_label_roadDescription'
    LicenceSchema['locationTechnicalRemarks'].widget.label_msgid = 'urban_label_description'
    LicenceSchema['missingParts'].widget.size = 15
    LicenceSchema['RCU'].widget.label_msgid = 'urban_label_RCB'
    LicenceSchema['rcuDetails'].widget.label_msgid = 'urban_label_rcbDetails'

    return LicenceSchema


Article127.schema = update_item_schema(Article127.schema)
Article127.schema = set_field_permissions(
    Article127.schema,
    permissions_mapping,
    exceptions=['portal_type']
)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
