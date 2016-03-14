# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from liege.urban.testing import LIEGE_URBAN_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that liege.urban is properly installed."""

    layer = LIEGE_URBAN_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if liege.urban is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'liege.urban'))

    def test_browserlayer(self):
        """Test that ILiegeUrbanLayer is registered."""
        from liege.urban.interfaces import (
            ILiegeUrbanLayer)
        from plone.browserlayer import utils
        self.assertIn(ILiegeUrbanLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = LIEGE_URBAN_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['liege.urban'])

    def test_product_uninstalled(self):
        """Test if liege.urban is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'liege.urban'))
