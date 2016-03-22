# -*- coding: utf-8 -*-

from collective.z3cform.rolefield.utils import add_local_roles_to_principals
from collective.z3cform.rolefield.utils import remove_local_roles_from_principals

from liege.urban.workflows.interfaces import IWorkflowStateRolesMapping

from zope.component import queryMultiAdapter


def update_local_roles(obj, event):
    """
    This handler is in charge of updating the local roles of an object
    depending on the mapping role/group found for the new state of this
    object's workflow.
    """

    # get workflow role/group mapping for which the transition was triggered
    workflow = event.workflow
    mapping = queryMultiAdapter((obj, workflow), IWorkflowStateRolesMapping)

    if not mapping:
        return

    # some local roles can be computed only after the object creation, we
    # need to handle that case specifically
    if not event.transition:
        mapping.object_created = False

    # update objects local roles by removing each local role found on the
    # mapping for the old state
    old_state = event.old_state.title
    old_state_local_roles = mapping.get_group_roles_mapping_of(old_state)

    for group, roles in old_state_local_roles.iteritems():
        remove_local_roles_from_principals(obj, [group], roles)

    # update objects local roles by adding each local role found on the
    # mapping for the new state
    new_state = event.new_state.title
    new_state_local_roles = mapping.get_group_roles_mapping_of(new_state)

    for group, roles in new_state_local_roles.iteritems():
        add_local_roles_to_principals(obj, [group], roles)
