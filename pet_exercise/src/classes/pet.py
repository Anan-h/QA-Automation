import json

from pet_exercise.src.classes.owner import Owner


class Pet:

    def __init__(self, name: str, age: int, species, owner: Owner, vaccinated):
        self.name = name
        self.age = age
        self.species = species
        self.owner = owner
        self.vaccinated = vaccinated

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        try:
            self._name = name
        except TypeError as e:
            print(e)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        try:
            self._age = age
        except TypeError as e:
            print(e)

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, name):
        try:
            self._owner = name
        except TypeError as e:
            print(e)

    @property
    def vaccinated(self):
        return self._vaccinated

    @vaccinated.setter
    def vaccinated(self, vaccinated: bool):
        try:
            self._vaccinated = vaccinated
        except TypeError as e:
            print(e)

    def pet_is_vaccinated(self):
        if self._vaccinated:
            return "the pet is vaccinated"
        else:
            return "the pet is not vaccinated"

    def vaccinate_pet(self):
        if self._vaccinated:
            return "the pet is already vaccinated"
        else:
            self.vaccinated = True

    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, species):
        try:
            self._species = species
        except TypeError as e:
            print(e)

    def get_pet_age_in_human_years(self):
        return f"this pet is: {self._age * 7} years old, in human years"

    def __eq__(self, other):
        if isinstance(other, Pet):
            return self.name == other.name and self.species == other.species
        return False

    def __str__(self):
        owner_name = self.owner.name
        vaccinated = self.pet_is_vaccinated()
        return f"{self.name} ({self.species}, {self.age} years old, Owner: {owner_name}.{vaccinated})"

    def to_dict(self):
        return {
            'name': self.name,
            'age': self.age,
            'owner_name': self.owner.name,
            'vaccinated': self.vaccinated,
            'species': self.species
        }

    @classmethod
    def from_dict(cls, data, owner):
        pass
