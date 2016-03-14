# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import liege.urban


class LiegeUrbanLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=liege.urban)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'liege.urban:default')


LIEGE_URBAN_FIXTURE = LiegeUrbanLayer()


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
