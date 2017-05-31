# -*- coding: utf-8 -*-

from Products.urban.CODT_IntegratedLicence import CODT_IntegratedLicence

# buildlicence and article127 schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema


CODT_IntegratedLicence.schema = update_item_schema(CODT_IntegratedLicence.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
