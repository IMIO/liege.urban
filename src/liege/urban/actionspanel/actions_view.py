# -*- coding: utf-8 -*-

from plone import api

from Products.urban.browser.actionspanel.actionspanel import LicenceActionsPanelView


class UrbanTransitionsPanelView(LicenceActionsPanelView):
    """
      This manage the view displaying workflow transitions on context.
    """
    def __init__(self, context, request):
        super(UrbanTransitionsPanelView, self).__init__(context, request)

        self.SECTIONS_TO_RENDER = (
            'renderTransitions',
        )

    def _transitionsToConfirm(self):
        portal_workflow = api.portal.get_tool('portal_workflow')
        transitions = portal_workflow.buildlicence_workflow.transitions.objectIds()

        to_confirm = dict([('BuildLicence.%s' % tr, 'simpleconfirm_view') for tr in transitions])

        return to_confirm
