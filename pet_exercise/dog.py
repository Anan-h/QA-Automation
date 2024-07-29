from pet_exercise.enum.dog_breeds import DogBreeds
from pet_exercise.enum.pet_species import PetSpecies
from pet_exercise.owner import Owner
from pet_exercise.pet import Pet


class Dog(Pet):

    def __init__(self, name, age, owner: Owner, breed):
        super().__init__(name, age, PetSpecies.DOGS.value, owner)
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
        return f"{self.name} (Dog: {self.breed}, {self.age} years old, Owner: {owner_name} {vaccinated})"
