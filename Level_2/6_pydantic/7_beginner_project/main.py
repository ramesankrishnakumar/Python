from datetime import date
from typing import Union

from jsonschema.exceptions import ValidationError
from pandas.io.clipboard import paste
from pydantic import BaseModel

"""
We are going to build a model for an automobile.

Throughout the course, at the end of each section you will add on to this model, refactor some parts of it, or create related models that will then be used in conjunction with this automobile model when we get to model composition.

To start, you should create an Automobile model that contains the following fields:

manufacturer, string, required, not nullable
series_name, string, required, not nullable
type_, string, required, not nullable
is_electric, boolean, defaults to False, not nullable
manufactured_date, date, required (hint use date from datetime module as your field type hint), not nullable
base_msrp_usd, float, required, not nullable
vin, string, required, not nullable
number_of_doors, integer, defaults to 4, not nullable
registration_country, string, defaults to None
license_plate, string, defaults to None


Once you have created your model, you should test deserializing and serializing your model and make sure everything works.

To help you, in most sections, I provide some sample "input" and "output" data that you can use to check your model is working.

You can test your model by deserializing the following input data, and comparing the serialization of each of those models to the provided Python dictionaries.

In other words, test them by doing something like this for both cases:

create model by deserializing the data
check the model's serialization to dict is equal to the provided expected dictionary

"""

data = {
    "manufacturer": "BMW",
    "series_name": "M4",
    "type_": "Convertible",
    "is_electric": False,
    "manufactured_date": "2023-01-01",
    "base_msrp_usd": 93_300,
    "vin": "1234567890",
    "number_of_doors": 2,
    "registration_country": "France",
    "license_plate": "AAA-BBB",
}

data_expected_serialization = {
    'manufacturer': 'BMW',
    'series_name': 'M4',
    'type_': 'Convertible',
    'is_electric': False,
    'manufactured_date': date(2023,1,1),
    'base_msrp_usd': 93_300,
    'vin': '1234567890',
    'number_of_doors': 2,
    'registration_country': 'France',
    'license_plate': 'AAA-BBB',
}


# JSON
data_json = '''
{
    "manufacturer": "BMW",
    "series_name": "M4",
    "type_": "Convertible",
    "manufactured_date": "2023-01-01",
    "base_msrp_usd": 93300,
    "vin": "1234567890"
}
'''

data_json_expected_serialization = {
    'manufacturer': 'BMW',
    'series_name': 'M4',
    'type_': 'Convertible',
    'is_electric': False,
    'manufactured_date': date(2023, 1, 1),
    'base_msrp_usd': 93_300,
    'vin': '1234567890',
    'number_of_doors': 4,
    'registration_country': None,
    'license_plate': None,
}

class Automobile(BaseModel):
    manufacturer: str
    series_name: str
    type_: str
    is_electric: bool = False
    manufactured_date: date
    base_msrp_usd: float
    vin: str
    number_of_doors: int = 4
    registration_country: Union[str, None] = None
    license_plate: Union[str, None] = None


car1: Automobile
car2: Automobile

try:
    car1 = Automobile.model_validate(data)
    for key, val in car1.model_dump().items():
        if data_expected_serialization[key] != val:
            print(f"fail for {key} {data_expected_serialization[key]} != {val}")
except ValidationError as e:
    print(e)
    exit(-1)



try:
    car2 = Automobile.model_validate_json(data_json)
    for key, val in car2.model_dump().items():
        if data_json_expected_serialization[key] != val:
            print(f"fail for {key} {data_json_expected_serialization[key]} != {val}")
except ValidationError as e:
    print(e)
    exit(-1)

assert car1.model_dump() == data_expected_serialization
assert car2.model_dump() == data_json_expected_serialization

print("pass!!!")