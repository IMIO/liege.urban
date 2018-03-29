# -*- coding: utf-8 -*-

from Products.urban.CODT_BuildLicence import CODT_BuildLicence

from liege.urban.licence_fields_permissions import set_environment_field_permissions

permissions_mapping = {
    'urban_description': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_location': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
    'urban_habitation': ('liege.urban: External Reader', 'urban: Add PortionOut'),
}


def update_item_schema(baseSchema):
    LicenceSchema = baseSchema.copy()

    # hide some fields
    LicenceSchema['folderCategory'].widget.visible = {'edit': 'invisible', 'view': 'invisible'}


CODT_BuildLicence.schema = update_item_schema(CODT_BuildLicence.schema)
CODT_BuildLicence.schema = set_environment_field_permissions(
    CODT_BuildLicence.schema,
    permissions_mapping,
)
