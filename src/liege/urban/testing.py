# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneWithPackageLayer
from plone.testing import z2

import liege.urban


LIEGE_URBAN_FIXTURE = PloneWithPackageLayer(
    zcml_filename="testing.zcml",
    zcml_package=liege.urban,
    additional_z2_products=(
        'Products.urban',
        'liege.urban',
        'Products.CMFPlacefulWorkflow',
        'imio.dashboard',
    ),
    gs_profile_id='liege.urban:default',
    name="LIEGE_URBAN_FIXTURE"
)


LIEGE_URBAN_INTEGRATION_TESTING = IntegrationTesting(
    bases=(LIEGE_URBAN_FIXTURE,),
    name='LiegeUrbanLayer:IntegrationTesting'
)


LIEGE_URBAN_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(LIEGE_URBAN_FIXTURE,),
    name='LiegeUrbanLayer:FunctionalTesting'
)


LIEGE_URBAN_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        LIEGE_URBAN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='LiegeUrbanLayer:AcceptanceTesting'
)
