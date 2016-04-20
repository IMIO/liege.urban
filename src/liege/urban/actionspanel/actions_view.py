# -*- coding: utf-8 -*-

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
        transitions = {
            'BuildLicence.ask_address_validation': 'simpleconfirm_view',
            'BuildLicence.validate_address': 'simpleconfirm_view',
        }
        return transitions
