from attr.setters import frozen
from pydantic import BaseModel, ValidationError, ConfigDict


class Model(BaseModel):
    field_1: int

m = Model(field_1=1)
m.field_1 = 20


class Model(BaseModel):
    field_1: int

    model_config = ConfigDict(
        frozen = True,
    )

m = Model(field_1=1)

'''
1 validation error for Model
field_1
  Instance is frozen [type=frozen_instance, input_value=20, input_type=int]
    For further information visit https://errors.pydantic.dev/2.9/v/frozen_instance
'''
try:
    m.field_1 = 20
except ValidationError as e:
    # print(e)
    pass