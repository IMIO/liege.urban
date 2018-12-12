# -*- coding: utf-8 -*-

from Products.urban.content.licence.RoadDecree import RoadDecree

from liege.urban import UrbanMessage as _
from liege.urban.licence_fields_permissions import set_field_permissions

permissions_mapping = {
    'urban_description': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_location': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
    'urban_habitation': ('liege.urban: External Reader', 'urban: Add PortionOut'),
}


def update_item_schema(base_schema):
    licence_schema = base_schema.copy()
    licence_schema['roadTechnicalAdvice'].widget.label = _(
        'urban_label_roadDescription',
    )

    return licence_schema


RoadDecree.schema = update_item_schema(RoadDecree.schema)
RoadDecree.schema = set_field_permissions(RoadDecree.schema)
