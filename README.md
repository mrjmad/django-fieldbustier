# django-fieldbustier

The purpose of this django-app is to allow you to add fields to models from another application.

## Why this name?

Because wanting to add models from another django-app, from your own, is a bit like wanting to get on a boat and do it by shouting "All Aboard", a knife between your teeth.

And in French, a pirate is also a "flibustier", a word quite close to fieldbustier, so -> django-fieldbustier.

## How to use it django-fieldbustier

you must declare the fields you want to add, modify or delete in your settings.

There are three configuration variables that are:
- ADD_FIELD_DJANGO_FIELDBUSTIER to add fields
- REPLACE_FIELD_DJANGO_FIELDBUSTIER to modify fields
- DELETE_FIELD_DJANGO_FIELDBUSTIER to delete fields

To add or modify fields you must use `FieldBustierConfig`. To delete people you must use `DeleteFieldBustierConfig`.


`FieldBustierConfig` are `namedtuple` with these attributes :
 - app_name
 - model_klass
 - field_name
 - field_klass (You can use Django Field or your Field)
 - args (a tuple for positional args)
 - kwargs (a dict for keyword args)

`DeleteFieldBustierConfig` are `namedtuple` with these attributes :
 - app_name
 - model_klass
 - field_name


### Add a Field

```
from django_fieldbustier.fieldbustier_config import FieldBustierConfig

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
```

### Modify a Field


```
from django_fieldbustier.fieldbustier_config import FieldBustierConfig

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
```

### Delete a Field

```
from django_fieldbustier.fieldbustier_config import FieldBustierConfig

DELETE_FIELD_DJANGO_FIELDBUSTIER = [DeleteFieldBustierConfig("demo_app",
                                                             "DummyModel",
                                                             "int_field")]
```

## Migrations

### GENERATE_FIELDBUSTIER_MIGRATIONS option

If you have used SQL to directly implement your changes, then you will not want the migrations to be generated.

To do this, you just have to set (in your settings) GENERATE_FIELDBUSTIER_MIGRATIONS at False.

### Location of migration files

By default, the migration files of an application are located in the application. In our case, if you use Django-Fieldbustier, it is to avoid modifying the target application. This behavior is therefore not appropriate at all.

To avoid this, simply use django's MIGRATION_MODULES variable to choose where you want your migrations to be generated.



## Thanks

Thanks for Olivier Meunier, Creme CRM codebase and Mezzanine injection Fields system for the original idea.
