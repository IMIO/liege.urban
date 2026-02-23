# encoding: utf-8

from datetime import datetime
from plone import api

import logging


logger = logging.getLogger('urban: migrations')


def fix_address_point(context):
    logger = logging.getLogger("urban: fix address point value type")
    brains = api.content.find(
        object_provides=["Products.urban.interfaces.IGenericLicence"],
        sort_on="modified",
        sort_order="reverse",
        sort_limit=2000,
    )[:2000]
    tzinfo = brains[0].modified.asdatetime().tzinfo
    matching_brains = [
        b for b in brains
        if b.modified.asdatetime() > datetime(2026, 2, 22, tzinfo=tzinfo)
    ]
    logger.info("{0} brains concerned".format(len(matching_brains)))
    for brain in matching_brains:
        obj = brain.getObject()
        parcels = obj.listFolderContents(
            contentFilter={"portal_type" : "Parcel"}
        )
        for parcel in parcels:
            if not isinstance(parcel.address_point, int):
                logger.info("fix parcel {0}".format(parcel.absolute_url()))
                parcel.address_point = int(parcel.address_point)
                parcel._p_changed = 1
    logger.info("migration step done!")
