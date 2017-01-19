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


class UsersFromGroupsVocabularyFactory(object):
    """
    Vocabulary factory listing all the users of a group.
    """

    group_ids = []  # to override
    me_value = False  # set to True to add a value representing the current user

    def __call__(self, context):
        """
        List users from a group as a vocabulary.
        """
        base_terms = []
        me_id = ''
        user_ids = set()
        if self.me_value:
            me = api.user.get_current()
            me_id = me.id
            base_terms.append(SimpleTerm(me_id, me_id, 'Moi'))
            base_terms.append(SimpleTerm('to_assign', 'to_assign', 'À ASSIGNER'))

        voc_terms = []
        for group_id in self.group_ids:
            group = api.group.get(group_id)

            for user in api.user.get_users(group=group):
                if user.id != me_id and user.id not in user_ids:
                    user_ids.add(user.id)
                    voc_terms.append(
                        SimpleTerm(
                            user.id,
                            user.id,
                            user.getProperty('fullname') or user.getUserName()
                        )
                    )

        vocabulary = SimpleVocabulary(base_terms + sorted(voc_terms, key=lambda term: term.title))
        return vocabulary


class SurveyUsersVocabularyFactory(UsersFromGroupsVocabularyFactory):
    """
    Vocabulary factory listing all the users of the survey group.
    """
    group_ids = ['survey_editors']


class ScheduleUsersVocabularyFactory(UsersFromGroupsVocabularyFactory):
    """
    Vocabulary factory listing all the users of the urban schedule.
    """
    me_value = True
    group_ids = [
        'technical_editors',
        'technical_validators',
        'administrative_editors',
        'administrative_validators',
    ]


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
