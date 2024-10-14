from pydantic import BaseModel, ValidationError


class Person(BaseModel):
    first_name: str # field, attribute
    last_name: str
    age: int

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


# deserialization from dictionary

person = {
    "first_name": "John",
    "last_name": "Doe",
    "age": 23,
}
p = Person(**person) # works
#print(str(p))

# but the recommended way to do this,
# which works for complex use case well is

p = Person.model_validate(person)
#print(str(p))

person = {
    "last_name": "Doe",
    "age": "23",
}

"""
1 validation error for Person
first_name
  Field required [type=missing, input_value={'last_name': 'Doe', 'age': '23'}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.9/v/missing
"""

try:
    p = Person.model_validate(person)
except ValidationError as e:
    pass
    # print(e)

# deserialization from json

person = '''{
    "first_name": "John",
    "last_name": "Doe",
    "age": 23 
}
'''
# No trailing comma for json

p = Person.model_validate_json(person)
# print(p) # first_name='John' last_name='Doe' age=23


person = '''{
    "first_name": "John",
    "last_name": "Doe"
}
'''
try:
    p = Person.model_validate_json(person)
except ValidationError as e:
    print(e)