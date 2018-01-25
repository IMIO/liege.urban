# -*- coding: utf-8 -*-


def set_field_permissions(schema, mapping, exceptions=[]):
    """
    """

    for field in schema.fields():
        if field.getName() not in exceptions:
            default = ('liege.urban: Internal Reader', 'liege.urban: Internal Editor')
            read_permission, write_permission = mapping.get(field.schemata, default)
            if read_permission:
                field.read_permission = read_permission
            if write_permission:
                field.write_permission = write_permission

    return schema
