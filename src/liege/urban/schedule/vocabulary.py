# -*- coding: utf-8 -*-

from collective.eeafaceted.collectionwidget.vocabulary import CollectionVocabulary

from plone import api

from zope.i18n import translate as _
from zope.schema.vocabulary import SimpleTerm
from zope.schema.vocabulary import SimpleVocabulary


class SurveyScheduleCollectionVocabulary(CollectionVocabulary):
    """
    Return vocabulary of base searchs for schedule faceted view.
    """

    def _brains(self, context):
        """
        Return all the DashboardCollections in the 'schedule' folder.
        """
        portal = api.portal.get()
        schedule_folder = portal.urban.survey_schedule
        catalog = api.portal.get_tool('portal_catalog')
        brains = catalog(
            path={
                'query': '/'.join(schedule_folder.getPhysicalPath()),
                'depth': 2
            },
            object_provides='plone.app.collection.interfaces.ICollection',
            sort_on='getObjPositionInParent'
        )
        return brains

SurveyScheduleCollectionVocabularyFactory = SurveyScheduleCollectionVocabulary()


class OpinionsScheduleCollectionVocabulary(CollectionVocabulary):
    """
    Return vocabulary of base searchs for schedule faceted view.
    """

    def _brains(self, context):
        """
        Return all the DashboardCollections in the 'schedule' folder.
        """
        portal = api.portal.get()
        schedule_folder = portal.urban.opinions_schedule
        catalog = api.portal.get_tool('portal_catalog')
        brains = catalog(
            path={
                'query': '/'.join(schedule_folder.getPhysicalPath()),
                'depth': 2
            },
            object_provides='plone.app.collection.interfaces.ICollection',
            sort_on='getObjPositionInParent'
        )
        return brains

OpinionsScheduleCollectionVocabularyFactory = OpinionsScheduleCollectionVocabulary()


class UsersFromGroupVocabularyFactory(object):
    """
    Vocabulary factory listing all the users of a group.
    """

    group_id = ''  # to override

    def __call__(self, context):
        """
        List users from a group as a vocabulary.
        """
        voc_terms = []
        group = api.group.get(self.group_id)

        for user in api.user.get_users(group=group):
            voc_terms.append(
                SimpleTerm(user.id, user.id, user.getProperty('fullname') or user.getUserName())
            )

        vocabulary = SimpleVocabulary(voc_terms)
        return vocabulary


class SurveyUsersVocabularyFactory(UsersFromGroupVocabularyFactory):
    """
    Vocabulary factory listing all the users of the survey group.
    """
    group_id = 'survey_editors'


class OpinionsRequestWorkflowStates(object):
    """
    List all states of urban licence workflow.
    """

    def __call__(self, context):

        states = ['wating_opinion', 'opinion_validation']

        vocabulary_terms = []
        for state in states:
            vocabulary_terms.append(
                SimpleTerm(
                    state,
                    state,
                    _(state, 'liege.urban', context.REQUEST)
                )
            )

        vocabulary = SimpleVocabulary(vocabulary_terms)
        return vocabulary
