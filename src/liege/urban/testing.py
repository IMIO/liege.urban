# -*- coding: utf-8 -*-
import liege.urban


def testing_profile(profile):
    profile.zcml_filename = "testing.zcml"
    profile.zcml_package = liege.urban
    profile.additional_z2_products = (
        'Products.urban',
        'liege.urban',
        'Products.CMFPlacefulWorkflow',
        'imio.dashboard',
    )
    profile.gs_profile_id = 'liege.urban:tests'
