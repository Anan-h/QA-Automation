from pet_exercise.src.enum.pet_species import PetSpecies
from pet_exercise.src.classes.owner import Owner
from pet_exercise.src.classes.pet import Pet


class Cat(Pet):

    def __init__(self, name, age, owner: Owner, indoor, vaccinated):
        super().__init__(name, age, PetSpecies.CAT.value, owner, vaccinated)
        self.indoor = indoor

    @property
    def indoor(self):
        return self._indoor

    @indoor.setter
    def indoor(self, indoor: bool):
        try:
            self._indoor = indoor
        except TypeError as e:
            print(e)

    def is_living_indoor(self):
        if self._indoor:
            return "the cat lives indoor"
        else:
            return "the cat lives outside"

    def move_out_side(self):
        if self._indoor:
            self._indoor = False
        else:
            return "the cat lives outside the house"

    def __str__(self):
        owner_name = self.owner.name
        vaccinated = self.pet_is_vaccinated()
        indoor = self.is_living_indoor()
        return f"{self.name} (Cat:{self.age} years old, Owner: {owner_name}, {indoor}.{vaccinated} )"

    def to_dict(self):
        data = super().to_dict()
        data['indoor'] = self.indoor
        return data

    @classmethod
    def from_dict(cls, data, owner):
        return cls(data['name'], data['age'], owner, data['indoor'], data['vaccinated'])