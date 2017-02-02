# -*- coding: utf-8 -*-

from Products.urban.UniqueLicence import UniqueLicence

# buildlicence and article127 schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema
from liege.urban.licence_fields_permissions import set_field_permissions

permissions_mapping = {
    'urban_description': ('liege.urban: External Reader', 'liege.urban: Internal Editor'),
    'urban_advices': ('liege.urban: Road Reader', 'liege.urban: Internal Editor'),
    'urban_location': ('liege.urban: External Reader', 'liege.urban: Road Editor'),
    'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
}


UniqueLicence.schema = update_item_schema(UniqueLicence.schema)
UniqueLicence.schema = set_field_permissions(
    UniqueLicence.schema,
    permissions_mapping,
    exceptions=['portal_type']
)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
