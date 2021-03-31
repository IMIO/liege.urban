# -*- coding: utf-8 -*-

from Products.urban.content.licence.CODT_UrbanCertificateTwo import CODT_UrbanCertificateTwo

# buildlicence and article127 schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema
from liege.urban.licence_fields_permissions import set_field_permissions

permissions_mapping = {
    'urban_description': ('liege.urban: External Reader', 'liege.urban: Description Editor'),
    'urban_advices': ('liege.urban: Road Reader', 'liege.urban: Internal Editor'),
    'urban_location': ('liege.urban: External Reader', 'liege.urban: Road Editor'),
    'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
    'urban_habitation': ('liege.urban: External Reader', 'liege.urban: Habitation Editor'),
}


CODT_UrbanCertificateTwo.schema = update_item_schema(CODT_UrbanCertificateTwo.schema)
CODT_UrbanCertificateTwo.schema = set_field_permissions(
    CODT_UrbanCertificateTwo.schema,
    permissions_mapping,
)
