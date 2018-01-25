# -*- coding: utf-8 -*-

from Products.urban.UrbanEventOpinionRequest import UrbanEventOpinionRequest

UrbanEventOpinionRequest.__ac_local_roles_block__ = True  # disable local roles inheritance and let the workflow handle the permissions.


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
