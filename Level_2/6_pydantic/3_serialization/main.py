from pydantic import BaseModel


class Person(BaseModel):
    first_name: str # field, attribute
    last_name: str
    age: int



p1 = Person(first_name="John", last_name="Doe", age=23)
p2 = Person(first_name="T", last_name="Pain", age=20)

# {'first_name': 'John', 'last_name': 'Doe', 'age': 23}
# print(p1.__dict__) # this is of type dict

# serialize via model_dump(), looks almost same as __dict__ but model_dump() is customizable
# print(p1.model_dump()) # {'first_name': 'John', 'last_name': 'Doe', 'age': 23} # this is of type dict
# print(p2.model_dump(exclude={"age"})) # {'first_name': 'T', 'last_name': 'Pain'}

# serialize to json
# print(p1.model_dump_json()) # this is of type str
# print(p1.model_dump_json(indent=2)) # this is of type str
# print(p1.model_dump_json(exclude={'age'})) # {"first_name":"John","last_name":"Doe"}
# print(p2.model_dump_json(include={'age'})) # {"age":20}




