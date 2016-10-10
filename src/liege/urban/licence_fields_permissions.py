# -*- coding: utf-8 -*-

from Products.urban.BuildLicence import BuildLicence_schema


def init_field_permissions():
    """
    """
    schemas = [BuildLicence_schema]

    permissions_mapping = {
        'urban_description': ('liege.urban: External Reader', ''),
        'urban_advices': ('liege.urban: Road Reader', ''),
        'urban_inquiry': ('', ''),
        'urban_analysis': ('', ''),
        'urban_location': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
        'urban_road': ('liege.urban: Road Reader', 'liege.urban: Road Editor'),
        'urban_habitation':  ('', ''),
        'urban_peb':  ('', ''),
    }

    exceptions = ['portal_type']

    for schema in schemas:
        for field in schema.fields():
            if field.getName() not in exceptions:
                read_permission, write_permission = permissions_mapping.get(field.schemata, ('', ''))
                if read_permission:
                    field.read_permission = read_permission
                if write_permission:
                    field.write_permission = write_permission
