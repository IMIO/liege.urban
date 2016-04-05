# -*- coding: utf-8 -*-

from Products.urban.BuildLicence import BuildLicence_schema


def init_field_permissions():
    """
    """
    schemas = [BuildLicence_schema]

    for schema in schemas:
        for field in schema.fields():
            exceptions = ['portal_type']
            if field.schemata != 'urban_description' and field.getName() not in exceptions:
                field.read_permission = 'liege.urban: Internal Reader'
