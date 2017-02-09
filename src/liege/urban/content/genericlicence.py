# -*- coding: utf-8 -*-

from liege.urban.interfaces import IShore

from Products.Archetypes.atapi import Schema

from Products.urban.Article127 import Article127
from Products.urban.BuildLicence import BuildLicence
from Products.urban.Declaration import Declaration
from Products.urban.Division import Division
from Products.urban.EnvClassOne import EnvClassOne
from Products.urban.EnvClassThree import EnvClassThree
from Products.urban.EnvClassTwo import EnvClassTwo
from Products.urban.GenericLicence import GenericLicence
from Products.urban.IntegratedLicence import IntegratedLicence
from Products.urban.MiscDemand import MiscDemand
from Products.urban.ParcelOutLicence import ParcelOutLicence
from Products.urban.PatrimonyCertificate import PatrimonyCertificate
from Products.urban.UniqueLicence import UniqueLicence
from Products.urban.UrbanCertificateBase import UrbanCertificateBase
from Products.urban.UrbanCertificateTwo import UrbanCertificateTwo

from zope.i18n import translate
from zope.component import queryAdapter


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

    # move some road fields to location schemata
    LicenceSchema['sevesoSite'].schemata = 'urban_location'
    LicenceSchema.moveField('sevesoSite', after='airportNoiseZoneDetails')
    LicenceSchema['natura_2000'].schemata = 'urban_location'
    LicenceSchema.moveField('natura_2000', after='sevesoSite')
    LicenceSchema['roadType'].schemata = 'urban_location'
    LicenceSchema.moveField('roadType', after='natura_2000')
    LicenceSchema['pash'].schemata = 'urban_location'
    LicenceSchema.moveField('pash', after='roadType')
    LicenceSchema['pashDetails'].schemata = 'urban_location'
    LicenceSchema.moveField('pashDetails', after='pash')
    LicenceSchema['catchmentArea'].schemata = 'urban_location'
    LicenceSchema.moveField('catchmentArea', after='pashDetails')
    LicenceSchema['catchmentAreaDetails'].schemata = 'urban_location'
    LicenceSchema.moveField('catchmentAreaDetails', after='catchmentArea')
    LicenceSchema['karstConstraints'].schemata = 'urban_location'
    LicenceSchema.moveField('karstConstraints', after='catchmentAreaDetails')
    LicenceSchema['karstConstraintsDetails'].schemata = 'urban_location'
    LicenceSchema.moveField('karstConstraintsDetails', after='karstConstraints')
    LicenceSchema['floodingLevel'].schemata = 'urban_location'
    LicenceSchema.moveField('floodingLevel', after='karstConstraintsDetails')
    LicenceSchema['floodingLevelDetails'].schemata = 'urban_location'
    LicenceSchema.moveField('floodingLevelDetails', after='floodingLevel')

    LicenceSchema['locationTechnicalRemarks'].widget.label_msgid = 'urban_label_description'
    LicenceSchema['RCU'].widget.label_msgid = 'urban_label_RCB'
    LicenceSchema['rcuDetails'].widget.label_msgid = 'urban_label_rcbDetails'

    return LicenceSchema


licence_classes = [
    Article127, BuildLicence, Declaration, Division, EnvClassOne,
    EnvClassThree, EnvClassTwo, MiscDemand, ParcelOutLicence, PatrimonyCertificate,
    UrbanCertificateBase, UrbanCertificateTwo, IntegratedLicence, UniqueLicence
]

for licence_class in licence_classes:
    licence_class.schema = update_item_schema(licence_class.schema)


def updateTitle(self):
    """
        Update the title to clearly identify the licence
    """
    if self.getApplicants():
        applicantTitle = self.getApplicants()[0].Title()
    else:
        applicantTitle = translate('no_applicant_defined', 'urban', context=self.REQUEST).encode('utf8')
    to_shore = queryAdapter(self, IShore)
    title = "%s %s - %s - %s" % (self.getReference(), to_shore.display(), self.getLicenceSubject(), applicantTitle)
    self.setTitle(title)
    self.reindexObject(idxs=('Title', 'applicantInfosIndex', 'sortable_title', ))

GenericLicence.updateTitle = updateTitle

# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
