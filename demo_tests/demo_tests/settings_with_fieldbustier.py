from django_fieldbustier.fieldbustier_config import DeleteFieldBustierConfig
from django_fieldbustier.fieldbustier_config import FieldBustierConfig

from .settings import *  # noqa


MIGRATION_MODULES = {"demo_app": "fieldbustier_migrations"}


INSTALLED_APPS.insert(0, "django_fieldbustier")  # noqa


ADD_FIELD_DJANGO_FIELDBUSTIER = [
    FieldBustierConfig(
        "demo_app",
        "DummyModel",
        "new_char_field",
        "CharField",
        ("An another CharField",),
        {"blank": True, "max_length": 200},
    )
]

REPLACE_FIELD_DJANGO_FIELDBUSTIER = [
    FieldBustierConfig(
        app_name="demo_app",
        model_klass="DummyModel",
        field_name="char_field",
        field_klass="CharField",
        args=("CharField FieldBusted !",),
        kwargs={"blank": True, "max_length": 200},
    ),
    FieldBustierConfig(
        "demo_app",
        "DummyModel",
        "decimal_field",
        "DecimalField",
        ("Decimal Field FieldBustier",),
        {"default": 2.3, "max_digits": 14, "decimal_places": 3},
    ),
]


DELETE_FIELD_DJANGO_FIELDBUSTIER = [DeleteFieldBustierConfig("demo_app", "DummyModel", "int_field")]
