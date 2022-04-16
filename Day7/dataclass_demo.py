from dataclasses import dataclass


@dataclass
class Customers:
    id: int
    name: str
    age: int


customer1 = Customers(1, "subraja", 20)
print(customer1.name)
