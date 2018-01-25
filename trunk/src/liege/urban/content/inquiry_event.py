# -*- coding: utf-8 -*-

from Products.urban.UrbanEventInquiry import UrbanEventInquiry


def update_item_schema(baseSchema):

    EventSchema = baseSchema

    # remove hours from date format
    EventSchema['explanationStartSDate'].widget.show_hm = False
    EventSchema['explanationStartSDate'].widget.format = '%d/%m/%Y'
    EventSchema['claimsDate'].widget.show_hm = False
    EventSchema['claimsDate'].widget.format = '%d/%m/%Y'

    # rename fields
    EventSchema['explanationStartSDate'].widget.label_msgid = 'urban_label_explanationDate'
    EventSchema['claimsDate'].widget.label_msgid = 'urban_label_closeDate'

    return EventSchema


UrbanEventInquiry.schema = update_item_schema(UrbanEventInquiry.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
