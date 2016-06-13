# -*- coding: utf-8 -*-

from imio.schedule.content.object_factories import CreationConditionObject
from imio.schedule.content.object_factories import EndConditionObject
from imio.schedule.content.object_factories import MacroCreationConditionObject
from imio.schedule.content.object_factories import MacroEndConditionObject
from imio.schedule.content.object_factories import MacroStartConditionObject
from imio.schedule.content.object_factories import StartConditionObject

schedule_config = {
    'survey_schedule': [
        {
            'type_name': 'TaskConfig',
            'id': 'check_address',
            'title': "Vérifier l'adresse",
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
            'default_assigned_user': 'survivor',
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
            'type_name': 'TaskConfig',
            'id': 'ask_road_opinion',
            'title': "Avis voirie",
            'default_assigned_group': 'Voirie_editors',
            'default_assigned_user': 'road_editor',
            'creation_state': ('creation',),
            'creation_conditions': (
                CreationConditionObject('liege.urban.schedule.is_internal_opinion'),
            ),
            'starting_states': ('waiting_opinion',),
            'ending_states': ('opinions_given',),
            'start_date': 'liege.urban.schedule.asking_date',
            'additional_delay': 15,
        },
        {
            'type_name': 'TaskConfig',
            'id': 'ask_sssp_opinion',
            'title': "Avis SSSP",
            'default_assigned_group': 'SSSP_editors',
            'default_assigned_user': 'sssp_editor',
            'creation_state': ('creation',),
            'creation_conditions': (
                CreationConditionObject('liege.urban.schedule.is_internal_opinion'),
            ),
            'starting_states': ('waiting_opinion',),
            'ending_states': ('opinions_given',),
            'start_date': 'liege.urban.schedule.asking_date',
            'additional_delay': 15,
        },
        {
            'type_name': 'TaskConfig',
            'id': 'ask_access_opinion',
            'title': "Avis Access",
            'default_assigned_group': 'Access_editors',
            'default_assigned_user': 'access_editor',
            'creation_state': ('creation',),
            'creation_conditions': (
                CreationConditionObject('liege.urban.schedule.is_internal_opinion'),
            ),
            'starting_states': ('waiting_opinion',),
            'ending_states': ('opinions_given',),
            'start_date': 'liege.urban.schedule.asking_date',
            'additional_delay': 15,
        },
        {
            'type_name': 'TaskConfig',
            'id': 'ask_plantation_opinion',
            'title': "Avis Plantation",
            'default_assigned_group': 'Plantation_editors',
            'default_assigned_user': 'plantation_editor',
            'creation_state': ('creation',),
            'creation_conditions': (
                CreationConditionObject('liege.urban.schedule.is_internal_opinion'),
            ),
            'starting_states': ('waiting_opinion',),
            'ending_states': ('opinions_given',),
            'start_date': 'liege.urban.schedule.asking_date',
            'additional_delay': 15,
        },
        {
            'type_name': 'TaskConfig',
            'id': 'ask_edii_opinion',
            'title': "Avis EDII",
            'default_assigned_group': 'EDII_editors',
            'default_assigned_user': 'edii_editor',
            'creation_state': ('creation',),
            'creation_conditions': (
                CreationConditionObject('liege.urban.schedule.is_internal_opinion'),
            ),
            'starting_states': ('waiting_opinion',),
            'ending_states': ('opinions_given',),
            'start_date': 'liege.urban.schedule.asking_date',
            'additional_delay': 15,
        },
    ],
    'buildlicence': [
        {
            'type_name': 'TaskConfig',
            'id': 'depot',
            'title': 'Dépôt dossiers',
            'default_assigned_user': 'armin',
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
            'default_assigned_user': 'armin',
            'creation_state': ('incomplete',),
            'starting_states': ('incomplete',),
            'ending_states': ('checking_completion',),
            'start_date': 'schedule.start_date.subtask_highest_due_date',
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'demande_complements',
                    'title': 'Demander des compléments',
                    'default_assigned_user': 'armin',
                    'creation_state': ('incomplete',),
                    'starting_states': ('incomplete',),
                    'end_conditions': (
                        EndConditionObject('urban.schedule.condition.complements_asked'),
                    ),
                    'start_date': 'urban.schedule.start_date.deposit_date',
                    'additional_delay': 1,
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'attente_complements',
                    'title': 'En attente de compléments',
                    'default_assigned_user': 'armin',
                    'creation_state': ('incomplete',),
                    'start_conditions': (
                        StartConditionObject('urban.schedule.condition.complements_asked'),
                    ),
                    'end_conditions': (
                        EndConditionObject('urban.schedule.condition.complements_received'),
                    ),
                    'start_date': 'urban.schedule.start_date.ask_complements_date',
                    'additional_delay': 15,
                },
            ],
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'accuse',
            'title': 'Accusé de réception',
            'default_assigned_user': 'armin',
            'creation_state': ('checking_completion',),
            'starting_states': ('checking_completion',),
            'end_conditions': (
                MacroEndConditionObject('urban.schedule.condition.acknowledgment_done'),
            ),
            'start_date': 'urban.schedule.start_date.deposit_date',
            'additional_delay': 15,
            'subtasks': [
                {
                    'type_name': 'TaskConfig',
                    'id': 'verif_complet',
                    'title': 'Vérification de la complétude',
                    'default_assigned_user': 'teckel',
                    'creation_state': ('checking_completion',),
                    'starting_states': ('checking_completion',),
                    'ending_states': ('complete', 'incomplete'),
                    'start_date': 'urban.schedule.start_date.deposit_date',
                    'additional_delay': 1,
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'valide_complet',
                    'title': 'Valider la complétude',
                    'default_assigned_user': 'teckel',
                    'creation_state': ('complete',),
                    'starting_states': ('complete',),
                    'ending_states': ('checking_completion', 'analysis'),
                    'start_date': 'schedule.start_date.starting_date',
                    'additional_delay': 2,
                },
                {
                    'type_name': 'MacroTaskConfig',
                    'id': 'choix',
                    'title': 'Choix de la procédure',
                    'default_assigned_user': 'teckel',
                    'creation_state': ('checking_completion',),
                    'starting_states': ('checking_completion',),
                    'ending_states': ('procedure_validated', 'preparing_decision'),
                    'start_date': 'urban.schedule.start_date.deposit_date',
                    'additional_delay': 2,
                    'subtasks': [
                        {
                            'type_name': 'TaskConfig',
                            'id': 'rayon-enquete',
                            'title': 'Identifier la zone d\'enquête',
                            'default_assigned_user': 'teckel',
                            'creation_conditions': (
                                CreationConditionObject('urban.schedule.condition.will_have_inquiry'),
                            ),
                            'end_conditions': (
                                EndConditionObject('urban.schedule.condition.inquiry_event_created', 'AND'),
                                EndConditionObject('liege.urban.schedule.inquiry_zone_identified'),
                            ),
                            'start_date': 'urban.schedule.start_date.deposit_date',
                            'additional_delay': 12,
                        },
                    ],
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'validate_procedure',
                    'title': 'Valider la procédure',
                    'default_assigned_user': 'valtec',
                    'creation_state': ('analysis',),
                    'starting_states': ('analysis'),
                    'ending_states': ('procedure_validated', 'preparing_decision'),
                    'start_date': 'urban.schedule.start_date.deposit_date',
                    'additional_delay': 13,
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'enquete-dates',
                    'title': 'Définir les dates de d\'enquête',
                    'default_assigned_user': 'teckel',
                    'creation_state': ('procedure_validated',),
                    'creation_conditions': (
                        CreationConditionObject('urban.schedule.condition.will_have_inquiry'),
                    ),
                    'end_conditions': (
                        EndConditionObject('urban.schedule.condition.inquiry_dates_defined'),
                    ),
                    'start_date': 'urban.schedule.start_date.deposit_date',
                    'additional_delay': 15,
                },
            ],
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'analyse',
            'title': 'Analyse',
            'default_assigned_user': 'valtec',
            'creation_state': ('procedure_validated',),
            'starting_states': ('procedure_validated',),
            'start_conditions': (
                MacroStartConditionObject('urban.schedule.condition.acknowledgment_done'),
            ),
            'ending_states': ('preparing_decision',),
            'start_date': 'urban.schedule.start_date.acknowledgment_date',
            'additional_delay': 5,
            'subtasks': [
                {
                    'type_name': 'MacroTaskConfig',
                    'id': 'avis-services',
                    'title': 'Avis de services',
                    'default_assigned_user': 'teckel',
                    'creation_state': ('analysis',),
                    'creation_conditions': (
                        MacroCreationConditionObject('urban.schedule.condition.has_opinion_requests'),
                    ),
                    'starting_states': ('analysis',),
                    'end_conditions': (
                        MacroEndConditionObject('urban.schedule.condition.opinion_requests_done'),
                    ),
                    'start_date': 'urban.schedule.start_date.acknowledgment_date',
                    'subtasks': [
                        {
                            'type_name': 'MacroTaskConfig',
                            'id': 'documents-avis',
                            'title': 'Envoyer les demandes d\'avis',
                            'default_assigned_user': 'armin',
                            'marker_interfaces': [u'liege.urban.schedule.interfaces.ISendOpinionRequestsTask'],
                            'creation_state': ('analysis',),
                            'creation_conditions': (
                                MacroCreationConditionObject('urban.schedule.condition.has_opinion_requests'),
                            ),
                            'starting_states': ('analysis',),
                            'end_conditions': (
                                MacroEndConditionObject('liege.urban.schedule.opinion_requests_waiting'),
                            ),
                            'start_date': 'urban.schedule.start_date.deposit_date',
                            'additional_delay': 3,
                            'subtasks': [
                                {
                                    'type_name': 'TaskConfig',
                                    'id': 'demander-avis',
                                    'title': 'Créer les événements',
                                    'default_assigned_user': 'teckel',
                                    'marker_interfaces': [u'liege.urban.schedule.interfaces.ICreateOpinionRequestsTask'],
                                    'creation_state': ('analysis',),
                                    'creation_conditions': (
                                        CreationConditionObject('urban.schedule.condition.has_opinion_requests'),
                                    ),
                                    'starting_states': ('analysis',),
                                    'end_conditions': (
                                        EndConditionObject('urban.schedule.condition.opinion_requests_created'),
                                    ),
                                    'start_date': 'urban.schedule.start_date.deposit_date',
                                    'additional_delay': 1,
                                },
                            ],
                        },
                    ]
                },
                {
                    'type_name': 'MacroTaskConfig',
                    'id': 'enquete',
                    'title': 'Enquête publique',
                    'default_assigned_user': 'teckel',
                    'creation_state': ('procedure_validated',),
                    'creation_conditions': (
                        MacroCreationConditionObject('urban.schedule.condition.acknowledgment_done', 'OR'),
                        MacroCreationConditionObject('urban.schedule.condition.has_inquiry'),
                    ),
                    'starting_states': ('procedure_validated',),
                    'end_conditions': (
                        MacroEndConditionObject('urban.schedule.condition.inquiry_done'),
                    ),
                    'start_date': 'urban.schedule.start_date.inquiry_end_date',
                    'subtasks': [
                        {
                            'type_name': 'TaskConfig',
                            'id': 'enquete-documents',
                            'title': 'Produire les documents',
                            'default_assigned_user': 'armin',
                            'creation_state': ('procedure_validated',),
                            'creation_conditions': (
                                CreationConditionObject('urban.schedule.condition.has_inquiry'),
                            ),
                            'end_conditions': (
                                EndConditionObject('liege.urban.schedule.inquiry_documents_done'),
                            ),
                            'start_date': 'urban.schedule.start_date.acknowledgment_date',
                        },
                    ]
                },
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'avis-fd',
            'title': 'Avis du FD',
            'default_assigned_user': 'armin',
            'creation_state': ('procedure_validated',),
            'creation_conditions': (
                MacroCreationConditionObject('urban.schedule.condition.need_FD_opinion'),
            ),
            'starting_states': ('procedure_validated',),
            'end_conditions': (
                MacroEndConditionObject('urban.schedule.condition.FD_opinion_received'),
            ),
            'start_date': 'urban.schedule.start_date.inquiry_end_date',
            'subtasks': [
                {
                    'type_name': 'MacroTaskConfig',
                    'id': 'premier-passage',
                    'title': 'Premier passage collège',
                    'default_assigned_user': 'teckel',
                    'creation_state': ('FD_opinion',),
                    'starting_states': ('FD_opinion',),
                    'start_date': 'schedule.start_date.subtask_highest_due_date',
                    'additional_delay': 2,
                    'subtasks': [
                        {
                            'type_name': 'TaskConfig',
                            'id': 'rediger-projet-avis',
                            'title': 'Rédiger le projet d\'avis',
                            'default_assigned_user': 'armin',
                            'creation_state': ('FD_opinion',),
                            'starting_states': ('FD_opinion',),
                            'start_date': 'schedule.start_date.subtask_highest_due_date',
                            'additional_delay': 2,
                        },
                        {
                            'type_name': 'TaskConfig',
                            'id': 'valider-projet-avis',
                            'title': 'Valider le projet d\'avis',
                            'default_assigned_user': 'valere',
                            'creation_state': ('FD_opinion',),
                            'starting_states': ('FD_opinion',),
                            'start_date': 'schedule.start_date.subtask_highest_due_date',
                            'additional_delay': 2,
                        },
                    ]
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'envoyer-avis-FD',
                    'title': 'Envoyer la demande d\'avis',
                    'default_assigned_user': 'teckel',
                    'creation_state': ('FD_opinion',),
                    'starting_states': ('FD_opinion',),
                    'start_date': 'schedule.start_date.subtask_highest_due_date',
                    'additional_delay': 2,
                },
                {
                    'type_name': 'TaskConfig',
                    'id': 'reception-avis-FD',
                    'title': 'Réception de l\'avis',
                    'default_assigned_user': 'teckel',
                    'creation_state': ('FD_opinion',),
                    'starting_states': ('FD_opinion',),
                    'start_date': 'schedule.start_date.subtask_highest_due_date',
                    'additional_delay': 2,
                }
            ]
        },
        {
            'type_name': 'MacroTaskConfig',
            'id': 'decision-finale',
            'title': 'Décision finale à notifier',
            'default_assigned_user': 'armin',
            'creation_state': ('preparing_decision',),
            'starting_states': ('preparing_decision',),
            'start_date': 'schedule.start_date.subtask_highest_due_date',
            'additional_delay': 2,
            'subtasks': [
                {
                    'type_name': 'MacroTaskConfig',
                    'id': 'projet-permis',
                    'title': 'Rédiger le projet de permis',
                    'default_assigned_user': 'armin',
                    'creation_state': ('preparing_decision',),
                    'starting_states': ('preparing_decision',),
                    'start_date': 'schedule.start_date.subtask_highest_due_date',
                    'additional_delay': 2,
                },
            ]
        },
    ],
}
