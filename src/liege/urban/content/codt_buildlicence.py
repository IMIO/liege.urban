# -*- coding: utf-8 -*-

from Products.urban.CODT_BuildLicence import CODT_BuildLicence

# buildlicence and codt_buildlicence schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema
from liege.urban.licence_fields_permissions import set_field_permissions

permissions_mapping = {
    'urban_description': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_location': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
    'urban_habitation': ('liege.urban: External Reader', 'urban: Add PortionOut'),
}


CODT_BuildLicence.schema = update_item_schema(CODT_BuildLicence.schema)
CODT_BuildLicence.schema = set_field_permissions(
    CODT_BuildLicence.schema,
    permissions_mapping,
)
