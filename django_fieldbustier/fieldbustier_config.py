from collections import namedtuple


FieldBustierConfig = namedtuple(
    "FieldBustierConfig", ["app_name", "model_klass", "field_name", "field_klass", "args", "kwargs"]
)

DeleteFieldBustierConfig = namedtuple("FieldBustierConfig", ["app_name", "model_klass", "field_name"])
