# -*- coding: utf-8 -*-

from Products.urban.Article127 import Article127
from Products.urban.BuildLicence import BuildLicence
from Products.urban.MiscDemand import MiscDemand
from Products.urban.ParcelOutLicence import ParcelOutLicence
from Products.urban.PatrimonyCertificate import PatrimonyCertificate
from Products.urban.PreliminaryNotice import PreliminaryNotice
from Products.urban.UrbanCertificateTwo import UrbanCertificateTwo


def update_item_schema(baseSchema):

    LicenceSchema = baseSchema

    # some fields are only visible in edit
    LicenceSchema['investigationArticlesText'].edit_only = True
    LicenceSchema['derogationDetails'].edit_only = True
    LicenceSchema['investigationReasons'].edit_only = True
    LicenceSchema['demandDisplay'].edit_only = True
    LicenceSchema['investigationDetails'].edit_only = True

    # reorder fields
    LicenceSchema.moveField('derogation', after='investigationArticlesText')
    LicenceSchema.moveField('derogationDetails', after='derogation')
    LicenceSchema.moveField('investigationReasons', after='derogationDetails')
    LicenceSchema.moveField('demandDisplay', after='investigationEnd')
    LicenceSchema.moveField('investigationDetails', after='investigationWriteReclamationNumber')

    return LicenceSchema


licence_classes = [
    Article127, BuildLicence, MiscDemand, ParcelOutLicence, PatrimonyCertificate,
    PreliminaryNotice, UrbanCertificateTwo
]

for licence_class in licence_classes:
    licence_class.schema = update_item_schema(licence_class.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
