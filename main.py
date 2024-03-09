from dataclasses import dataclass
from enum import Enum

class Sex(Enum):
    MALE = "Male"
    FEMALE = "Female"

@dataclass
class Dog():
    name: str
    age: int
    breed: str
    skill: str
    sex: Sex

    @classmethod
    def create(cls, name, age, breed, skill, sex):
        if not isinstance(sex, Sex):
            raise TypeError(f"Expected type Sex for sex, but got {type(sex)}.")
        return cls(name, age, breed, skill, sex)

if __name__ == "__main__":
    dog = Dog(name="Musyamaro", age=3, breed="Golden Retriever", skill="Run", sex="M")
    print(dog.sex)
    