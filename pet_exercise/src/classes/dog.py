from pet_exercise.src.enum.pet_species import PetSpecies
from pet_exercise.src.classes.owner import Owner
from pet_exercise.src.classes.pet import Pet


class Dog(Pet):

    def __init__(self, name, age, owner: Owner, breed, vaccinated):
        super().__init__(name, age, PetSpecies.DOG.value, owner, vaccinated)
        self.breed = breed

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        try:
            self._breed = breed
        except TypeError as e:
            print(e)

    def __str__(self):
        owner_name = self.owner.name
        vaccinated = self.pet_is_vaccinated()
        return f"{self.name} (Dog: {self.breed}, {self.age} years old, Owner: {owner_name}. {vaccinated})"

    def to_dict(self):
        data = super().to_dict()
        data['breed'] = self.breed
        return data

    @classmethod
    def from_dict(cls, data, owner):
        return cls(data['name'], data['age'], owner, data['breed'], data['vaccinated'])
