# -*- coding: utf-8 -*-

from Products.urban.content.licence.IntegratedLicence import IntegratedLicence

# buildlicence and article127 schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema


IntegratedLicence.schema = update_item_schema(IntegratedLicence.schema)
