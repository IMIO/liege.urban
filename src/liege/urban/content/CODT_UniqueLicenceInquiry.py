# -*- coding: utf-8 -*-

from Products.urban.content.CODT_UniqueLicenceInquiry import CODT_UniqueLicenceInquiry
from Products.Archetypes.atapi import DisplayList


def list_inquiry_category(self):
    """ """
    vocabulary = (
        ("", "-- Choisissez --"),
        ("B", "Catégorie B, rayon 200m (attention publication)"),
        ("C", "Catégorie C, rayon 50m"),
    )
    return DisplayList(vocabulary)


CODT_UniqueLicenceInquiry.list_inquiry_category = list_inquiry_category
