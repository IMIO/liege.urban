# -*- coding: utf-8 -*-

from Products.urban.workflows.adapter import LocalRoleAdapter


class StateRolesMapping(LocalRoleAdapter):
    """ """

    mapping = {
        'Requests_discount__notice': {
            'administrative_editors': ('Editor',),
        },
        'address_validating': {
            'administrative_editors': ('Editor',),
            'technical_validators': ('Editor',),
            'administrative_validators': ('Reader',),
        },
        'analysis_report': {
            'technical_validators': ('Editor',),
            'technical_editors': ('Reader',),
        },
        'analysis_report_resume': {
            'technical_validators': ('Editor',),
            'technical_editors': ('Reader',),
        },
        'college_opinion_after_investigation': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Reader',),
        },
        'complete': {
            'administrative_editors': ('Editor',),
        },
        'delivry_licence_by_commune': {
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
        },
        'delivry_licence_by_spw': {
            'technical_editors': ('Editor',),
            'technical_validators': ('Editor',),
        },
        'deposite_complement': {
            'administrative_editors': ('Editor',),
        },
        'deposite_folder': {
            'administrative_editors': ('Editor',),
        },
        'folder_sending_to_spw': {
            'administrative_editors': ('Editor',),
        },
        'inadmissible': {
            'administrative_editors': ('Editor',),
        },
        'incomplete': {
            'administrative_editors': ('Editor',),
        },
        'notification': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Reader',),
        },
        'public_investigation': {
            'administrative_editors': ('Editor',),
            'administrative_validators': ('Reader',),
        },
        'rapport_resume_spw': {
            'administrative_editors': ('Editor',),
        },
        'rubrics_identifications': {
            'technical_validators': ('Editor',),
        },
        'sending_college_notice_spw': {
            'administrative_editors': ('Editor',),
        },
        'sending_deposite_complement_spw': {
            'administrative_editors': ('Editor',),
        },
        'technical_pre_analysis': {
            'administrative_editors': ('Editor',),
        },
    }
