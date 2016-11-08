# -*- coding: utf-8 -*-

from imio.schedule.content.object_factories import CreationConditionObject
from imio.schedule.content.object_factories import EndConditionObject
from imio.schedule.content.object_factories import MacroCreationConditionObject
from imio.schedule.content.object_factories import MacroEndConditionObject
from imio.schedule.content.object_factories import StartConditionObject

schedule_config = {
    'survey_schedule': [
        {
            'type_name': 'TaskConfig',
            'id': 'check_address',
            'title': "Vérifier l'adresse",
            'default_assigned_group': 'survey_editors',
            'default_assigned_user': 'survivor',
            'creation_state': ('validating_address',),
            'starting_states': ('validating_address',),
            'ending_states': ('waiting_address', 'checking_completion'),
            'end_conditions': (
                EndConditionObject('liege.urban.schedule.parcels_validated'),
            ),
            'start_date': 'urban.schedule.start_date.deposit_date',
            'additional_delay': 1,
        },
        {
            'type_name': 'TaskConfig',
            'id': 'assign_temporary_address',
            'title': "Assigner une adresse temporaire",
            'default_assigned_group': 'survey_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('waiting_address',),
            'starting_states': ('waiting_address',),
            'ending_states': ('checking_completion',),
            'end_conditions': (
                EndConditionObject('liege.urban.schedule.parcels_added', 'AND'),
                EndConditionObject('liege.urban.schedule.parcels_validated')
            ),
            'start_date': 'urban.schedule.start_date.deposit_date',
            'additional_delay': 1,
        },
    ],
    'opinions_schedule': [
        {
            'type_name': 'MacroTaskConfig',
            'id': 'ask_road_opinion',
            'title': "Avis voirie",
            'default_assigned_group': 'Voirie_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('creation',),
            'creation_conditions': (
                CreationConditionObject('liege.urban.schedule.is_internal_opinion'),
            ),
            'starting_states': ('waiting_opinion',),
            'ending_states': ('opinions_given',),
            'start_date': 'liege.urban.schedule.asking_date',
            'additional_delay': 15,
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'valide',
                    'title': 'Valider',
                    'default_assigned_group': 'Voirie_validators',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('creation',),
                    'starting_states': ('opinion_validation',),
                    'ending_states': ('opinions_given',),
                    'start_date': 'liege.urban.schedule.asking_date',
                    'additional_delay': 15,
                },
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'ask_sssp_opinion',
            'title': "Avis SSSP",
            'default_assigned_group': 'SSSP_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('creation',),
            'creation_conditions': (
                CreationConditionObject('liege.urban.schedule.is_internal_opinion'),
            ),
            'starting_states': ('waiting_opinion',),
            'ending_states': ('opinions_given',),
            'start_date': 'liege.urban.schedule.asking_date',
            'additional_delay': 15,
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'valide',
                    'title': 'Valider',
                    'default_assigned_group': 'SSSP_validators',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('creation',),
                    'starting_states': ('opinion_validation',),
                    'ending_states': ('opinions_given',),
                    'start_date': 'liege.urban.schedule.asking_date',
                    'additional_delay': 15,
                },
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'ask_access_opinion',
            'title': "Avis Access",
            'default_assigned_group': 'Access_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('creation',),
            'creation_conditions': (
                CreationConditionObject('liege.urban.schedule.is_internal_opinion'),
            ),
            'starting_states': ('waiting_opinion',),
            'ending_states': ('opinions_given',),
            'start_date': 'liege.urban.schedule.asking_date',
            'additional_delay': 15,
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'valide',
                    'title': 'Valider',
                    'default_assigned_group': 'Access_validators',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('creation',),
                    'starting_states': ('opinion_validation',),
                    'ending_states': ('opinions_given',),
                    'start_date': 'liege.urban.schedule.asking_date',
                    'additional_delay': 15,
                },
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'ask_plantation_opinion',
            'title': "Avis Plantation",
            'default_assigned_group': 'Plantation_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('creation',),
            'creation_conditions': (
                CreationConditionObject('liege.urban.schedule.is_internal_opinion'),
            ),
            'starting_states': ('waiting_opinion',),
            'ending_states': ('opinions_given',),
            'start_date': 'liege.urban.schedule.asking_date',
            'additional_delay': 15,
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'valide',
                    'title': 'Valider',
                    'default_assigned_group': 'Plantation_validators',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('creation',),
                    'starting_states': ('opinion_validation',),
                    'ending_states': ('opinions_given',),
                    'start_date': 'liege.urban.schedule.asking_date',
                    'additional_delay': 15,
                },
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'ask_edii_opinion',
            'title': "Avis EDII",
            'default_assigned_group': 'EDII_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('creation',),
            'creation_conditions': (
                CreationConditionObject('liege.urban.schedule.is_internal_opinion'),
            ),
            'starting_states': ('waiting_opinion',),
            'ending_states': ('opinions_given',),
            'start_date': 'liege.urban.schedule.asking_date',
            'additional_delay': 15,
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'valide',
                    'title': 'Valider',
                    'default_assigned_group': 'EDII_validators',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('creation',),
                    'starting_states': ('opinion_validation',),
                    'ending_states': ('opinions_given',),
                    'start_date': 'liege.urban.schedule.asking_date',
                    'additional_delay': 15,
                },
            ]
        },
    ],
    'buildlicence': [
        {
            'type_name': 'TaskConfig',
            'id': 'depot',
            'title': 'Dépôt dossiers',
            'default_assigned_group': 'administrative_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('deposit',),
            'starting_states': ('deposit',),
            'ending_states': ('validating_address',),
            'end_conditions': (
                EndConditionObject('urban.schedule.condition.deposit_done'),
            ),
            'start_date': 'urban.schedule.start_date.creation_date',
            'additional_delay': 0,
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'incomplet',
            'title': 'Incomplet',
            'default_assigned_group': 'administrative_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('incomplete',),
            'starting_states': ('incomplete',),
            'ending_states': ('checking_completion',),
            'start_date': 'schedule.start_date.subtask_highest_due_date',
            'activate_recurrency': True,
            'recurrence_states': ('incomplete',),
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'demande_complements',
                    'title': 'Demander des compléments',
                    'default_assigned_group': 'administrative_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('incomplete',),
                    'starting_states': ('incomplete',),
                    'end_conditions': (
                        EndConditionObject('urban.schedule.condition.complements_asked'),
                    ),
                    'start_date': 'urban.schedule.start_date.deposit_date',
                    'additional_delay': 15,
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'attente_complements',
                    'title': 'En attente de compléments',
                    'default_assigned_group': 'administrative_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('incomplete',),
                    'start_conditions': (
                        StartConditionObject('urban.schedule.condition.complements_asked'),
                    ),
                    'end_conditions': (
                        EndConditionObject('urban.schedule.condition.complements_received'),
                    ),
                    'start_date': None,  # infinite deadline
                },
            ],
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'accuse',
            'title': 'Accusé de réception',
            'default_assigned_group': 'administrative_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('checking_completion',),
            'starting_states': ('checking_completion',),
            'end_conditions': (
                MacroEndConditionObject('urban.schedule.condition.acknowledgment_done'),
            ),
            'start_date': 'urban.schedule.start_date.deposit_date',
            'additional_delay': 15,
            'subtasks': [
                {
                    'type_name': 'MacroTaskConfig',
                    'id': 'rediger-accuse',
                    'title': 'Rédiger accusé',
                    'default_assigned_group': 'administrative_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('checking_completion',),
                    'starting_states': ('checking_completion',),
                    'end_conditions': (
                        MacroEndConditionObject('liege.urban.schedule.acknowledgment_written'),
                    ),
                    'start_date': 'urban.schedule.start_date.deposit_date',
                    'additional_delay': 13,
                    'subtasks': [
                        {
                            'type_name': 'TaskConfig',
                            'id': 'verif_complet',
                            'title': 'Vérification de la complétude',
                            'default_assigned_group': 'technical_editors',
                            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                            'creation_state': ('checking_completion',),
                            'starting_states': ('checking_completion',),
                            'ending_states': ('complete', 'incomplete'),
                            'start_date': 'urban.schedule.start_date.deposit_date',
                            'recurrence_states': ('checking_completion'),
                            'activate_recurrency': True,
                            'additional_delay': 11,
                        },
                        {
                            'type_name': 'MacroTaskConfig',
                            'id': 'choix',
                            'title': 'Choix de la procédure',
                            'default_assigned_group': 'technical_editors',
                            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                            'creation_state': ('complete',),
                            'starting_states': ('complete',),
                            'ending_states': ('procedure_choosen',),
                            'start_date': 'urban.schedule.start_date.deposit_date',
                            'additional_delay': 11,
                            'subtasks': [
                                {
                                    'type_name': 'TaskConfig',
                                    'id': 'rayon-enquete',
                                    'title': 'Identifier la zone d\'enquête',
                                    'default_assigned_group': 'technical_editors',
                                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                                    'creation_conditions': (
                                        CreationConditionObject('urban.schedule.condition.will_have_inquiry'),
                                    ),
                                    'end_conditions': (
                                        EndConditionObject('urban.schedule.condition.inquiry_event_created', 'AND'),
                                        EndConditionObject('liege.urban.schedule.inquiry_zone_identified'),
                                    ),
                                    'start_date': 'urban.schedule.start_date.deposit_date',
                                    'additional_delay': 11,
                                },
                            ],
                        },
                        {
                            'type_name': 'TaskConfig',
                            'id': 'validate_procedure',
                            'title': 'Valider la procédure',
                            'default_assigned_group': 'technical_validators',
                            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                            'creation_state': ('procedure_choosen',),
                            'starting_states': ('procedure_choosen',),
                            'ending_states': ('procedure_validated',),
                            'start_date': 'urban.schedule.start_date.deposit_date',
                            'additional_delay': 12,
                        },
                        {
                            'type_name': 'TaskConfig',
                            'id': 'enquete-dates',
                            'title': 'Définir les dates de d\'enquête',
                            'default_assigned_group': 'administrative_editors',
                            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                            'creation_state': ('procedure_validated',),
                            'creation_conditions': (
                                CreationConditionObject('urban.schedule.condition.will_have_inquiry'),
                            ),
                            'end_conditions': (
                                EndConditionObject('urban.schedule.condition.inquiry_dates_defined'),
                            ),
                            'start_date': 'urban.schedule.start_date.deposit_date',
                            'additional_delay': 13,
                        },
                    ],
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'valider-accuse',
                    'title': 'Valider accusé',
                    'default_assigned_group': 'administrative_validators',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('checking_completion',),
                    'start_conditions': (
                        StartConditionObject('liege.urban.schedule.acknowledgment_written'),
                    ),
                    'end_conditions': (
                        EndConditionObject('liege.urban.schedule.acknowledgment_validated'),
                    ),
                    'start_date': 'urban.schedule.start_date.deposit_date',
                    'additional_delay': 14,
                }
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'valider-analyse',
            'title': 'Valider analyse',
            'default_assigned_group': 'technical_validators',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('procedure_validated',),
            'creation_conditions': (
                MacroCreationConditionObject('urban.schedule.condition.acknowledgment_done'),
            ),
            'starting_states': ('procedure_validated',),
            'ending_states': ('decision_in_progress', 'FD_opinion'),
            'start_date': 'urban.schedule.start_date.acknowledgment_date',
            'calculation_delay': (
                'urban.schedule.delay.annonced_delay',
            ),
            'additional_delay': 0,
            'subtasks': [
                {
                    'type_name': 'MacroTaskConfig',
                    'id': 'rediger-analyse',
                    'title': 'Rédiger analyse',
                    'default_assigned_group': 'technical_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('procedure_validated',),
                    'starting_states': ('procedure_validated',),
                    'ending_states': ('report_written',),
                    'start_date': 'urban.schedule.start_date.acknowledgment_date',
                    'additional_delay': 5,
                    'subtasks': [
                        {
                            'type_name': 'MacroTaskConfig',
                            'id': 'avis-services',
                            'title': 'Avis de services',
                            'default_assigned_group': 'technical_editors',
                            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                            'marker_interfaces': [u'Products.urban.schedule.interfaces.IReceiveOpinionRequestsTask'],
                            'creation_state': ('procedure_validated',),
                            'creation_conditions': (
                                MacroCreationConditionObject('urban.schedule.condition.has_opinion_requests'),
                            ),
                            'starting_states': ('procedure_validated',),
                            'end_conditions': (
                                MacroEndConditionObject('urban.schedule.condition.opinion_requests_done'),
                            ),
                            'start_date': 'urban.schedule.start_date.acknowledgment_date',
                            'additional_delay': 33,
                            'subtasks': [
                                {
                                    'type_name': 'MacroTaskConfig',
                                    'id': 'documents-avis',
                                    'title': 'Envoyer les demandes d\'avis',
                                    'default_assigned_group': 'administrative_editors',
                                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                                    'marker_interfaces': [u'Products.urban.schedule.interfaces.ISendOpinionRequestsTask'],
                                    'creation_state': ('procedure_validated',),
                                    'creation_conditions': (
                                        MacroCreationConditionObject('urban.schedule.condition.has_opinion_requests'),
                                    ),
                                    'starting_states': ('procedure_validated',),
                                    'end_conditions': (
                                        MacroEndConditionObject('liege.urban.schedule.opinion_requests_waiting'),
                                    ),
                                    'start_date': 'urban.schedule.start_date.acknowledgment_date',
                                    'additional_delay': 0,
                                    'subtasks': [
                                        {
                                            'type_name': 'TaskConfig',
                                            'id': 'demander-avis',
                                            'title': 'Créer les événements',
                                            'default_assigned_group': 'technical_editors',
                                            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                                            'marker_interfaces': [u'Products.urban.schedule.interfaces.ICreateOpinionRequestsTask'],
                                            'creation_state': ('procedure_validated',),
                                            'creation_conditions': (
                                                CreationConditionObject('urban.schedule.condition.has_opinion_requests'),
                                            ),
                                            'starting_states': ('procedure_validated',),
                                            'end_conditions': (
                                                EndConditionObject('urban.schedule.condition.opinion_requests_created'),
                                            ),
                                            'start_date': 'urban.schedule.start_date.acknowledgment_date',
                                            'additional_delay': 0,
                                        },
                                    ],
                                },
                            ]
                        },
                        {
                            'type_name': 'MacroTaskConfig',
                            'id': 'enquete',
                            'title': 'Enquête publique',
                            'default_assigned_group': 'technical_editors',
                            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                            'creation_state': ('procedure_validated',),
                            'creation_conditions': (
                                MacroCreationConditionObject('urban.schedule.condition.acknowledgment_done', 'AND'),
                                MacroCreationConditionObject('urban.schedule.condition.has_inquiry'),
                            ),
                            'starting_states': ('procedure_validated',),
                            'end_conditions': (
                                MacroEndConditionObject('urban.schedule.condition.inquiry_done'),
                            ),
                            'start_date': 'urban.schedule.start_date.inquiry_end_date',
                            'additional_delay': 1,
                            'subtasks': [
                                {
                                    'type_name': 'TaskConfig',
                                    'id': 'enquete-documents',
                                    'title': 'Produire les documents',
                                    'default_assigned_group': 'administrative_editors',
                                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                                    'creation_state': ('procedure_validated',),
                                    'creation_conditions': (
                                        CreationConditionObject('urban.schedule.condition.has_inquiry'),
                                    ),
                                    'end_conditions': (
                                        EndConditionObject('liege.urban.schedule.inquiry_documents_done'),
                                    ),
                                    'start_date': 'urban.schedule.start_date.acknowledgment_date',
                                },
                                {
                                    'type_name': 'TaskConfig',
                                    'id': 'valider-documents',
                                    'title': 'Valider les documents',
                                    'default_assigned_group': 'administrative_validators',
                                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                                    'creation_conditions': (
                                        CreationConditionObject('urban.schedule.condition.has_inquiry'),
                                    ),
                                    'start_conditions': (
                                        StartConditionObject('liege.urban.schedule.inquiry_documents_done'),
                                    ),
                                    'end_conditions': (
                                        EndConditionObject('liege.urban.schedule.inquiry_documents_validated'),
                                    ),
                                    'start_date': 'urban.schedule.start_date.acknowledgment_date',
                                },
                                {
                                    'type_name': 'TaskConfig',
                                    'id': 'envoyer-documents',
                                    'title': 'Envoyer les documents',
                                    'default_assigned_group': 'administrative_editors',
                                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                                    'creation_conditions': (
                                        CreationConditionObject('urban.schedule.condition.has_inquiry'),
                                    ),
                                    'start_conditions': (
                                        StartConditionObject('liege.urban.schedule.inquiry_documents_validated'),
                                    ),
                                    'end_conditions': (
                                        EndConditionObject('liege.urban.schedule.inquiry_documents_sent'),
                                    ),
                                    'start_date': 'urban.schedule.start_date.acknowledgment_date',
                                },
                            ]
                        },
                    ]
                },
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'avis-fd',
            'title': 'Avis du FD',
            'default_assigned_group': 'administrative_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('procedure_validated', 'FD_opinion'),
            'creation_conditions': (
                MacroCreationConditionObject('liege.urban.schedule.only_need_FD_opinion', 'OR'),
                MacroCreationConditionObject('liege.urban.schedule.licence_state_is_FD_opinion'),
            ),
            'starting_states': ('procedure_validated', 'FD_opinion'),
            'ending_states': ('decision_in_progress',),
            'end_conditions': (
                MacroEndConditionObject('liege.urban.schedule.FD_opinion_received'),
            ),
            'start_date': 'urban.schedule.start_date.inquiry_end_date',
            'subtasks': [
                {
                    'type_name': 'MacroTaskConfig',
                    'id': 'premier-passage',
                    'title': 'Premier passage collège',
                    'default_assigned_group': 'technical_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('procedure_validated', 'FD_opinion'),
                    'starting_states': ('procedure_validated', 'FD_opinion'),
                    'start_date': 'schedule.start_date.subtask_highest_due_date',
                    'end_conditions': (
                        MacroEndConditionObject('liege.urban.schedule.FD_project_college_done'),
                    ),
                    'start_date': 'schedule.start_date.task_starting_date',
                    'additional_delay': 2,
                    'subtasks': [
                        {
                            'type_name': 'TaskConfig',
                            'id': 'rediger-projet-avis',
                            'title': 'Rédiger le projet d\'avis',
                            'default_assigned_group': 'administrative_editors',
                            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                            'creation_state': ('procedure_validated', 'FD_opinion'),
                            'starting_states': ('procedure_validated', 'FD_opinion'),
                            'end_conditions': (
                                EndConditionObject('liege.urban.schedule.FD_project_writen'),
                            ),
                            'additional_delay': 2,
                            'start_date': 'schedule.start_date.task_starting_date',
                        },
                        {
                            'type_name': 'TaskConfig',
                            'id': 'valider-projet-avis',
                            'title': 'Valider le projet d\'avis',
                            'default_assigned_group': 'administrative_validators',
                            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                            'creation_state': ('procedure_validated', 'FD_opinion'),
                            'starting_states': ('procedure_validated', 'FD_opinion'),
                            'start_conditions': (
                                StartConditionObject('liege.urban.schedule.FD_project_writen'),
                            ),
                            'end_conditions': (
                                EndConditionObject('liege.urban.schedule.FD_project_validated', 'AND'),
                                EndConditionObject('liege.urban.schedule.FD_project_sent_to_college'),
                            ),
                            'start_date': 'schedule.start_date.task_starting_date',
                            'additional_delay': 2,
                        },
                    ]
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'envoyer-avis-FD',
                    'title': 'Envoyer la demande d\'avis',
                    'default_assigned_group': 'technical_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('procedure_validated', 'FD_opinion'),
                    'starting_states': ('procedure_validated', 'FD_opinion'),
                    'start_conditions': (
                        StartConditionObject('liege.urban.schedule.FD_project_college_done'),
                    ),
                    'end_conditions': (
                        EndConditionObject('liege.urban.schedule.FD_opinion_asked'),
                    ),
                    'start_date': 'schedule.start_date.task_starting_date',
                    'additional_delay': 2,
                },
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'decision-finale',
            'title': 'Décision finale à notifier',
            'default_assigned_group': 'administrative_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('decision_in_progress',),
            'starting_states': ('decision_in_progress',),
            'ending_states': ('accepted', 'refused'),
            'end_conditions': (
                MacroEndConditionObject('liege.urban.schedule.decision_notified'),
            ),
            'start_date': 'schedule.start_date.subtask_highest_due_date',
            'additional_delay': 2,
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'rediger-proposition-decision',
                    'title': 'Rédiger le projet de permis',
                    'default_assigned_group': 'administrative_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('decision_in_progress',),
                    'starting_states': ('decision_in_progress',),
                    'end_conditions': (
                        EndConditionObject('liege.urban.schedule.decision_project_drafted'),
                    ),
                    'start_date': 'schedule.start_date.task_starting_date',
                    'calculation_delay': (
                        'urban.schedule.delay.annonced_delay',
                    ),
                    'additional_delay': -7,
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'envoyer-proposition-decision',
                    'title': 'Valider et envoyer vers IA délib',
                    'default_assigned_group': 'administrative_validators',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('decision_in_progress',),
                    'starting_states': ('decision_in_progress',),
                    'start_conditions': (
                        StartConditionObject('liege.urban.schedule.decision_project_drafted'),
                    ),
                    'end_conditions': (
                        EndConditionObject('liege.urban.schedule.decision_project_sent'),
                    ),
                    'start_date': 'schedule.start_date.task_starting_date',
                    'additional_delay': 2,
                },
            ]
        },
    ],
    'preliminarynotice': [
        {
            'type_name': 'TaskConfig',
            'id': 'depot',
            'title': 'Dépôt de la demande',
            'default_assigned_group': 'administrative_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('deposit',),
            'starting_states': ('deposit',),
            'ending_states': ('analysis',),
            'start_date': 'urban.schedule.start_date.creation_date',
            'additional_delay': 0,
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'analysis_validation',
            'title': 'Valider l\'analyse',
            'default_assigned_group': 'technical_validators',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('analysis',),
            'starting_states': ('analysis',),
            'ending_states': ('college_in_progress',),
            'start_date': 'urban.schedule.start_date.creation_date',
            'additional_delay': 5,
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'analysis',
                    'title': 'Analyse',
                    'default_assigned_group': 'technical_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('analysis',),
                    'starting_states': ('analysis',),
                    'ending_states': ('analysis_proposition',),
                    'start_date': 'urban.schedule.start_date.creation_date',
                    'additional_delay': 4,
                    'activate_recurrency': True,
                    'recurrence_states': ('analysis',),
                },
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'valider-reponse',
            'title': 'Valider le projet de réponse',
            'default_assigned_group': 'administrative_validators',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('college_in_progress',),
            'starting_states': ('college_in_progress',),
            'end_conditions': (
                MacroEndConditionObject('liege.urban.schedule.notification_project_validated'),
            ),
            'start_date': 'schedule.start_date.subtask_highest_due_date',
            'additional_delay': 2,
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'envoi-college',
                    'title': 'Préparer et envoyer vers IA délib',
                    'default_assigned_group': 'administrative_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('college_in_progress',),
                    'starting_states': ('college_in_progress',),
                    'end_conditions': (
                        EndConditionObject('liege.urban.schedule.college_project_sent'),
                    ),
                    'start_date': 'schedule.start_date.task_starting_date',
                    'additional_delay': 2,
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'passage-college',
                    'title': 'Passage au collège',
                    'default_assigned_group': 'administrative_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('college_in_progress',),
                    'starting_states': ('college_in_progress',),
                    'start_conditions': (
                        StartConditionObject('liege.urban.schedule.college_project_sent'),
                    ),
                    'end_conditions': (
                        EndConditionObject('liege.urban.schedule.college_done'),
                    ),
                    'start_date': 'schedule.start_date.task_starting_date',
                    'additional_delay': 2,
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'rediger-projet-reponse',
                    'title': 'Rédiger le projet de réponse',
                    'default_assigned_group': 'administrative_editors',
                    'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
                    'creation_state': ('decision_in_progress',),
                    'starting_states': ('decision_in_progress',),
                    'start_conditions': (
                        StartConditionObject('liege.urban.schedule.college_done'),
                    ),
                    'end_conditions': (
                        EndConditionObject('liege.urban.schedule.notification_project_written'),
                    ),
                    'start_date': 'schedule.start_date.task_starting_date',
                    'additional_delay': 2,
                },
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'notifier-reponse',
            'title': 'Envoyer la réponse',
            'default_assigned_group': 'administrative_editors',
            'default_assigned_user': 'liege.urban.schedule.assign_task_owner',
            'creation_state': ('college_in_progress',),
            'starting_states': ('college_in_progress',),
            'start_conditions': (
                StartConditionObject('liege.urban.schedule.notification_project_validated'),
            ),
            'ending_states': ('opinion_sent',),
            'end_conditions': (
                MacroEndConditionObject('liege.urban.schedule.notification_sent'),
            ),
            'start_date': 'urban.schedule.start_date.creation_date',
            'additional_delay': 5,
        },
    ],
}
