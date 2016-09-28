# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import Schema

from Products.urban.Article127 import Article127
from Products.urban.BuildLicence import BuildLicence
from Products.urban.Declaration import Declaration
from Products.urban.Division import Division
from Products.urban.EnvClassOne import EnvClassOne
from Products.urban.EnvClassThree import EnvClassThree
from Products.urban.EnvClassTwo import EnvClassTwo
from Products.urban.MiscDemand import MiscDemand
from Products.urban.ParcelOutLicence import ParcelOutLicence
from Products.urban.PatrimonyCertificate import PatrimonyCertificate
from Products.urban.PreliminaryNotice import PreliminaryNotice
from Products.urban.UrbanCertificateBase import UrbanCertificateBase
from Products.urban.UrbanCertificateTwo import UrbanCertificateTwo


def update_item_schema(baseSchema):

    specificSchema = Schema((
    ),)

    LicenceSchema = baseSchema + specificSchema.copy()

    # some fields are edit only
    LicenceSchema['missingPartsDetails'].edit_only = True
    LicenceSchema['protectedBuildingDetails'].edit_only = True
    LicenceSchema['rcuDetails'].edit_only = True
    LicenceSchema['prenuDetails'].edit_only = True
    LicenceSchema['prevuDetails'].edit_only = True
    LicenceSchema['airportNoiseZoneDetails'].edit_only = True
    LicenceSchema['pashDetails'].edit_only = True
    LicenceSchema['catchmentAreaDetails'].edit_only = True
    LicenceSchema['karstConstraintsDetails'].edit_only = True
    LicenceSchema['floodingLevelDetails'].edit_only = True

    # move folderCategoryTownship field on description schemata
    LicenceSchema['folderCategoryTownship'].schemata = 'urban_description'
    LicenceSchema['folderCategoryTownship'].widget.label_msgid = 'urban_label_UsageTownship'
    LicenceSchema['roadCoating'].widget.label_msgid = 'urban_label_pathCoating'
    LicenceSchema['futureRoadCoating'].widget.label_msgid = 'urban_label_futurePathCoating'
    LicenceSchema.moveField('folderCategoryTownship', after='folderCategory')

    return LicenceSchema


licence_classes = [
    Article127, BuildLicence, Declaration, Division, EnvClassOne,
    EnvClassThree, EnvClassTwo, MiscDemand, ParcelOutLicence, PatrimonyCertificate,
    PreliminaryNotice, UrbanCertificateBase, UrbanCertificateTwo
]

for licence_class in licence_classes:
    licence_class.schema = update_item_schema(licence_class.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
