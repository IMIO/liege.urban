# -*- coding: utf-8 -*-

from Products.urban.FolderManager import FolderManager


def Title(self):
    """
    """
    grade = self.getGrade()
    if not grade or not self.Vocabulary('grade')[0].getValue(grade):
        return self.id
    title = "{} ({})".format(
        self.getInitials(),
        self.Vocabulary('grade')[0].getValue(grade).encode("utf8"),
    )
    return title


FolderManager.Title = Title
