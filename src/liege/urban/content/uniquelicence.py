# -*- coding: utf-8 -*-

from Products.urban.UniqueLicence import UniqueLicence

# buildlicence and uniquelicence schema should have the same changes
from liege.urban.content.buildlicence import update_item_schema


UniqueLicence.schema = update_item_schema(UniqueLicence.schema)
