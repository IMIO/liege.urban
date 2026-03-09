# encoding: utf-8

from datetime import datetime
from plone import api

import logging
import transaction


logger = logging.getLogger('urban: migrations')


def fix_address_point(context):
    logger = logging.getLogger("urban: fix address point value type")
    brains = api.content.find(
        object_provides=["Products.urban.interfaces.IGenericLicence"],
        sort_on="modified",
        sort_order="reverse",
        sort_limit=2000,
    )[:2000]
    tzinfo = brains[0].modified.asdatetime().tzinfo
    matching_brains = [
        b for b in brains
        if b.modified.asdatetime() > datetime(2026, 2, 22, tzinfo=tzinfo)
    ]
    logger.info("{0} brains concerned".format(len(matching_brains)))
    for brain in matching_brains:
        obj = brain.getObject()
        parcels = obj.listFolderContents(
            contentFilter={"portal_type" : "Parcel"}
        )
        for parcel in parcels:
            if not isinstance(parcel.address_point, int):
                logger.info("fix parcel {0}".format(parcel.absolute_url()))
                parcel.address_point = int(parcel.address_point)
                parcel._p_changed = 1
    logger.info("migration step done!")


def fix_workflow_security(context):
    from liege.urban.migration.utils import refresh_workflow_permissions

    logger = logging.getLogger('urban: Fix workflow security')
    logger.info("starting migration steps")
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile('profile-liege.urban:default', 'workflow')

    urban_folder = api.portal.get()["urban"]
    workflows = {
        "article127_workflow": {
            "folder_path": ["codt_article127s"],
            "states": [
                "abandoned",
                "accepted",
                "complete",
                "decision_in_progress",
                "deposit",
                "procedure_choosen",
                "procedure_validated",
                "refused",
                "report_written",
                "frozen_suspension",
                "validating_address",
                "waiting_address",
                "obsolete",
            ]
        },
        "envclassone_workflow": {
            "folder_path": ["envclassones", "envclasstwos"],
            "states": [
                "deposit",
                "validating_address",
                "waiting_address",
                "checking_completion",
                "complete",
                "incomplete",
                "technical_report_validation",
                "college_in_progress",
                "FT_opinion",
                "technical_synthesis_validation",
                "final_decision_in_progress",
                "inacceptable",
                "authorized",
                "refused",
                "abandoned",
            ],
        },
        "envclassthree_workflow": {
            "folder_path": ["envclassthrees"],
            "states": [
                "deposit",
                "procedure_analysis",
                "inacceptable_validation",
                "acceptable_validation",
                "acceptable_with_conditions_validation",
                "inacceptable",
                "acceptable",
                "acceptable_with_conditions",
                "abandoned",
            ],
        },
        "roaddecree_workflow": {
            "folder_path": ["roaddecrees"],
            "states": [
                "folder_creation",
                "public_investigation",
                "technical_analysis_post_investigation",
                "technical_analysis_validation",
                "college_council_passage",
                "display_in_progress",
                "refused",
                "abandoned",
                "authorized",
            ],
        },
        "ticket_workflow": {
            "folder_path": ["tickets"],
            "states": [
                "creation",
                "prosecution_analysis",
                "technical_analysis",
                "technical_validation",
                "waiting_for_agreement",
                "waiting_to_finalize",
                "in_court",
                "ended",
                "frozen_suspension",
            ],
        },
        "urban_licence_workflow": {
            "folder_path": [
                "codt_urbancertificateones",
                "codt_integratedlicences",
                "envclassborderings",
                "explosivespossessions",
            ],
            "states": [
                "accepted",
                "in_progress",
                "incomplete",
                "refused",
                "inacceptable",
                "retired",
            ],
        },
    }

    for workflow in workflows.keys():
        for folder_name in workflows[workflow]["folder_path"]:
            logger.info(
                "Refresh workflow permissions for {0} in folder {1}".format(
                    workflow, folder_name,
                )
            )
            refresh_workflow_permissions(
                workflow,
                folder_path="/".join(urban_folder[folder_name].getPhysicalPath()),
                for_states=workflows[workflow]["states"]
            )
    logger.info("migration step done!")


def fix_workflow_security_second(context):
    from liege.urban.migration.utils import refresh_workflow_permissions

    logger = logging.getLogger('urban: Fix workflow security')
    logger.info("starting migration steps")
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile('profile-liege.urban:default', 'workflow')

    workflows = {
        "inspection_workflow": {
            "folder_path": [
                "inspections",
            ],
            "states": [
                "administrative_answer",
                "analysis",
                "creation",
                "ended",
                "first_administrative_answer",
                "frozen_suspension",
                "inspection_follow_up",
            ],
        },
        "buildlicence_workflow": {
            "folder_path": [
                "buildlicences",
            ],
            "states": [
                "FD_opinion",
                "abandoned",
                "accepted",
                "authorized",
                "checking_completion",
                "complete",
                "decision_in_progress",
                "deposit",
                "filed_away",
                "frozen_suspension",
                "incomplete",
                "procedure_choosen",
                "procedure_validated",
                "refused",
                "report_written",
                "suspension",
                "validating_address",
                "waiting_address",
            ],
        },
        "article127_workflow": {
            "folder_path": [
                "article127s",
            ],
            "states": [
                "abandoned",
                "accepted",
                "complete",
                "decision_in_progress",
                "deposit",
                "procedure_choosen",
                "procedure_validated",
                "refused",
                "report_written",
                "frozen_suspension",
                "validating_address",
                "waiting_address",
                "obsolete",
            ],
        },
        "urban_licence_workflow": {
            "folder_path": [
                "declarations",
                "uniquelicences",
                "integratedlicences",
                "codt_integratedlicences",
                "codt_urbancertificateones",
            ],
            "states": [
                "accepted",
                "in_progress",
                "inacceptable",
                "incomplete",
                "refused",
                "retired",
            ],
        },
        "codt_buildlicence_workflow": {
            "folder_path": [
                "codt_buildlicences",
                "codt_urbancertificatetwos",
                "codt_commerciallicences",
            ],
            "states": [
                "FD_opinion",
                "abandoned",
                "accepted",
                "authorized",
                "checking_completion",
                "complete",
                "decision_in_progress",
                "deposit",
                "filed_away",
                "frozen_suspension",
                "incomplete",
                "obsolete_accept",
                "obsolete_authorized",
                "procedure_choosen",
                "procedure_validated",
                "refused",
                "report_written",
                "suspension",
                "validating_address",
                "waiting_address",
            ],
        }
    }

    urban_folder = api.portal.get()["urban"]
    for workflow in workflows.keys():
        for folder_name in workflows[workflow]["folder_path"]:
            logger.info(
                "Refresh workflow permissions for '{0}' in folder '{1}'".format(
                    workflow, folder_name,
                )
            )
            refresh_workflow_permissions(
                workflow,
                folder_path="/".join(urban_folder[folder_name].getPhysicalPath()),
                for_states=workflows[workflow]["states"],
                logger=logger,
            )

    logger.info("migration step done!")


def update_event_workflow(context):
    logger = logging.getLogger('urban: Update event workflow')
    logger.info("starting migration steps")
    setup_tool = api.portal.get_tool('portal_setup')
    setup_tool.runImportStepFromProfile('profile-liege.urban:default', 'workflow')
    logger.info("migration step done!")
