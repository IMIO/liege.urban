# -*- coding: utf-8 -*-

from Products.urban.FolderManager import FolderManager


def Title(self):
    """
    """
    title = "{} ({})".format(
        self.getInitials(),
        self.Vocabulary('grade')[0].getValue(self.getGrade()).encode("utf8"),
    )
    return title


FolderManager.Title = Title
