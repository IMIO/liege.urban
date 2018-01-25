# -*- coding: utf-8 -*-

from Products.Archetypes.atapi import Schema
from Products.Archetypes.atapi import RichWidget
from Products.Archetypes.atapi import TextField

from Products.urban.interfaces import IOptionalFields
from Products.urban.UrbanEvent import UrbanEvent
from Products.urban.utils import setOptionalAttributes

from zope.interface import implements


specific_schema = Schema((
    TextField(
        name='pmObject',
        allowable_content_types=('text/html',),
        widget=RichWidget(
            label='Pmobject',
            label_msgid='urban_label_pmObject',
            i18n_domain='urban',
        ),
        default_method='getDefaultText',
        default_content_type='text/html',
        default_output_type='text/html',
        optional=True,
        pm_text_field=True,
    ),
    TextField(
        name='motivation',
        allowable_content_types=('text/html',),
        widget=RichWidget(
            label='Motivation',
            label_msgid='urban_label_motivation',
            i18n_domain='urban',
        ),
        default_method='getDefaultText',
        default_content_type='text/html',
        default_output_type='text/html',
        optional=True,
        pm_text_field=True,
    ),
    TextField(
        name='device',
        allowable_content_types=('text/html',),
        widget=RichWidget(
            label='Device',
            label_msgid='urban_label_device',
            i18n_domain='urban',
        ),
        default_method='getDefaultText',
        default_content_type='text/html',
        default_output_type='text/html',
        optional=True,
        pm_text_field=True,
    ),
    TextField(
        name='deviceContinuation',
        allowable_content_types=('text/html',),
        widget=RichWidget(
            label='DeviceContinuation',
            label_msgid='urban_label_deviceContinuation',
            i18n_domain='urban',
        ),
        default_method='getDefaultText',
        default_content_type='text/html',
        default_output_type='text/html',
        optional=True,
        pm_text_field=True,
    ),
    TextField(
        name='deviceEnd',
        allowable_content_types=('text/html',),
        widget=RichWidget(
            label='DeviceEnd',
            label_msgid='urban_label_deviceEnd',
            i18n_domain='urban',
        ),
        default_method='getDefaultText',
        default_content_type='text/html',
        default_output_type='text/html',
        optional=True,
        pm_text_field=True,
    ),
),)

optional_fields = [field.getName() for field in specific_schema.filterFields(isMetadata=False)]
setOptionalAttributes(specific_schema, optional_fields)


class UrbanEventOptionalFields(object):
    """
    """
    implements(IOptionalFields)

    def __init__(self, context):
        self.context = context

    def get(self):
        return specific_schema.fields()


def update_item_schema(baseSchema):

    UrbanEventSchema = baseSchema + specific_schema.copy()

    return UrbanEventSchema


UrbanEvent.schema = update_item_schema(UrbanEvent.schema)


# Classes have already been registered, but we register them again here
# because we have potentially applied some schema adaptations (see above).
# Class registering includes generation of accessors and mutators, for
# example, so this is why we need to do it again now.
from Products.urban.config import registerClasses
registerClasses()
