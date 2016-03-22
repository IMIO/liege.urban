# -*- coding: utf-8 -*-

schedule_config = {
    'survey_schedule': [
        'TaskConfig',
        {
            'id': "check_address",
            'title': "Vérifier l'adresse",
            'default_assigned_user': 'survey',
            'creation_state': 'validating_address',
            'starting_states': 'validating_address',
            'ending_states': ('waiting_address', 'procedure_choice',),
            'start_date': 'urban.due_date.deposit_date',
            'additional_delay': 2,
        },
        {
            'id': "assign_temporary_address",
            'title': "Assigner une adresse temporaire",
            'default_assigned_user': 'survey',
            'creation_state': 'waiting_address',
            'starting_states': 'waiting_address',
            'ending_states': ('procedure_choice',),
            'start_date': 'urban.due_date.deposit_date',
            'additional_delay': 2,
        },
    ],
    'buildlicence': [
        'TaskConfig',
        {
            'id': "accuse",
            'title': 'Accusé de réception',
            'default_assigned_user': 'urban.schedule.assign_current_user',
            'creation_state': 'in_progress',
            'starting_states': ('in_progress',),
            'ending_states': ('accepted',),
            'due_date_computation': 'urban.due_date.deposit_date',
            'additional_delay': 10,
        },
        {
            'id': "depot",
            'title': 'Dépôt dossiers',
            'default_assigned_user': 'urban.schedule.assign_current_user',
            'creation_state': 'in_progress',
            'starting_states': ('in_progress',),
            'ending_states': ('accepted',),
            'due_date_computation': 'urban.due_date.deposit_date',
            'additional_delay': 10,
        },
        {
            'id': "analyse",
            'title': 'Dossiers à analyser',
            'default_assigned_user': 'urban.schedule.assign_current_user',
            'starting_state': 'accepted',
            'ending_states': ('refused',),
            'due_date_computation': 'urban.due_date.deposit_date',
            'additional_delay': 10,
        },
    ],

}
