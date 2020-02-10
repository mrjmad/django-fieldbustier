from collections import namedtuple
from sys import version_info


if version_info[1] >= 7:
    FieldBustierConfig = namedtuple(
        "FieldBustierConfig",
        ["app_name", "model_klass", "field_name", "field_klass", "args", "kwargs", "post_function"],
        defaults=(None,),
    )
else:
    FieldBustierConfig = namedtuple(
        "FieldBustierConfig",
        ["app_name", "model_klass", "field_name", "field_klass", "args", "kwargs", "post_function"],
    )
    FieldBustierConfig.__new__.__defaults__ = (None,)


DeleteFieldBustierConfig = namedtuple("FieldBustierConfig", ["app_name", "model_klass", "field_name"])
