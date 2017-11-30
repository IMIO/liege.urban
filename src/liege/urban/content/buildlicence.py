# -*- coding: utf-8 -*-

from Products.urban.BuildLicence import BuildLicence

from liege.urban.licence_fields_permissions import set_field_permissions

permissions_mapping = {
    'urban_description': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_location': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
    'urban_habitation': ('liege.urban: External Reader', 'urban: Add PortionOut'),
}


def update_item_schema(baseSchema):
    LicenceSchema = baseSchema.copy()

    # some fields are edit only
    LicenceSchema['annoncedDelayDetails'].widget.visible = {'edit': 'visible', 'view': 'invisible'}
    LicenceSchema['pebDetails'].widget.visible = {'edit': 'visible', 'view': 'invisible'}
    LicenceSchema['pebTechnicalAdvice'].widget.visible = {'edit': 'visible', 'view': 'invisible'}

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
    LicenceSchema['roadDgrneUnderground'].schemata = 'urban_location'
    LicenceSchema.moveField('roadDgrneUnderground', after='natura_2000')
    LicenceSchema.moveField('roadType', after='roadDgrneUnderground')
    LicenceSchema['roadAdaptation'].schemata = 'urban_analysis'
    LicenceSchema.moveField('roadAdaptation', before='annoncedDelay')

    # stats INS no longer mandatory
    LicenceSchema['usage'].required = False
    LicenceSchema['roadTechnicalAdvice'].widget.label_msgid = 'urban_label_roadDescription'
    LicenceSchema['missingParts'].widget.size = 15

    return LicenceSchema


BuildLicence.schema = update_item_schema(BuildLicence.schema)
BuildLicence.schema = set_field_permissions(
    BuildLicence.schema,
    permissions_mapping,
)
