# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import Schema

from Products.urban.Applicant import Applicant
from Products.urban.Claimant import Claimant
from Products.urban.FolderManager import FolderManager


def update_item_schema(baseSchema):

    specificSchema = Schema((),)

    ContactSchema = baseSchema + specificSchema.copy()

    # remove fax field
    ContactSchema.delField('fax')

    return ContactSchema


Applicant.schema = update_item_schema(Applicant.schema)
Claimant.schema = update_item_schema(Claimant.schema)
FolderManager.schema = update_item_schema(FolderManager.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
