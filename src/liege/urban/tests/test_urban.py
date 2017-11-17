# -*- coding: utf-8 -*-

from liege.urban.testing import LIEGE_URBAN_FIXTURE
from liege.urban.testing import LIEGE_URBAN_TESTS_PROFILE_INTEGRATION
from liege.urban.testing import LIEGE_URBAN_TESTS_PROFILE_FUNCTIONAL
from liege.urban.testing import LIEGE_URBAN_TESTS_INTEGRATION
from liege.urban.testing import LIEGE_URBAN_TESTS_CONFIG
from liege.urban.testing import LIEGE_URBAN_TESTS_LICENCES
from liege.urban.testing import LIEGE_URBAN_IMPORTS
from liege.urban.testing import LIEGE_URBAN_TESTS_FUNCTIONAL
from liege.urban.testing import LIEGE_URBAN_TESTS_CONFIG_FUNCTIONAL
from liege.urban.testing import LIEGE_URBAN_TESTS_LICENCES_FUNCTIONAL
from liege.urban.testing import LIEGE_URBAN_TEST_ROBOT

from Products.urban import tests as urban_tests
from Products.urban.testing import URBAN_TESTS_PROFILE_DEFAULT
from Products.urban.testing import URBAN_TESTS_PROFILE_INTEGRATION
from Products.urban.testing import URBAN_TESTS_PROFILE_FUNCTIONAL
from Products.urban.testing import URBAN_TESTS_INTEGRATION
from Products.urban.testing import URBAN_TESTS_CONFIG
from Products.urban.testing import URBAN_TESTS_LICENCES
from Products.urban.testing import URBAN_IMPORTS
from Products.urban.testing import URBAN_TESTS_FUNCTIONAL
from Products.urban.testing import URBAN_TESTS_CONFIG_FUNCTIONAL
from Products.urban.testing import URBAN_TESTS_LICENCES_FUNCTIONAL
from Products.urban.testing import URBAN_TEST_ROBOT

import importlib
import inspect
import os

layers_mapping = {
    URBAN_TESTS_PROFILE_DEFAULT: LIEGE_URBAN_FIXTURE,
    URBAN_TESTS_PROFILE_INTEGRATION: LIEGE_URBAN_TESTS_PROFILE_INTEGRATION,
    URBAN_TESTS_PROFILE_FUNCTIONAL: LIEGE_URBAN_TESTS_PROFILE_FUNCTIONAL,
    URBAN_TESTS_INTEGRATION: LIEGE_URBAN_TESTS_INTEGRATION,
    URBAN_TESTS_CONFIG: LIEGE_URBAN_TESTS_CONFIG,
    URBAN_TESTS_LICENCES: LIEGE_URBAN_TESTS_LICENCES,
    URBAN_IMPORTS: LIEGE_URBAN_IMPORTS,
    URBAN_TESTS_FUNCTIONAL: LIEGE_URBAN_TESTS_FUNCTIONAL,
    URBAN_TESTS_CONFIG_FUNCTIONAL: LIEGE_URBAN_TESTS_CONFIG_FUNCTIONAL,
    URBAN_TESTS_LICENCES_FUNCTIONAL: LIEGE_URBAN_TESTS_LICENCES_FUNCTIONAL,
    URBAN_TEST_ROBOT: LIEGE_URBAN_TEST_ROBOT,
}

_this_module_ = globals()

# impport all tests modules from urban
test_modules_names = [m_name.split('.')[0] for m_name in os.listdir(urban_tests.__path__[0])
                      if m_name.lower().startswith('test') and m_name.endswith('py')]
for module_name in test_modules_names:
    test_module = importlib.import_module('{}.{}'.format(urban_tests.__name__, module_name))
    for class_name, test_class in inspect.getmembers(test_module, inspect.isclass):
        is_test = class_name.lower().startswith('test')
        layer = getattr(test_class, 'layer', '')
        if is_test and layer:
            # import all test classes from urban, so ALL the urban tests runs when
            # running urban.liege tests
            test_class.layer = layers_mapping[layer]
            _this_module_[test_class.__name__] = test_class
