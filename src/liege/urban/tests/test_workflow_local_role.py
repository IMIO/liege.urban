# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from Products.urban.testing import URBAN_TESTS_LICENCES
from Products.urban.browser.urbanconfigview import AddInternalServiceForm
from plone import api

import unittest
import logging


logger = logging.getLogger("urban.liege: test workflow local role")


class TestOpinionsrequestWorkflow(unittest.TestCase):

    layer = URBAN_TESTS_LICENCES

    matrice = {
        "demande-davis-plantation": {
            "creation": {
                "administrative_editors": ["Reader", "Editor"],
                "administrative_validators": ["Reader", "Editor"],
                "opinions_editors": None,
                "survey_editors": ["Reader"],
                "Plantation_editors": None,
                "Plantation_validators": None,
                "Access_editors": None,
                "Access_validators": None,
                "urban_readers": ["Reader"],
                "technical_editors": ["Reader"],
            },
            "waiting_opinion": {
                "administrative_editors": ["Reader"],
                "administrative_validators": ["Reader"],
                "technical_editors": ["Reader"],
                "technical_editors_environement": None,
                "survey_editors": ["Reader"],
                "Plantation_editors": ["Reader", "Editor", "Contributor"],
                "Plantation_validators": ["Reader", "Editor", "Contributor"],
                "Access_editors": None,
                "Access_validators": None,
                "urban_readers": ["Reader"],
            },
            "opinion_validation": {
                "Plantation_editors": ["Reader"],
                "Plantation_validators": ["Reader", "Editor", "Reviewer"],
                "Access_editors": None,
                "Access_validators": None,
                "survey_editors": ["Reader"],
                "urban_readers": ["Reader"],
                "technical_editors": ["Reader"],
            },
            "opinion_given": {
                "Plantation_validators": ["Reader"],
                "Plantation_editors": ["Reader"],
                "Access_editors": None,
                "Access_validators": None,
                "administrative_editors": ["Reader"],
                "survey_editors": ["Reader"],
                "urban_readers": ["Reader"],
                "technical_editors": ["Reader"],
            }
        },
        "demande-davis-access": {
            "creation": {
                "administrative_editors": ["Reader", "Editor"],
                "administrative_validators": ["Reader", "Editor"],
                "opinions_editors": None,
                "survey_editors": ["Reader"],
                "Plantation_editors": None,
                "Plantation_validators": None,
                "Access_editors": None,
                "Access_validators": None,
                "urban_readers": ["Reader"],
                "technical_editors": ["Reader"],
            },
            "waiting_opinion": {
                "administrative_editors": ["Reader"],
                "administrative_validators": ["Reader"],
                "technical_editors": ["Reader"],
                "technical_editors_environement": None,
                "survey_editors": ["Reader"],
                "Plantation_editors": None,
                "Plantation_validators": None,
                "Access_editors": ["Reader", "Editor", "Contributor"],
                "Access_validators": ["Reader", "Editor", "Contributor"],
                "urban_readers": ["Reader"],
            },
            "opinion_validation": {
                "Plantation_validators": None,
                "Plantation_editors": None,
                "Access_editors": ["Reader"],
                "Access_validators": ["Reader", "Editor", "Reviewer"],
                "survey_editors": ["Reader"],
                "urban_readers": ["Reader"],
                "technical_editors": ["Reader"],
            },
            "opinion_given": {
                "Plantation_validators": None,
                "Plantation_editors": None,
                "Access_editors": ["Reader"],
                "Access_validators": ["Reader"],
                "administrative_editors": ["Reader"],
                "survey_editors": ["Reader"],
                "urban_readers": ["Reader"],
                "technical_editors": ["Reader"],
            }
        }
    }

    workflow = [
        "creation",
        "waiting_opinion",
        "opinion_validation",
        "opinion_given",
    ]

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.urban = self.portal.urban
        self.portal_urban = self.portal.portal_urban
        self.common_matrice = {}
        self.mapping_user_group = {
            "administrative_editors": "rich",
            "administrative_validators": "rach",
            "technical_editors": "gert",
            "technical_editors_environement": "gert_e",
            "Voirie_editors": "voirie_edit",
            "Voirie_validators": "voirie_valid",
            "survey_editors": "survivor",
            "urban_readers": "urb_read",
            "opinions_editors": "opi_edit",
        }
        email = 'dll@imio.be'

        with api.env.adopt_roles(["Manager"]):
            add_internal_service = AddInternalServiceForm(
                self.portal_urban, self.request
            )
            # create internal service

            services = [
                "Voirie",
                "Access",
                "Plantation",
                "SSSP",
                "EDII",
                "Am_territoire",
                "Bic",
                "Logement",
                "Zip-qi"
            ]
            for service in services:
                add_internal_service.create_groups(service, service)
                add_internal_service.set_registry_mapping(
                    service.lower(),
                    service,
                    "{}_editors".format(service),
                    "{}_validators".format(service),
                    "",
                    "",
                )
                self.common_matrice["{}_editors".format(service)] = None
                self.common_matrice["{}_validators".format(service)] = None

                username_edit = "{}_edit_user".format(service)
                user_edit = api.user.create(
                    email=email,
                    username=username_edit,
                    password=username_edit
                )
                api.group.add_user(
                    groupname="{}_editors".format(service),
                    user=user_edit
                )
                self.mapping_user_group["{}_editors".format(service)] = (
                    "{}_edit_user".format(service)
                )

                username_valid = "{}_valid_user".format(service)
                user_valid = api.user.create(
                    email=email,
                    username=username_valid,
                    password=username_valid
                )
                api.group.add_user(
                    groupname="{}_validators".format(service),
                    user=user_valid
                )
                self.mapping_user_group["{}_validators".format(service)] = (
                    "{}_valid_user".format(service)
                )

            username = "urb_read"
            user = api.user.create(
                email=email,
                username=username,
                password=username
            )
            api.group.add_user(
                groupname="urban_readers",
                user=user
            )

            username = "opi_edit"
            user = api.user.create(
                email=email,
                username=username,
                password=username
            )
            api.group.add_user(
                groupname="opinions_editors",
                user=user
            )

            # create opinion ask event
            codt_buildlicence_event = self.portal_urban["codt_buildlicence"]["eventconfigs"]
            api.content.create(
                type="OpinionEventConfig",
                title="Demande d'avis (plantation)",
                abbreviation="Plantation",
                id="demande-avis-plantation",
                container=codt_buildlicence_event,
                is_internal_service=True,
                internal_service="plantation",
                eventPortalType="UrbanEventOpinionRequest",
                eventType=["liege.urban.interfaces.IInternalOpinionRequestEvent"],
                activatedFields=["externalDecision"],
                TALCondition="python: event.mayAddOpinionRequestEvent(here)",
            )
            api.content.create(
                type="OpinionEventConfig",
                title="Demande d'avis (ACCESS+)",
                abbreviation="ACCESS+",
                id="demande-avis-access",
                container=codt_buildlicence_event,
                is_internal_service=True,
                internal_service="access",
                eventPortalType="UrbanEventOpinionRequest",
                eventType=["liege.urban.interfaces.IInternalOpinionRequestEvent"],
                activatedFields=["externalDecision"],
                TALCondition="python: event.mayAddOpinionRequestEvent(here)",
            )
            api.content.create(
                type="EventConfig",
                title=u"*** Demande d'avis CONFIG ***",
                id="config-opinion-request",
                container=codt_buildlicence_event,
                eventPortalType="UrbanEventOpinionRequest",
                eventType=["Products.urban.interfaces.IOpinionRequest"],
                activatedFields=[
                    "transmitDate",
                    "receiptDate",
                    "externalDecision",
                    "opinionText",
                    "adviceAgreementLevel",
                ],
                TALCondition="python: False",
            )

            # add ask opinion to licence
            self.licence = api.content.create(
                type="CODT_BuildLicence",
                container=self.urban["codt_buildlicences"],
                title="Test",
            )
            self.licence.setSolicitOpinionsToOptional(
                (
                    "demande-avis-plantation",
                    "demande-avis-access",
                )
            )
            self.licence.createAllAdvices()

    def assertRoles(self, username, context, expected_roles):
        """Parameters:
        - username: str   username of the user to test
        - context: obj   Plone content object
        - expected_roles: list[str]   list of roles
        """
        if expected_roles is None:
            expected_roles = []
        roles = api.user.get_roles(username=username, obj=context)
        ignored_roles = ("Authenticated", "Owner", "UrbanMapReader", "Member")
        for role in ignored_roles:
            if role in roles:
                roles.remove(role)
        self.assertListEqual(
            sorted(roles),
            sorted(expected_roles),
        )

    def execute_matrice_test(self, event, workflow_exception=None):
        print("Event: {}".format(event))
        config = self.matrice.get(event, None)
        obj = self.licence[event]
        if config is None:
            return
        for state in self.workflow:
            group_mapping = config.get(state, None)
            if group_mapping is None:
                continue

            new_group_mapping = self.common_matrice.copy()
            new_group_mapping.update(group_mapping)

            print("State: {}".format(state))
            user_workflow = "admin"
            if workflow_exception and state in workflow_exception:
                user_workflow = workflow_exception[state]

            with api.env.adopt_user(username=user_workflow):
                api.content.transition(
                    obj=obj,
                    to_state=state
                )

            for group, roles in new_group_mapping.items():
                print("Group: {}".format(group))
                username = self.mapping_user_group.get(group, None)
                if username is None:
                    continue
                self.assertRoles(
                    username=username,
                    context=obj,
                    expected_roles=roles
                )

    def tearDown(self):
        with api.env.adopt_roles(["Manager"]):
            api.content.delete(self.licence)

    def test_access(self):
        with api.env.adopt_roles(["Manager"]):
            avis_plantation = self.licence["demande-davis-plantation"]
            avis_access = self.licence["demande-davis-access"]
            self.assertRoles("admin", avis_plantation, ["Manager"])
            self.assertRoles("admin", avis_access, ["Manager"])
            self.execute_matrice_test(
                "demande-davis-access",
                workflow_exception={"opinion_validation": "Access_edit_user"}
            )

    def test_plantation(self):
        with api.env.adopt_roles(["Manager"]):
            avis_plantation = self.licence["demande-davis-plantation"]
            avis_access = self.licence["demande-davis-access"]
            self.assertRoles("admin", avis_plantation, ["Manager"])
            self.assertRoles("admin", avis_access, ["Manager"])
            self.execute_matrice_test(
                "demande-davis-plantation",
                workflow_exception={"opinion_validation": "Plantation_edit_user"}
            )
