from pydantic import (
    BaseModel,
    ConfigDict,
    ValidationError
)


class Model(BaseModel):
    field_1: int


m = Model(field_1=1)
print(m.model_dump())

# no error, when string is assigned to int
m.field_1 = 'Python'
print(m.field_1)


class Model(BaseModel):
    field_1: int

    model_config = ConfigDict(
        validate_assignment=True,
    )

m = Model(field_1= 1)
print(m.model_dump())

"""
1 validation error for Model
field_1
  Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='Python', input_type=str]
    For further information visit https://errors.pydantic.dev/2.9/v/int_parsing
"""

try:
    m.field_1 = 'Python'
except ValidationError as e:
   # print(e)
   pass 
