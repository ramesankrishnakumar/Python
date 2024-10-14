# https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.field_title_generator
from dataclasses import field
from typing import Any

from pydantic import (
    BaseModel,
    ConfigDict,
    ValidationError
)

class MyModel(BaseModel):
    field1: int

# usually comes from a dictionary or json
m = MyModel(field1=1, field_2=20)
print(f"dump: {m.model_dump()}")
print(f"extra_fields: {m.model_extra}") # By default, pydantic ignores the extra attributes passed


"""
Whether to ignore, allow, or forbid extra attributes during model initialization. Defaults to 'ignore'.

You can configure how pydantic handles the attributes that are not defined in the model:

allow - Allow any extra attributes.
forbid - Forbid any extra attributes.
ignore - Ignore any extra attributes.
"""

class MyModel(BaseModel):
    field1: int
    model_config = ConfigDict( # default
        extra="ignore",
    )

m = MyModel(field1=1, field_2=20)
print(f"dump: {m.__dict__}")
print(f"extra_fields: {m.model_extra}") # By default, pydantic ignores the extra attributes passed


class MyModel(BaseModel):
    field1: int
    model_config = ConfigDict( # default
        extra="forbid",
    )

"""
1 validation error for MyModel
field_2
  Extra inputs are not permitted [type=extra_forbidden, input_value=20, input_type=int]
    For further information visit https://errors.pydantic.dev/2.9/v/extra_forbidden

"""
try:
    m = MyModel(field1=1, field_2=20)
except ValidationError as e:
    # print(e)
    pass

###
### Strict Vs Lax
###


class Model(BaseModel):
    field_1: str
    field_2: float
    field_3: list
    field_4: tuple

"""
1 validation error for Model
field_1
  Input should be a valid string [type=string_type, input_value=1, input_type=int]
    For further information visit https://errors.pydantic.dev/2.9/v/string_type
"""

try:
    m = Model(field_1=1, field_2=2, field_3=(1, 2, 3), field_4=[4, 5, 6])
    print(f"dump: {m.__dict__}")
except ValidationError as e:
   # print(e)
   pass

# dump: {'field_1': '1', 'field_2': 2.0, 'field_3': [1, 2, 3], 'field_4': (4, 5, 6)}
# 2 to 2.0 , tuple to list & list to tuple
m = Model(field_1="1", field_2=2, field_3=(1, 2, 3), field_4=[4, 5, 6])
print(f"dump: {m.model_dump()}")


class Model(BaseModel):
    field_1: str
    field_2: float
    field_3: list
    field_4: tuple

    model_config = ConfigDict( strict=True)
"""
2 validation errors for Model
field_3
  Input should be a valid list [type=list_type, input_value=(1, 2, 3), input_type=tuple]
    For further information visit https://errors.pydantic.dev/2.9/v/list_type
field_4
  Input should be a valid tuple [type=tuple_type, input_value=[4, 5, 6], input_type=list]
    For further information visit https://errors.pydantic.dev/2.9/v/tuple_type
"""

try:
    m = Model(field_1="1", field_2=2, field_3=(1, 2, 3), field_4=[4, 5, 6])
except ValidationError as e:
    # print(e)
    pass


class Model(BaseModel):
    field_1: bool
    field_2: float
    field_3: int
    field_4: str | None
    field_5: tuple[int, ...] # tuple of integers and of any size
    field_6: set[str]
    field_7: dict[str, Any]

json_str = """ 
{
"field_1": true,
"field_2": 10,
"field_3": 1,
"field_4": null,
"field_5": [1,2,3],
"field_6": ["a", "b", "c"],
"field_7": {
"a" : 1, "b" : 2, "c" : { "d" : "ccc"}
}

}
"""

# dump: {'field_1': True, 'field_2': 10.0, 'field_3': 1, 'field_4': None, 'field_5': (1, 2, 3), 'field_6': {'b', 'c', 'a'}, 'field_7': {'a': 1, 'b': 2, 'c': {'d': 'ccc'}}}
m = Model.model_validate_json(json_str)
print(f"dump: { m.model_dump()}")
