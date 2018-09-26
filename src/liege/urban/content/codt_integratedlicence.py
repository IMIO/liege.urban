# -*- coding: utf-8 -*-

from Products.urban.content.licence.CODT_IntegratedLicence import CODT_IntegratedLicence

# buildlicence and integratedlicence schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema
from liege.urban.licence_fields_permissions import set_field_permissions

permissions_mapping = {
    'urban_description': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_location': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
    'urban_habitation': ('liege.urban: External Reader', 'urban: Add PortionOut'),
}


CODT_IntegratedLicence.schema = update_item_schema(CODT_IntegratedLicence.schema)
CODT_IntegratedLicence.schema = set_field_permissions(
    CODT_IntegratedLicence.schema,
    permissions_mapping,
)
