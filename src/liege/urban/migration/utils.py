# -*- coding: utf-8 -*-

from plone import api

import transaction


def brain_iterator(catalog, query):
    for brain in catalog.unrestrictedSearchResults(query):
        yield brain


def refresh_workflow_permissions(
    workflow_id,
    folder_path=None,
    for_states=None,
    logger=None,
    transaction_count=1000,
):
    if not folder_path:
        folder_path = '/'.join(api.portal.get().getPhysicalPath())
    portal_workflow = api.portal.get_tool('portal_workflow')
    portal_catalog = api.portal.get_tool('portal_catalog')
    index = 0

    for at_type, wf_ids in portal_workflow._chains_by_type.items():
        if len(wf_ids) < 1:
            continue
        if wf_ids[0] == workflow_id:
            workflow = portal_workflow.getWorkflowById(wf_ids[0])
            query = {
                'path': {'query': folder_path},
                'portal_type': at_type,
            }
            if for_states is not None:
                query["review_state"] = for_states
            if logger is not None:
                length = len(portal_catalog.unrestrictedSearchResults(query))
                logger.info("{0} objects to reindex".format(length))
            for brain in brain_iterator(portal_catalog, query):
                index += 1
                obj = brain.getObject()
                workflow.updateRoleMappingsFor(obj)
                obj.reindexObjectSecurity()
                obj.reindexObject(idxs=['allowedRolesAndUsers'])
                if index % transaction_count == 0:
                    transaction.commit()
                    if logger is not None:
                        logger.info("Commit {0} / {1}".format(index, length))
            transaction.commit()
            if logger is not None:
                logger.info("Commit {0} / {1}".format(index, length))
