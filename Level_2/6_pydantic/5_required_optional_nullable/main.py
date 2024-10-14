from datetime import datetime
from pprint import pprint
from typing import Union

from pydantic import BaseModel


class CircleV1(BaseModel):
    radius: float
    center: tuple[int, int]


# model fields can be printed from class name
"""
{'radius': FieldInfo(annotation=float, required=True),
 'center': FieldInfo(annotation=tuple[int, int], required=True)}
"""
#pprint(CircleV1.model_fields, sort_dicts=False)

class CircleV2(BaseModel):
    radius: float
    center: tuple[int, int] = [0,0]  # required = false # pydantic does not validate this


class CircleV3(BaseModel):
    radius: float
    center: tuple[int, int] = "junk"


#print(CircleV3(radius=1)) # radius=1.0 center='junk' # radius got type coerced


"""
{'radius': FieldInfo(annotation=float, required=True),
 'center': FieldInfo(annotation=tuple[int, int], required=False, default=[0, 0])}
"""
#pprint(CircleV2.model_fields, sort_dicts=False)

# center is optional and takes the default value of [0,0] when not provided

circle_json = ''' {
    "radius": 5.4
} '''

circle_from_json = CircleV2.model_validate_json(circle_json)
# print(circle_from_json)
fields_of_class = CircleV2.model_fields.keys()
# print(fields_of_class) # dict_keys(['radius', 'center'])
fields_set_manually = circle_from_json.model_fields_set
# print(fields_set_manually) # {'radius'}
print(fields_of_class - fields_set_manually) # fields having default value # {'center'}


## Nullable
class Model(BaseModel):
    field : int | None # not optional


# print(Model.model_fields) # {'field': FieldInfo(annotation=Union[int, NoneType], required=True)}
# print(Model(field=None))




class Model2(BaseModel): # same as above
    field : Union[int, None] # not optional


class Regular:
    center: tuple[int, int] = (0, 0)

    def __init__(self, radius: float):
        self.radius = radius


r1 = Regular(5)
r2 = Regular(4)
Regular.center = (5, 5) # acts as a static field
# print(r1.radius, r1.center) # (5,5)
# print(r2.radius, r2.center) # (5,5)

def populate_date_in_list(lst = []): # memory of [] is calculated at compile time
    lst.append(datetime.now().__str__())
    return lst

my_list = []
my_list = populate_date_in_list(my_list)

# print(my_list) # ['2024-09-13 12:17:38.880023']

my_list = populate_date_in_list() # leverage default param
# print(my_list) # ['2024-09-13 12:17:38.880035']
my_list = populate_date_in_list()
# print(my_list) # ['2024-09-13 12:17:38.880035', '2024-09-13 12:17:38.880037']

