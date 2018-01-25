# -*- coding: utf-8 -*-

from Products.urban.FolderManager import FolderManager


def Title(self):
    """
    """

    title = "{} ({})".format(
        self.getInitials(),
        self.displayValue(self.Vocabulary('grade')[0], self.getGrade()).encode('utf8')
    )
    return title


FolderManager.Title = Title


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
