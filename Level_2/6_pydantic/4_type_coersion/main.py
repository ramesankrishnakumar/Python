from pydantic import BaseModel


class Coordinates(BaseModel):
    x: float
    y: float


p1 = Coordinates(x="1.1", y=2) # pydantic tries to transform this to the correct type

print(f"p1: {p1}") # p1: x=1.1 y=2.0
print(p1.model_fields)

# refer this https://docs.pydantic.dev/latest/concepts/conversion_table/ for
# the default type coercion and strict mode operation

