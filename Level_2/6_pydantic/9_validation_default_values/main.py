from pydantic import BaseModel, ConfigDict


class Model(BaseModel):
    field_1: int = None
    field_2: str = 100

# field_1=None field_2=100
# default values assigned are not validated
model = Model()
print(str(model))

"""
2 validation errors for Model
field_1
  Input should be a valid integer [type=int_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.9/v/int_type
field_2
  Input should be a valid string [type=string_type, input_value=20, input_type=int]
    For further information visit https://errors.pydantic.dev/2.9/v/string_type
"""
try:
    model = Model(field_1=None, field_2=20)
except Exception as e:
    # print(e)
    pass

class Model(BaseModel):
    field_1: int = None
    field_2: str = 100
    # using model config to validate default assignment
    model_config = ConfigDict(
        validate_default=True,
    )

"""
default value validation: 2 validation errors for Model
field_1
  Input should be a valid integer [type=int_type, input_value=None, input_type=NoneType]
    For further information visit https://errors.pydantic.dev/2.9/v/int_type
field_2
  Input should be a valid string [type=string_type, input_value=100, input_type=int]
    For further information visit https://errors.pydantic.dev/2.9/v/string_type
"""

try:
    model = Model()
except Exception as e:
    print(f"default value validation: {e}")
    # pass
