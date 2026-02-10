# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from Products.urban.testing import URBAN_TESTS_LICENCES
from Products.urban.browser.urbanconfigview import AddInternalServiceForm
from plone import api

import unittest

class TestOpinionsrequestWorkflow(unittest.TestCase):

    layer = URBAN_TESTS_LICENCES

    matrice = {
        "plantation":{
            "creation": {
                "administrative_editors" : ["Editor"],
                "administrative_validators" : ["Contributor"],
                "opinions_editors" : ["Reader"],
                "Voirie_editors" : ["Reader"],
                "Voirie_validators" : ["Reader"],
                "survey_editors" : ["Reader"],
                "Plantation_editors": None,
                "Plantation_validators": None,
                "Access_editors": None,
                "Access_validators": None,
                "urban_readers": ["Reader"],
            },
            "waiting_opinion": {
                "administrative_editors" : ["Reader"],
                "administrative_validators" : ["Reader"],
                "technical_editors": ["Editor"],
                "technical_editors_environement": ["Editor"],
                "Voirie_editors" : ["Reader"],
                "Voirie_validators" : ["Reader"],
                "survey_editors" : ["Reader"],
                "Plantation_validators": None,
                "Access_editors": None,
                "Access_validators": None,
                "Plantation_editors": ["Editor"],
                "urban_readers": ["Reader"],
            },
            "opinion_validation": {
                "Voirie_editors" : ["Reader"],
                "Voirie_validators" : ["Reader"],
                "Plantation_validators": ["Reader"],
                "Plantation_editors": ["Reader", "Contributor"],
                "Access_editors": None,
                "Access_validators": None,
                "survey_editors" : ["Reader"],
                "urban_readers": ["Reader"],
            },
            "opinion_given": {
                "Voirie_editors" : ["Reader"],
                "Voirie_validators" : ["Reader"],
                "Plantation_validators": ["Reader"],
                "Plantation_editors": ["Reader"],
                "Access_editors": None,
                "Access_validators": None,
                "administrative_editors" : ["Reader"],
                "survey_editors" : ["Reader"],
                "urban_readers": ["Reader"],
            }
        },
        "access":{
            "creation": {
                "administrative_editors" : ["Editor"],
                "administrative_validators" : ["Contributor"],
                "opinions_editors" : ["Reader"],
                "Voirie_editors" : ["Reader"],
                "Voirie_validators" : ["Reader"],
                "survey_editors" : ["Reader"],
                "Plantation_editors": None,
                "Plantation_validators": None,
                "Access_editors": None,
                "Access_validators": None,
                "urban_readers": ["Reader"],
            },
            "waiting_opinion": {
                "administrative_editors" : ["Reader"],
                "administrative_validators" : ["Reader"],
                "technical_editors": ["Editor"],
                "technical_editors_environement": ["Editor"],
                "Voirie_editors" : ["Reader"],
                "Voirie_validators" : ["Reader"],
                "survey_editors" : ["Reader"],
                "Plantation_validators": None,
                "Access_editors": ["Editor"],
                "Access_validators": None,
                "Plantation_editors": None,
                "urban_readers": ["Reader"],
            },
            "opinion_validation": {
                "Voirie_editors" : ["Reader"],
                "Voirie_validators" : ["Reader"],
                "Plantation_validators": None,
                "Plantation_editors": None,
                "Access_editors": ["Reader", "Contributor"],
                "Access_validators": ["Reader"],
                "survey_editors" : ["Reader"],
                "urban_readers": ["Reader"],
            },
            "opinion_given": {
                "Voirie_editors" : ["Reader"],
                "Voirie_validators" : ["Reader"],
                "Plantation_validators": None,
                "Plantation_editors": None,
                "Access_editors": ["Reader"],
                "Access_validators": ["Reader"],
                "administrative_editors" : ["Reader"],
                "survey_editors" : ["Reader"],
                "urban_readers": ["Reader"],
            }
        }
    }

    def setUp(self):
        self.portal = self.layer["portal"]
        self.request = self.layer["request"]
        self.urban = self.portal.urban
        self.portal_urban = self.portal.portal_urban

        with api.env.adopt_roles(['Manager']):
            add_internal_service = AddInternalServiceForm(self.portal_urban, self.request)
            # create internal service
            service_id = "plantation"
            service_name = "plantation"
            editor_group_id, validator_group_id = add_internal_service.create_groups(
                service_id.capitalize(), service_name
            )
            add_internal_service.set_registry_mapping(
                service_id,
                service_name,
                editor_group_id,
                validator_group_id,
                "",
                "",
            )

            service_id = "access"
            service_name = "Access +"
            editor_group_id, validator_group_id = add_internal_service.create_groups(
                service_id.capitalize(), service_name
            )
            add_internal_service.set_registry_mapping(
                service_id,
                service_name,
                editor_group_id,
                validator_group_id,
                "",
                "",
            )
            
            # XXX Add one user to each groups

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
        roles = api.user.get_roles(username=username, obj=context)
        ignored_roles = ("Authenticated", "Owner")
        for role in ignored_roles:
            if role in roles:
                roles.remove(role)
        self.assertListEqual(
            sorted(roles),
            sorted(expected_roles),
        )

    def tearDown(self):
        with api.env.adopt_roles(['Manager']):
            api.content.delete(self.licence)

    def test_access(self):
        with api.env.adopt_roles(['Manager']):
            avis_plantation = self.licence["demande-davis-plantation"]
            avis_access = self.licence["demande-davis-access"]
            self.assertRoles("admin", avis_plantation, ["Manager"])
            self.assertRoles("admin", avis_access, ["Manager"])

    def test_plantation(self):
        with api.env.adopt_roles(['Manager']):
            avis_plantation = self.licence["demande-davis-plantation"]
            avis_access = self.licence["demande-davis-access"]
            self.assertRoles("admin", avis_plantation, ["Manager"])
            self.assertRoles("admin", avis_access, ["Manager"])