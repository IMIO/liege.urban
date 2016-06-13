# -*- coding: utf-8 -*-

from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class ShoreVocabularyFactory(object):

    def __call__(self, context):
        vocabulary = SimpleVocabulary(
            [
                SimpleTerm('right', 'right', 'Droite'),
                SimpleTerm('left', 'left', 'Gauche'),
                SimpleTerm('center', 'center', 'Centre'),
            ]
        )
        return vocabulary
