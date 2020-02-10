from collections import defaultdict
from importlib import import_module
from sys import argv

from django.apps import AppConfig
from django.apps import apps
from django.conf import settings
from django.utils.translation import ugettext_lazy as _


def import_object(path_to_object):
    path_module, object_name = path_to_object.rsplit(".", 1)

    imported_module = import_module(path_module)
    return getattr(imported_module, object_name)


def import_field_class(path_to_field_klass):
    if "." in path_to_field_klass:
        return import_object(path_to_field_klass)
    else:
        return import_object(f"django.db.models.{path_to_field_klass}")


def parse_fields_for_fieldbustier(list_fields):
    fields = defaultdict(list)
    for one_field in list_fields:
        model_key = one_field.app_name, one_field.model_klass.lower()
        field_klass = import_field_class(one_field.field_klass)

        field_buste = field_klass(*one_field.args, **one_field.kwargs)
        if one_field.post_function:
            one_field.post_function(field_buste)

        fields[model_key].append((one_field.field_name, field_buste))
    return fields


GENERATE_MIGRATIONS = getattr(settings, "GENERATE_FIELDBUSTIER_MIGRATIONS", True)

fields_for_fieldbustier = defaultdict(list)
replace_fields_for_fieldbustier = defaultdict(list)
delete_fields_for_fieldbustier = list()


def add_fields_to_model(sender, **kwargs):
    model_key = sender._meta.app_label, sender._meta.model_name
    for field_name, field in fields_for_fieldbustier.get(model_key, {}):
        field.contribute_to_class(sender, field_name)


def replace_fields_of_model(sender, **kwargs):
    model_key = sender._meta.app_label, sender._meta.model_name
    for field_name, field in replace_fields_for_fieldbustier.get(model_key, {}):
        meta = sender._meta
        old_fields = [old_field for old_field in meta.local_fields if old_field.name == field_name]
        if old_fields:
            meta.local_fields.remove(old_fields[0])
        field.contribute_to_class(sender, field_name)


def delete_fields_of_model(sender, **kwargs):
    name_useless_fields = [
        field_config.field_name
        for field_config in delete_fields_for_fieldbustier
        if sender._meta.app_label == field_config.app_name
        and sender._meta.model_name == field_config.model_klass.lower()
    ]
    meta = sender._meta
    useless_fields = [old_field for old_field in meta.local_fields if old_field.name in name_useless_fields]
    for useless_field in useless_fields:
        meta.local_fields.remove(useless_field)


class FieldBustierConfig(AppConfig):
    name = "django_fieldbustier"
    verbose_name = _("django_fieldbustier")

    def ready(self):
        if "makemigrations" in argv and not GENERATE_MIGRATIONS:
            return

        fields_for_fieldbustier.update(
            parse_fields_for_fieldbustier(getattr(settings, "ADD_FIELD_DJANGO_FIELDBUSTIER", []))
        )

        replace_fields_for_fieldbustier.update(
            parse_fields_for_fieldbustier(getattr(settings, "REPLACE_FIELD_DJANGO_FIELDBUSTIER", []))
        )

        delete_fields_for_fieldbustier.extend(getattr(settings, "DELETE_FIELD_DJANGO_FIELDBUSTIER", []))

        for model_key in fields_for_fieldbustier:
            apps.lazy_model_operation(add_fields_to_model, model_key)

        for model_key in replace_fields_for_fieldbustier:
            apps.lazy_model_operation(replace_fields_of_model, model_key)

        for field_config in delete_fields_for_fieldbustier:
            model_key = field_config.app_name, field_config.model_klass.lower()
            apps.lazy_model_operation(delete_fields_of_model, model_key)
