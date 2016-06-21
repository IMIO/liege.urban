# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import Schema

from Products.urban.BuildLicence import BuildLicence


def update_item_schema(baseSchema):

    specificSchema = Schema((),)
    BuildLicenceSchema = baseSchema + specificSchema.copy()

    # stats INS no longer mandatory
    BuildLicenceSchema['usage'].required = False

    return BuildLicenceSchema


BuildLicence.schema = update_item_schema(BuildLicence.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
