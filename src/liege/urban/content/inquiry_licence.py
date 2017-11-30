# -*- coding: utf-8 -*-

from Products.urban.Article127 import Article127
from Products.urban.BuildLicence import BuildLicence
from Products.urban.CODT_Article127 import CODT_Article127
from Products.urban.CODT_BuildLicence import CODT_BuildLicence
from Products.urban.CODT_IntegratedLicence import CODT_IntegratedLicence
from Products.urban.CODT_ParcelOutLicence import CODT_ParcelOutLicence
from Products.urban.CODT_UniqueLicence import CODT_UniqueLicence
from Products.urban.CODT_UrbanCertificateTwo import CODT_UrbanCertificateTwo
from Products.urban.IntegratedLicence import IntegratedLicence
from Products.urban.MiscDemand import MiscDemand
from Products.urban.ParcelOutLicence import ParcelOutLicence
from Products.urban.PatrimonyCertificate import PatrimonyCertificate
from Products.urban.UniqueLicence import UniqueLicence
from Products.urban.UrbanCertificateTwo import UrbanCertificateTwo


def update_item_schema(baseSchema):

    LicenceSchema = baseSchema

    # some fields are only visible in edit
    LicenceSchema['investigationArticlesText'].widget.visible = {'edit': 'visible', 'view': 'invisible'}
    LicenceSchema['derogationDetails'].widget.visible = {'edit': 'visible', 'view': 'invisible'}
    LicenceSchema['investigationReasons'].widget.visible = {'edit': 'visible', 'view': 'invisible'}
    LicenceSchema['demandDisplay'].widget.visible = {'edit': 'visible', 'view': 'invisible'}
    LicenceSchema['investigationDetails'].widget.visible = {'edit': 'visible', 'view': 'invisible'}

    # reorder fields
    LicenceSchema.moveField('derogation', after='investigationArticlesText')
    LicenceSchema.moveField('derogationDetails', after='derogation')
    LicenceSchema.moveField('investigationReasons', after='demandDisplay')
    LicenceSchema.moveField('investigationDetails', after='roadModificationSubject')

    # re translate some fields
    LicenceSchema['solicitOpinionsTo'].widget.label_msgid = 'urban_label_solicitExternalOpinionsTo'
    LicenceSchema['solicitOpinionsToOptional'].widget.label_msgid = 'urban_label_solicitInternalOpinionsTo'

    return LicenceSchema


licence_classes = [
    Article127, BuildLicence, CODT_Article127, CODT_BuildLicence, CODT_IntegratedLicence,
    CODT_ParcelOutLicence, CODT_UniqueLicence, CODT_UrbanCertificateTwo,
    IntegratedLicence, MiscDemand, ParcelOutLicence, PatrimonyCertificate, UniqueLicence,
    UrbanCertificateTwo
]

for licence_class in licence_classes:
    licence_class.schema = update_item_schema(licence_class.schema)
