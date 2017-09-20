# -*- coding: utf-8 -*-

from plone.app.testing import PloneWithPackageLayer

from Products.urban import tests as urban_tests
from Products.urban import testing

import inspect
import Products.urban


testing.URBAN_TESTS_PROFILE_DEFAULT = PloneWithPackageLayer(
    zcml_filename="testing.zcml",
    zcml_package=Products.urban,
    additional_z2_products=(
        'liege.urban',
        'Products.urban',
        'Products.CMFPlacefulWorkflow',
        'imio.dashboard',
    ),
    gs_profile_id='Products.urban:tests',
    name="URBAN_TESTS_PROFILE_DEFAULT"
)

# impport all tests modules from urban
test_modules = [v for k, v in inspect.getmembers(urban_tests, inspect.ismodule)
                if k.lower().startswith('test')]

for module in test_modules:
    test_classes = [v for k, v in inspect.getmembers(urban_tests, inspect.isclass)
                    if k.lower().startswith('test')]
    # import all test classes from urban, so ALL the urban tests runs when
    # running urban.liege tests
    for test_class in test_classes:
        test_class
