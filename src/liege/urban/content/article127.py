# -*- coding: utf-8 -*-

from Products.urban.Article127 import Article127

# buildlicence and article127 schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema
from liege.urban.licence_fields_permissions import set_field_permissions

permissions_mapping = {
    'urban_description': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_advices': ('liege.urban: Road Reader', 'liege.urban: Internal Editor'),
    'urban_location': ('liege.urban: External Reader', 'liege.urban: Road Editor'),
    'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
}


Article127.schema = update_item_schema(Article127.schema)
Article127.schema = set_field_permissions(
    Article127.schema,
    permissions_mapping,
)
