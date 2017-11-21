# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneWithPackageLayer
from plone.testing import z2
from plone.app.testing import helpers
from plone import api

from Products.urban.testing import UrbanConfigFunctionalLayer
from Products.urban.testing import UrbanConfigLayer
from Products.urban.testing import UrbanImportsLayer
from Products.urban.testing import UrbanLicencesFunctionalLayer
from Products.urban.testing import UrbanLicencesLayer
from Products.urban.testing import UrbanWithUsersFunctionalLayer
from Products.urban.testing import UrbanWithUsersLayer

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
    gs_profile_id='liege.urban:tests',
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


LIEGE_URBAN_TESTS_PROFILE_INTEGRATION = IntegrationTesting(
    bases=(LIEGE_URBAN_FIXTURE,), name="LIEGE_URBAN_TESTS_PROFILE_INTEGRATION")

LIEGE_URBAN_TESTS_PROFILE_FUNCTIONAL = FunctionalTesting(
    bases=(LIEGE_URBAN_FIXTURE,), name="LIEGE_URBAN_TESTS_PROFILE_FUNCTIONAL")


class UrbanLiegeWithUsersLayer(UrbanWithUsersLayer):
    """ """
    default_user = 'rach'
    default_password = 'Aaaaa12345@'

LIEGE_URBAN_TESTS_INTEGRATION = UrbanLiegeWithUsersLayer(
    bases=(LIEGE_URBAN_FIXTURE, ), name="LIEGE_URBAN_TESTS_INTEGRATION")


class UrbanLiegeConfigLayer(UrbanConfigLayer, UrbanLiegeWithUsersLayer):
    """ """

    def setUp(self):
        super(UrbanLiegeConfigLayer, self).setUp()
        with helpers.ploneSite() as portal:
            portal.setupCurrentSkin(portal.REQUEST)
            setup_tool = api.portal.get_tool('portal_setup')
            setup_tool.runImportStepFromProfile('profile-liege.urban:default', 'workflow')

LIEGE_URBAN_TESTS_CONFIG = UrbanLiegeConfigLayer(
    bases=(LIEGE_URBAN_FIXTURE, ), name="LIEGE_URBAN_TESTS_CONFIG")


LIEGE_URBAN_TESTS_LICENCES = UrbanLicencesLayer(
    bases=(LIEGE_URBAN_FIXTURE, ), name="LIEGE_URBAN_TESTS_LICENCES")


LIEGE_URBAN_IMPORTS = UrbanImportsLayer(
    bases=(LIEGE_URBAN_FIXTURE, ), name="LIEGE_URBAN_IMPORTS")


LIEGE_URBAN_TESTS_FUNCTIONAL = UrbanWithUsersFunctionalLayer(
    bases=(LIEGE_URBAN_FIXTURE, ), name="LIEGE_URBAN_TESTS_FUNCTIONAL")


LIEGE_URBAN_TESTS_CONFIG_FUNCTIONAL = UrbanConfigFunctionalLayer(
    bases=(LIEGE_URBAN_FIXTURE, ), name="LIEGE_URBAN_TESTS_CONFIG_FUNCTIONAL")


LIEGE_URBAN_TESTS_LICENCES_FUNCTIONAL = UrbanLicencesFunctionalLayer(
    bases=(LIEGE_URBAN_FIXTURE, ), name="LIEGE_URBAN_TESTS_LICENCES_FUNCTIONAL")


LIEGE_URBAN_TEST_ROBOT = UrbanConfigFunctionalLayer(
    bases=(
        LIEGE_URBAN_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name="LIEGE_URBAN_ROBOT"
)
