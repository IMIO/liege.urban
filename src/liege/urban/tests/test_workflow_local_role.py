# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from Products.urban.testing import URBAN_TESTS_LICENCES_FUNCTIONAL
from Products.urban.browser.urbanconfigview import AddInternalServiceForm
from plone import api

import unittest

class TestOpinionsrequestWorkflow(unittest.TestCase):

    layer = URBAN_TESTS_LICENCES_FUNCTIONAL

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
        self.urban = self.portal.urban
        self.portal_urban = self.portal.portal_urban

        add_internal_service = AddInternalServiceForm()
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

        # create opinion ask event
        codt_buildlicence_event = self.portal_urban["codt_buildlicence"]["eventconfigs"]
        api.content.create(
            type="OpinionEventConfig",
            title="Demande d'avis (plantation)",
            container=codt_buildlicence_event,
            is_internal_service=True,
            internal_service="plantation",
        )
        api.content.create(
            type="OpinionEventConfig",
            title="Demande d'avis (ACCESS+)",
            container=codt_buildlicence_event,
            is_internal_service=True,
            internal_service="access",
        )

        # add ask opinion to licence
        