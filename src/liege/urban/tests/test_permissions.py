# -*- coding: utf-8 -*-
"""Setup tests for this package."""
import unittest

from plone import api
from zope.event import notify
from zope.lifecycleevent import ObjectModifiedEvent

from Products.urban.browser.urbanconfigview import AddInternalServiceForm
from Products.urban.testing import URBAN_TESTS_CONFIG_FUNCTIONAL


class TestOpinionEditors(unittest.TestCase):

    layer = URBAN_TESTS_CONFIG_FUNCTIONAL

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

        with api.env.adopt_roles(["Manager"]):

            self.setup_opinion_request_type()

            self.create_internal_service(
                "access",
                "ACCESS",
            )

            api.user.create(email="claude@claude.com", username="claude")
            api.group.add_user(groupname='Access_editors', username='claude')
            api.group.add_user(groupname='opinions_editors', username='claude')

            aaa_id = self.portal.urban.codt_article127s.invokeFactory("CODT_Article127", id="aaa")
            self.aaa = getattr(self.portal.urban.codt_article127s, aaa_id)
            notify(ObjectModifiedEvent(self.aaa))

            bbb_id = self.portal.urban.roaddecrees.invokeFactory("RoadDecree", id="bbb")
            self.bbb = getattr(self.portal.urban.roaddecrees, bbb_id)
            self.bbb.setBound_licence(self.aaa.UID())
            self.bbb.setSolicitOpinionsTo(["access"])
            self.bbb.createAllAdvices()
            notify(ObjectModifiedEvent(self.bbb))

            opinion_request = self.bbb.getAllOpinionRequests()[0]
            api.user.grant_roles(username="claude", roles=["Editor"], obj=opinion_request)

    def tearDown(self):
        with api.env.adopt_roles(['Manager']):
            api.content.delete(self.aaa)
            api.content.delete(self.bbb)
            api.user.delete(username="claude")

    def setup_opinion_request_type(self):
        urbaneventtypes_folder = self.portal.portal_urban.roaddecree.urbaneventtypes

        term_id = urbaneventtypes_folder.invokeFactory(
            "OpinionRequestEventType",
            id="ask_access_opinion",
            title="Demande d'avis (ACCESS)",
            description="access",
            internal_service="access",
            is_internal_service=True,
            eventTypeType=u'Products.urban.interfaces.IOpinionRequestEvent',
            eventPortalType='UrbanEventOpinionRequest',
        )

        urbaneventtypes_folder.invokeFactory(
            'UrbanEventType',
            id="config-opinion-request",
            title="*** Demande d'avis CONFIG ***",
            activatedFields=[],
            TALCondition="python: False",
            podTemplates=({'id': "cu2-avis.odt", 'title': "Courrier de demande d'avis"},),
            eventTypeType='Products.urban.interfaces.IOpinionRequestEvent',
            eventPortalType='UrbanEventOpinionRequest'
        )

    def create_internal_service(self, service_id, service_name):
        add_internal_service_form = AddInternalServiceForm({}, {})
        editor_group_id, validator_group_id = add_internal_service_form.create_groups(
            service_id.capitalize(), service_name
        )
        (
            task_config_answer,
            task_config_validate,
        ) = add_internal_service_form.create_task_configs(
            service_id, service_name, editor_group_id, validator_group_id
        )
        add_internal_service_form.set_registry_mapping(
            service_id,
            service_name,
            editor_group_id,
            validator_group_id,
            task_config_answer,
            task_config_validate,
        )

    def test_linked_opinion_editors_view(self):
        # before
        self.assertFalse(api.user.has_permission('View', username='claude', obj=self.aaa))
        self.assertFalse(api.user.has_permission('View', username='claude', obj=self.bbb))
        self.assertNotIn("ExternalReader", api.user.get_roles(username='claude', obj=self.aaa))
        self.assertNotIn("ExternalReader", api.user.get_roles(username='claude', obj=self.bbb))

        opinion_request = self.bbb.getAllOpinionRequests()[0]
        with api.env.adopt_user("claude"):
            api.content.transition(opinion_request, "ask_opinion")
            api.content.transition(opinion_request, "ask_validation")

        with api.env.adopt_roles(["Manager"]):
            api.content.transition(self.aaa, "ask_address_validation")
            api.content.transition(self.aaa, "validate_address")
            api.content.transition(self.bbb, "to_public_investigation")
            api.content.transition(self.bbb, "to_technical_analysis_post_investigation")

        # after
        self.assertTrue(api.user.has_permission('View', username='claude', obj=self.aaa))
        self.assertTrue(api.user.has_permission('View', username='claude', obj=self.bbb))
        self.assertIn("ExternalReader", api.user.get_roles(username='claude', obj=self.aaa))
        self.assertIn("ExternalReader", api.user.get_roles(username='claude', obj=self.bbb))
